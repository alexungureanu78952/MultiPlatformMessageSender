# VS Code Memes Multi-Platform Sender 💻📸

Script Python pentru trimiterea automată de mesaje cu imagini (screenshot-uri și meme-uri VS Code) pe 4 platforme: **Email**, **WhatsApp**, **Instagram**, și **Facebook Messenger**.

Proiectat să ruleze o singură dată pe **16 februarie 2026 la ora 00:00** prin Windows Task Scheduler.

---

## 📋 Cerințe

- Python 3.8+
- Windows 10/11 (pentru Task Scheduler)
- Chrome browser (pentru Messenger)
- Conturi active pe:
  - Gmail (cu App Password)
  - WhatsApp
  - Instagram
  - Facebook

---

## 🚀 Instalare

### 1. Clonează/Descarcă proiectul

```bash
cd d:\cod\IA\vscode_ss_spam
```

### 2. Creează mediu virtual (recomandat)

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instalează dependențele

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configurare

### 1. Creează fișierul `.env`

Copiază `.env.example` la `.env` și completează credențialele:

```bash
copy .env.example .env
```

Editează `.env`:

```env
# Gmail Settings
GMAIL_USER=your_email@gmail.com
GMAIL_APP_PASSWORD=xxxx xxxx xxxx xxxx

# Instagram Credentials
INSTAGRAM_USERNAME=your_username
INSTAGRAM_PASSWORD=your_password

# Facebook Credentials
FACEBOOK_EMAIL=your_email@example.com
FACEBOOK_PASSWORD=your_password
```

#### 🔐 Cum obții Gmail App Password:

1. Du-te la [Google Account Security](https://myaccount.google.com/security)
2. Activează **2-Step Verification**
3. Mergi la **App Passwords**
4. Selectează **Mail** și **Windows Computer**
5. Copiază parola de 16 caractere generată

### 2. Creează fișierul `config.json`

Copiază `config.json.example` la `config.json`:

```bash
copy config.json.example config.json
```

Editează `config.json` cu informațiile prietenei tale:

```json
{
  "recipient": {
    "name": "Numele Prietenei",
    "email": "prietena@example.com",
    "instagram_username": "username_instagram",
    "facebook_id": "100012345678901",
    "whatsapp_phone": "+40712345678"
  },
  "message": {
    "subject": "Happy Valentine's Day! 💻",
    "text": "Am câștigat pariul! Iată screenshot-urile și meme-urile cu VS Code promise! 🎉",
    "whatsapp_caption": "Pariul câștigat! VS Code memes 😎"
  },
  "images_folder": "images"
}
```

**Note importante:**
- `whatsapp_phone`: Format internațional cu `+` (ex: `+40712345678`)
- `facebook_id`: Nu e necesar, se folosește numele pentru căutare

### 3. Adaugă imaginile

Pune toate screenshot-urile și meme-urile în folder-ul `images/`:

```
images/
  ├── screenshot1.png
  ├── screenshot2.png
  ├── meme1.jpg
  └── meme2.jpg
```

Formate suportate: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.webp`

---

## 🧪 Testare

**FOARTE IMPORTANT:** Testează script-ul înainte de 16 februarie!

### Test complet:

```bash
python main.py
```

### Test individual pe platformă:

```python
# Test doar email
from utils import Config, setup_logger
from platforms import send_email

logger = setup_logger()
config = Config()
send_email(config, logger)
```

### ⚠️ Aspecte importante la prima rulare:

1. **WhatsApp:**
   - Va deschide browser automat
   - Trebuie să scanezi QR code prima dată
   - După scanare, sesiunea rămâne activă
   - **Testează înainte de data stabilită!**

2. **Instagram:**
   - Prima autentificare salvează sesiunea
   - Dacă ai 2FA, confirmă login-ul în aplicația Instagram
   - Așteaptă 45 secunde între imagini (rate limiting)

3. **Facebook Messenger:**
   - Prima dată te loghezi manual în browser
   - Sesiunea rămâne salvată în profil Chrome
   - Verifică că numele destinatarului e corect

4. **Email:**
   - Cel mai fiabil
   - Nu necesită intervenție după setup

---

## 📅 Configurare Windows Task Scheduler

### Metoda 1: Interfață grafică

1. Deschide **Task Scheduler** (caută "Task Scheduler" în Start Menu)

2. Click **Create Basic Task**

3. Completează:
   - **Name:** VS Code Memes Sender
   - **Description:** Trimite meme-uri VS Code pe 16 februarie la 00:00

4. **Trigger:**
   - Selectează **One time**
   - **Date:** 16/02/2026
   - **Time:** 00:00:00

5. **Action:**
   - Selectează **Start a program**
   - **Program/script:** `D:\cod\IA\vscode_ss_spam\venv\Scripts\python.exe`
   - **Add arguments:** `main.py`
   - **Start in:** `D:\cod\IA\vscode_ss_spam`

6. **Finish** și verifică task-ul creat

### Metoda 2: PowerShell (rapid)

Rulează în PowerShell ca Administrator:

```powershell
$action = New-ScheduledTaskAction -Execute "D:\cod\IA\vscode_ss_spam\venv\Scripts\python.exe" -Argument "main.py" -WorkingDirectory "D:\cod\IA\vscode_ss_spam"

$trigger = New-ScheduledTaskTrigger -Once -At "2026-02-16T00:00:00"

$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries

Register-ScheduledTask -TaskName "VSCodeMemesSender" -Action $action -Trigger $trigger -Settings $settings -Description "Trimite meme-uri VS Code pe 16 februarie la miezul nopții"
```

### Verificare task:

```powershell
Get-ScheduledTask -TaskName "VSCodeMemesSender"
```

### Rulare manuală pentru test:

```powershell
Start-ScheduledTask -TaskName "VSCodeMemesSender"
```

---

## 📝 Log-uri

Toate execuțiile sunt înregistrate în folder-ul `logs/`:

```
logs/
  └── vscode_spam_20260216_000001.log
```

Log-urile conțin:
- Timestamp-uri detaliate
- Status pentru fiecare platformă
- Erori și warnings
- Rezumat final

---

## 🔧 Troubleshooting

### Email nu funcționează

- ✅ Verifică că ai activat 2FA în Gmail
- ✅ Verifică că ai generat App Password corect
- ✅ Nu folosești parola obișnuită, ci App Password
- ✅ `GMAIL_USER` e adresa ta completă (ex: `user@gmail.com`)

### WhatsApp nu trimite

- ✅ Prima dată testează manual pentru QR code
- ✅ Verifică formatul numărului: `+40712345678` (cu `+`)
- ✅ Nu delogha WhatsApp Web între test și execuție finală
- ✅ Browser-ul trebuie să aibă acces la WhatsApp Web

### Instagram eșuează

- ✅ Username și parolă corecte în `.env`
- ✅ Confirmă login în app dacă ai 2FA
- ✅ Nu schimba parola între test și execuție
- ✅ Verifică că username-ul destinatarului e corect
- ✅ Contul tău Instagram nu e nou (risc de ban mai mare)

### Messenger nu găsește persoana

- ✅ Verifică că numele din `config.json` e exact cum apare în Messenger
- ✅ Loghează-te manual prima dată
- ✅ Chrome trebuie să fie instalat
- ✅ Permite browser-ului să ruleze (nu-l închide manual)

### Task Scheduler nu rulează

- ✅ Verifică că path-urile sunt absolute și corecte
- ✅ PC-ul trebuie să fie pornit la ora setată
- ✅ Dacă e laptop, trebuie să fie pe priză sau permite rularea pe baterie
- ✅ Verifică în Event Viewer dacă există erori

---

## 📁 Structura Proiectului

```
vscode_ss_spam/
├── platforms/              # Module pentru fiecare platformă
│   ├── __init__.py
│   ├── email_sender.py    # Gmail cu yagmail
│   ├── whatsapp.py        # WhatsApp cu pywhatkit
│   ├── instagram.py       # Instagram cu instagrapi
│   └── messenger.py       # Facebook cu Selenium
├── utils/                  # Utilități
│   ├── __init__.py
│   ├── config_loader.py   # Încarcă .env și config.json
│   └── logger.py          # Logging sistem
├── images/                 # Imaginile tale (screenshot-uri, meme-uri)
│   └── .gitkeep
├── sessions/               # Sesiuni salvate (Instagram, Chrome)
│   └── .gitkeep
├── logs/                   # Log-uri execuție
│   └── .gitkeep
├── main.py                # Script principal
├── requirements.txt       # Dependențe Python
├── .env                   # Credențiale (NU face commit!)
├── .env.example          # Template pentru .env
├── config.json           # Configurație destinatar (NU face commit!)
├── config.json.example   # Template pentru config.json
├── .gitignore            # Exclud fișiere sensibile
└── README.md             # Această documentație
```

---

## ⚡ Flux de Execuție

1. Script-ul se pornește la data și ora setată (16 feb, 00:00)
2. Încarcă configurația din `.env` și `config.json`
3. Verifică existența imaginilor în folder `images/`
4. Trimite pe fiecare platformă în ordine:
   - **Email** (cel mai fiabil)
   - **WhatsApp** (necesită browser)
   - **Instagram** (rate limiting de 45s între imagini)
   - **Messenger** (necesită browser)
5. Dacă o platformă eșuează, continuă cu următoarea
6. Loghează succesul/eșecul fiecărei platforme
7. Generează raport final în log
8. Se închide automat

**Durata estimată:** 5-15 minute (depinde de numărul de imagini)

---

## 🛡️ Securitate

- ⚠️ **NU face commit la `.env` sau `config.json`** (conțin date sensibile)
- ✅ Folosește `.env.example` și `config.json.example` ca template
- ✅ `.gitignore` exclude automat fișierele sensibile
- ✅ Sesiunile Instagram și Chrome sunt locale
- ✅ Log-urile NU conțin parole

---

## 📞 Support

Dacă întâmpini probleme:

1. Verifică log-urile în `logs/`
2. Rulează manual `python main.py` pentru debugging
3. Testează fiecare platformă individual
4. Verifică că toate credențialele sunt corecte

---

## 🎉 Succes!

După configurare și testare, script-ul va trimite automat toate mesajele pe 16 februarie la miezul nopții. Baftă la pariu! 🏆

---

**Creat:** Ianuarie 2026  
**Target Date:** 16 Februarie 2026, 00:00  
**Platforms:** Email, WhatsApp, Instagram, Facebook Messenger
