"""
Main script to send messages with images across multiple platforms
Designed to run once via Windows Task Scheduler on February 16, 2026 at 00:00

Usage:
    python main.py
"""

from utils import Config, setup_logger
from platforms import send_email, send_whatsapp
from datetime import datetime


def main():
    """Main execution function"""
    
    # Setup logger
    logger = setup_logger('vscode_spam')
    
    logger.info("=" * 60)
    logger.info("VS CODE MEMES SENDER - Starting execution")
    logger.info(f"Execution time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info("=" * 60)
    
    try:
        # Load configuration
        logger.info("Loading configuration...")
        config = Config()
        logger.info("✓ Configuration loaded successfully")
        
        # Check if images exist
        images = config.get_image_files()
        if not images:
            logger.error("✗ No images found in images folder!")
            logger.error(f"  Please add images to: {config.images_folder}")
            return
        
        logger.info(f"Found {len(images)} images to send")
        for img in images:
            logger.info(f"  - {img}")
        
        logger.info("")
        
        # Results tracking
        results = {
            'email': False,
            'whatsapp': False
        }
        
        # 1. Send via Email (subject + text + images)
        logger.info("\n" + "=" * 60)
        results['email'] = send_email(config, logger)
        logger.info("=" * 60)
        
        # 2. Send via WhatsApp (text only)
        logger.info("\n" + "=" * 60)
        results['whatsapp'] = send_whatsapp(config, logger)
        logger.info("=" * 60)
        
        # Final summary
        logger.info("\n" + "=" * 60)
        logger.info("EXECUTION SUMMARY")
        logger.info("=" * 60)
        
        success_count = sum(results.values())
        total_count = len(results)
        
        logger.info(f"Total platforms: {total_count}")
        logger.info(f"Successful: {success_count}")
        logger.info(f"Failed: {total_count - success_count}")
        logger.info("")
        
        for platform, success in results.items():
            status = "✓ SUCCESS" if success else "✗ FAILED"
            logger.info(f"  {platform.upper()}: {status}")
        
        logger.info("=" * 60)
        
        if success_count == total_count:
            logger.info("🎉 All messages sent successfully!")
        elif success_count > 0:
            logger.info("⚠ Partial success - some platforms failed")
        else:
            logger.error("✗ All platforms failed - check configuration and logs")
        
        logger.info("=" * 60)
        
    except FileNotFoundError as e:
        logger.error(f"✗ Configuration file not found: {str(e)}")
        logger.error("Please copy .env.example to .env and config.json.example to config.json")
        logger.error("Then fill in your credentials and recipient information")
        
    except Exception as e:
        logger.error(f"✗ Unexpected error: {str(e)}")
        import traceback
        logger.error(traceback.format_exc())
    
    finally:
        logger.info("\nExecution completed")
        logger.info(f"End time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


if __name__ == "__main__":
    main()
