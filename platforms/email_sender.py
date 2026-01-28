"""
Email sender module using Gmail
Sends email with multiple image attachments
"""
import yagmail
from pathlib import Path


def send_email(config, logger):
    """
    Send email with images using Gmail
    
    Args:
        config: Config object with credentials and recipient info
        logger: Logger instance
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        logger.info("=== Starting Email sending ===")
        
        # Get image files
        images = config.get_image_files()
        if not images:
            logger.warning("No images found in images folder")
            return False
        
        logger.info(f"Found {len(images)} images to send")
        
        # Initialize yagmail
        yag = yagmail.SMTP(
            user=config.gmail_user,
            password=config.gmail_password
        )
        
        # Prepare email content
        recipient = config.recipient['email']
        subject = config.message['subject']
        body = config.message['text']
        
        logger.info(f"Sending email to {recipient}")
        
        # Send email with attachments
        yag.send(
            to=recipient,
            subject=subject,
            contents=[body],
            attachments=images
        )
        
        logger.info(f"✓ Email sent successfully to {recipient}")
        logger.info(f"  - Attached {len(images)} images")
        return True
        
    except Exception as e:
        logger.error(f"✗ Email sending failed: {str(e)}")
        return False
