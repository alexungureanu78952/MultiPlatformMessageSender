# Script de test rapid pentru verificarea configurației

from utils import Config, setup_logger
from pathlib import Path

def test_config():
    """Testează dacă configurația este validă"""
    logger = setup_logger('test_config')
    
    print("\n" + "="*60)
    print("🧪 TEST CONFIGURAȚIE")
    print("="*60 + "\n")
    
    try:
        # Test loading config
        print("1. Încarcă configurația...")
        config = Config()
        print("   ✓ Configurația a fost încărcată\n")
        
        # Test credentials
        print("2. Verifică credențialele:")
        print(f"   Gmail: {config.gmail_user}")
        print(f"   Gmail Password: {'***' if config.gmail_password else 'LIPSĂ'}")
        print(f"   Instagram: {config.instagram_username}")
        print(f"   Instagram Password: {'***' if config.instagram_password else 'LIPSĂ'}")
        print(f"   Facebook: {config.facebook_email}")
        print(f"   Facebook Password: {'***' if config.facebook_password else 'LIPSĂ'}\n")
        
        # Test recipient info
        print("3. Informații destinatar:")
        print(f"   Nume: {config.recipient['name']}")
        print(f"   Email: {config.recipient['email']}")
        print(f"   Instagram: {config.recipient['instagram_username']}")
        print(f"   WhatsApp: {config.recipient['whatsapp_phone']}\n")
        
        # Test images
        print("4. Verifică imaginile:")
        images = config.get_image_files()
        if images:
            print(f"   ✓ Găsite {len(images)} imagini:")
            for img in images:
                print(f"     - {Path(img).name}")
        else:
            print("   ✗ NU există imagini în folder!")
            print(f"     Adaugă imagini în: {config.images_folder}\n")
            return False
        
        print("\n" + "="*60)
        print("✓ TOATE VERIFICĂRILE AU TRECUT!")
        print("="*60 + "\n")
        print("Poți rula acum: python main.py")
        print()
        return True
        
    except FileNotFoundError as e:
        print(f"\n✗ EROARE: Fișier lipsă - {e}")
        print("\nPași de rezolvare:")
        print("1. Copiază config.json.example la config.json")
        print("2. Completează toate credențialele și datele destinatarului")
        return False
        
    except Exception as e:
        print(f"\n✗ EROARE: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    test_config()
