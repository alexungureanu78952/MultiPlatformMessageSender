"""
Config loader utility
Loads JSON config with all credentials and settings
"""
import json
from pathlib import Path


class Config:
    def __init__(self):
        # Load config.json
        config_path = Path(__file__).parent.parent / 'config.json'
        with open(config_path, 'r', encoding='utf-8') as f:
            self.config = json.load(f)
        
        # Email credentials
        self.gmail_user = self.config['credentials']['gmail']['user']
        self.gmail_password = self.config['credentials']['gmail']['app_password']
        
        # Instagram credentials
        self.instagram_username = self.config['credentials']['instagram']['username']
        self.instagram_password = self.config['credentials']['instagram']['password']
        
        # Facebook credentials
        self.facebook_email = self.config['credentials']['facebook']['email']
        self.facebook_password = self.config['credentials']['facebook']['password']
        
        # Recipient info
        self.recipient = self.config['recipient']
        self.message = self.config['message']
        
        # Images folder
        self.images_folder = Path(__file__).parent.parent / self.config['images_folder']
    
    def get_image_files(self):
        """Get all image files from the images folder"""
        if not self.images_folder.exists():
            return []
        
        image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'}
        return [
            str(img) for img in self.images_folder.iterdir()
            if img.suffix.lower() in image_extensions
        ]
