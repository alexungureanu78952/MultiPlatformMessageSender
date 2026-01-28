"""
WhatsApp sender module using Selenium
Sends WhatsApp messages with images via WhatsApp Web
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pathlib import Path
import time


def send_whatsapp(config, logger):
    """
    Send WhatsApp text message using Selenium
    
    IMPORTANT: 
    - Prima dată trebuie să scanezi QR code
    - După scanare, sesiunea rămâne salvată
    - Trimite doar text, fără imagini
    
    Args:
        config: Config object with recipient phone number
        logger: Logger instance
        
    Returns:
        bool: True if successful, False otherwise
    """
    driver = None
    
    try:
        logger.info("=== Starting WhatsApp sending ===")
        
        # Setup Chrome driver
        logger.info("Setting up Chrome driver...")
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-notifications')
        options.add_argument('--disable-popup-blocking')
        
        # User data directory for persistent session
        user_data_dir = Path(__file__).parent.parent / 'sessions' / 'whatsapp_chrome'
        user_data_dir.mkdir(parents=True, exist_ok=True)
        options.add_argument(f'--user-data-dir={user_data_dir}')
        
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
        
        logger.info("Opening WhatsApp Web...")
        driver.get('https://web.whatsapp.com/')
        
        # Wait for QR code or chat interface
        logger.info("⚠ Așteaptă încărcarea WhatsApp Web...")
        logger.info("⚠ Dacă e prima dată, scanează QR code-ul!")
        
        try:
            # Wait for search box (indicates logged in)
            WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
            )
            logger.info("✓ WhatsApp Web loaded successfully")
        except:
            logger.error("✗ Timeout waiting for WhatsApp Web. Please scan QR code if shown.")
            return False
        
        # Get recipient phone and message
        phone = config.recipient['whatsapp_phone']
        message_text = config.message.get('whatsapp_caption', config.message['text'])
        
        logger.info(f"Searching for contact: {phone}")
        
        # Navigate directly to chat URL
        # Remove + and spaces from phone number for URL
        clean_phone = phone.replace('+', '').replace(' ', '').replace('-', '')
        chat_url = f'https://web.whatsapp.com/send?phone={clean_phone}'
        
        logger.info(f"Opening chat with {phone}...")
        driver.get(chat_url)
        time.sleep(5)
        
        # Wait for message input box to appear
        try:
            message_box = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]'))
            )
            logger.info(f"✓ Contact {phone} chat opened")
            time.sleep(2)
        except:
            logger.error(f"✗ Could not open chat with {phone}. Verifică că numărul e corect și salvat.")
            return False
        
        # Send text message
        try:
            logger.info(f"Sending message: {message_text}")
            
            # Click in message box and type
            message_box.click()
            time.sleep(0.5)
            message_box.send_keys(message_text)
            time.sleep(1)
            
            # Send with Enter key
            message_box.send_keys(Keys.ENTER)
            logger.info("✓ Message sent successfully")
            time.sleep(2)
            
        except Exception as e:
            logger.error(f"✗ Failed to send message: {str(e)}")
            return False
        
        logger.info(f"✓ WhatsApp messages sent to {phone}")
        return True
        
    except Exception as e:
        logger.error(f"✗ WhatsApp sending failed: {str(e)}")
        logger.error("Verifică că ai scanat QR code-ul și că numărul de telefon e corect")
        return False
        
    finally:
        if driver:
            logger.info("Closing browser...")
            time.sleep(3)
            driver.quit()
