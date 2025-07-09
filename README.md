# 📬 Telegram to Google Sheet

Ce projet est un **bot Telegram** qui écoute un **canal** spécifique, extrait les adresses **e-mail** des messages (y compris ceux avec des boutons), et les enregistre automatiquement dans un **Google Sheets**.

## 🚀 Fonctionnalités

- Écoute un canal Telegram public ou privé
- Récupère automatiquement les e-mails dans les messages postés
- Évite les doublons
- Stocke les données dans un Google Sheets (cloud)
- Fonctionne en continu (grâce à PM2 ou autre)

---

## 🛠️ Prérequis

- Python 3.9 ou supérieur (testé avec Python 3.12)
- Un projet Google Cloud avec une feuille Google Sheets
- Un bot Telegram avec le token
- Accès en écriture à un canal Telegram (le bot doit être admin)

---

## 📦 Installation

Clone le dépôt :

```bash
git clone https://github.com/votre-utilisateur/telegram-email-bot.git
cd telegram-email-bot
```

## Crée et active un environnement virtuel :

```bash
python3 -m venv venv
source venv/bin/activate
```
## Installe les dépendances :

```bash
pip install -r requirements.txt
```
## 🔐 Configuration

1. Google Sheets API
- Crée un projet sur console.cloud.google.com

- Active l'API Google Sheets + Google Drive

- Crée un compte de service et télécharge le fichier credentials.json

- Partage votre feuille Google Sheets avec l’e-mail du compte de service

2. Feuille Google Sheets
- Crée une feuille nommée emails_telegram, avec la première colonne destinée aux emails.

3. Telegram Bot
è Crée un bot via @BotFather

- Ajoute le bot dans ton canal Telegram

- Donne-lui le rôle d'administrateur

- Récupère l’identifiant du canal (CHANNEL_ID) via @getidsbot

## ⚙️ Configuration dans main.py

- Modifie ces constantes selon ton setup :
```bash
TELEGRAM_TOKEN = 'VOTRE_TOKEN_ICI'
CHANNEL_ID = -1001234567890  # Remplace par l'ID de ton canal
GOOGLE_SHEET_NAME = 'emails_telegram'
```
- Assure-toi que credentials.json est dans le dossier du script.

## ▶️ Lancer le bot

```bash
python3 main.py
```

## 🧪 Tester
Poste un message contenant une adresse email dans ton canal. Tu devrais voir :

✅ Bot lancé. En écoute sur le canal...
Message reçu dans le handler
Emails extraits: [...]
[Ajouté] exemple@email.com

## 📌 Lancer en production avec PM2
Pour que le bot tourne en arrière-plan même après fermeture SSH :

```bash
npm install -g pm2
pm2 start main.py --interpreter python3 --name telegram-bot
pm2 save
pm2 startup
```

## 🧼 Sécurité
Ne jamais partager credentials.json ou ton token Telegram

Utilise .gitignore pour exclure les fichiers sensibles :

```bash
venv/
__pycache__/
credentials.json
```

## 📚 Technologies utilisées
python-telegram-bot v20+

gspread pour Google Sheets

oauth2client pour l’authentification Google

apscheduler (via telegram-ext)

PM2 pour gestion en production

## 🤝 Contribuer
Les pull requests sont les bienvenues. Merci de proposer des idées ou des améliorations !

👨‍💻 Auteur
Développé par Bristhis Degbeko.
https://bristhisdegbeko.fr/
