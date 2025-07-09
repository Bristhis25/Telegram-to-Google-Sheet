import pytz
import apscheduler.util

def patched_astimezone(tz):
    if tz is None:
        return pytz.utc
    if isinstance(tz, pytz.BaseTzInfo):
        return tz
    try:
        import zoneinfo
        if isinstance(tz, zoneinfo.ZoneInfo):
            return pytz.timezone(str(tz))
    except ImportError:
        pass
    return pytz.utc

apscheduler.util.astimezone = patched_astimezone

# Maintenant les imports normaux
import re
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# === CONFIGURATION ===

TELEGRAM_TOKEN = 'token telegram à recup sur botfather'
CHANNEL_ID = id du canal
GOOGLE_SHEET_NAME = 'nom de la feuille de calcul'

# === GOOGLE SHEETS SETUP ===

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open(GOOGLE_SHEET_NAME).sheet1

# === FONCTIONS ===

def extract_emails(text):
    return re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

def is_duplicate(email):
    existing_emails = sheet.col_values(1)
    return email in existing_emails

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Message reçu dans le handler")

    chat_id = None
    text = None

    if update.effective_chat:
        chat_id = update.effective_chat.id
        print(f"ID chat : {chat_id} (attendu {CHANNEL_ID})")

    # Pour les messages dans un canal, c'est update.channel_post
    if update.message:
        text = update.message.text
        print("Message dans update.message")
    elif update.channel_post:
        text = update.channel_post.text
        print("Message dans update.channel_post")
    else:
        print("Aucun message texte trouvé dans update.message ni update.channel_post")

    if chat_id == CHANNEL_ID:
        if text:
            print(f"Texte du message: {text}")
            emails = extract_emails(text)
            print(f"Emails extraits: {emails}")
            for email in emails:
                if not is_duplicate(email):
                    sheet.append_row([email])
                    print(f"[Ajouté] {email}")
                else:
                    print(f"[Déjà présent] {email}")
        else:
            print("Message texte absent")
    else:
        print("Message reçu d'un chat différent")

# === MAIN ===

if __name__ == '__main__':
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    # Écoute tous les types de messages pour capter aussi channel_post
    app.add_handler(MessageHandler(filters.ALL, handle_message))
    print("✅ Bot lancé. En écoute sur le canal...")
    app.run_polling()
