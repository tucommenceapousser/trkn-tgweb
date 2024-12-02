# trkn-tgweb

🔒 **trkn-tgweb** est une application web sécurisée développée avec **Streamlit**, permettant d'interagir avec des bots Telegram de manière intuitive et rapide.  
Créé par **trhacknon**, ce projet vise à simplifier l'envoi et la gestion des messages via l'API Telegram.

## SCREENSHOT
![trkn-tgweb Screenshot](https://g.top4top.io/p_325854bfp0.jpg)

## 🤖 Comment créer un bot Telegram avec BotFather

Pour utiliser **trkn-tgweb**, vous aurez besoin d'un bot Telegram et de son token d'API. Voici les étapes pour créer votre bot avec [BotFather](https://t.me/botfather) :

### 1. Démarrer BotFather
1. Ouvrez Telegram.
2. Recherchez **BotFather** ou cliquez directement ici : [BotFather](https://t.me/botfather).
3. Cliquez sur **Start** pour commencer.

### 2. Créer un nouveau bot
1. Tapez la commande suivante :

/newbot

2. BotFather vous demandera un nom pour votre bot. Entrez un nom (exemple : `trknwebbot`).
3. BotFather vous demandera ensuite un **nom d'utilisateur** unique pour le bot, qui doit se terminer par `bot`.  
Exemple : `trknwebbot_bot`.

### 3. Obtenir le token d'API
Une fois le bot créé, BotFather vous fournira un **token d'API**. Il ressemblera à ceci :

123456789:ABCDefghIJKlmnopQRSTUvwxYZ12345

**Conservez ce token précieusement**, vous en aurez besoin pour configurer votre bot avec **trkn-tgweb**.

### 4. Configurer votre bot avec trkn-tgweb
1. Accédez à votre interface [trkn-tgweb](https://trkn-tgweb.onrender.com).
2. Entrez le token d'API dans le champ correspondant.
3. Cliquez sur **Valider** pour connecter votre bot.

Et voilà ! Votre bot est maintenant prêt à envoyer et recevoir des messages via l'interface **trkn-tgweb**.

## 📜 Fonctionnalités

- 🔑 **Authentification sécurisée** avec mot de passe (`P@ssw0rd`).
- 📩 **Envoi de messages** vers un bot Telegram en utilisant son Token et le chat ID du destinataire.
- 📋 **Réinitialisation et gestion** des messages envoyés et reçus.
- 🌌 **Interface utilisateur** fluide et moderne, avec un design contrasté et des éléments graphiques stylisés.

## 🎯 Prérequis

- **Python 3.8+**
- **Bibliothèques nécessaires** :
  - `streamlit`
  - `python-telegram-bot`

## 🚀 Installation et utilisation

1. Clonez ce dépôt :

   ```bash
   git clone https://github.com/tucommenceapousser/trkn-tgweb.git
   cd trkn-tgweb

2. Installez les dépendances requises :

pip install -r requirements.txt


3. Lancez l'application :

```
streamlit run --server.enableCORS=true --server.enableWebsocketCompression=false --server.runOnSave=false main.py
```


4. Accédez à l'application via http://localhost:8501.

## 🌐 Démo en ligne

Découvrez la démo en ligne de **trkn-tgweb** ici :  
[🔗 trkn-tgweb Demo](https://trkn-tgweb.onrender.com)

🛡️ Authentification

Mot de passe par défaut pour accéder à l'application :
P@ssw0rd

## 🚀 Déployer trkn-tgweb

Vous pouvez déployer **trkn-tgweb** facilement sur différentes plateformes d'hébergement. Cliquez sur les boutons ci-dessous pour commencer :

### 1. Déployer sur Replit
[![Déployer sur Replit](https://img.shields.io/badge/Deploy%20on%20Replit-FF6C37?style=for-the-badge&logo=replit&logoColor=lime)](https://replit.com/new/github/tucommenceapousser/trkn-tgweb)

### 2. Déployer sur Render
[![Déployer sur Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/tucommenceapousser/trkn-tgweb)

🛠️ Développement

Développé par trhacknon pour automatiser et améliorer la communication via Telegram en quelques clics.

📄 Licence

Ce projet est sous licence libre. Utilisez-le et modifiez-le selon vos besoins.


---

💻 Développeur : trhacknon
🌐 trhacknon.dev | 📬 trhacknon@protonmail.ch
