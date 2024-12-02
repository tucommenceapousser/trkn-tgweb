import streamlit as st
from telegram import Bot
from telegram.error import TelegramError
import os
import json

# Chemins des fichiers de stockage temporaire
sent_messages_file = "sent_messages.json"
received_messages_file = "received_messages.json"

# Fonction pour charger les messages depuis le fichier
def load_messages(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return json.load(f)
    return []

# Fonction pour sauvegarder les messages dans le fichier
def save_messages(file_path, messages):
    with open(file_path, "w") as f:
        json.dump(messages, f)

# Fonction pour réinitialiser les messages dans les fichiers
def reset_messages():
    # Vider les fichiers de messages
    save_messages(sent_messages_file, [])
    save_messages(received_messages_file, [])
    # Réinitialiser les listes locales aussi
    st.session_state.received_messages = []
    st.session_state.sent_messages = []

# Initialisation de l'état des messages dans session_state
if "sent_messages" not in st.session_state:
    st.session_state.sent_messages = load_messages(sent_messages_file)
if "received_messages" not in st.session_state:
    st.session_state.received_messages = load_messages(received_messages_file)

# Gestion de l'état de la session
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "page" not in st.session_state:
    st.session_state.page = "login"

# Si l'utilisateur est authentifié
if st.session_state.authenticated:
    st.session_state.page = "main"  # Mettre à jour l'état de la page à "main"

# Logique de la page de login
if st.session_state.page == "login":
    # Affichage du logo de la page de login
    st.image("https://a.top4top.io/p_3257d4x8a0.png", width=300)
    password = st.text_input("🔑 Entrez le mot de passe:", type="password")

    # Vérification du mot de passe
    if password == "trkntrkn":
        st.session_state.authenticated = True  # Authentifier l'utilisateur
        st.success("Connexion réussie! ✅")
        st.session_state.page = "main"  # Diriger vers la page principale
    elif password:
        st.error("Mot de passe incorrect.")

# Si l'utilisateur est connecté, afficher la page principale
if st.session_state.page == "main":
    # Ajouter des styles pour le fond d'écran et l'affichage du logo principal
    st.markdown("""
        <style>
        .stApp {
            background: url('https://b.top4top.io/p_3257e0tsm0.png') no-repeat center center fixed;
            background-size: cover;
            color: #33FF33;
            font-family: 'Courier New', monospace;
        }
        h1 {
            color: #00FF00;
            text-align: center;
            font-size: 3em;
            text-shadow: 0 0 5px #33FF33, 0 0 10px #33FF33, 0 0 20px #33FF33;
        }
        .message-box {
            background-color: rgba(0, 0, 0, 0.8);
            padding: 10px;
            border-radius: 5px;
            margin-bottom: 10px;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)

    # Affichage du logo principal
    st.image("https://c.top4top.io/p_3257z2e3f1.jpg", width=500)
    st.title("🌍 Free Gaza Telegram Bot")

    # Demander le token du bot à l'utilisateur
    token = st.text_input("🔑 Entrez votre token API Telegram Bot:", type="password", key="token")

    if token:
        bot = Bot(token=token)
        st.success("✅ Votre bot est prêt à être utilisé!")

        # Zone pour entrer le chat ID du destinataire
        recipient_chat_id = st.text_input("📩 Entrez le chat ID du destinataire:")

        # Zone pour entrer un message
        message = st.text_area("💬 Entrez un message à envoyer au destinataire:")

        # Bouton pour envoyer le message
        if st.button("Envoyer le message"):
            if recipient_chat_id and message:
                try:
                    bot.send_message(chat_id=recipient_chat_id, text=message)
                    st.success("Message envoyé avec succès! ✅")
                    st.session_state.sent_messages.append(f"Envoyé: {message}")
                    save_messages(sent_messages_file, st.session_state.sent_messages)
                except TelegramError as e:
                    st.error(f"Erreur: {e}")
            else:
                st.warning("⚠️ Veuillez entrer un chat ID et un message.")

        # Affichage des messages envoyés
        st.write("### 📜 Messages envoyés :")
        for msg in st.session_state.sent_messages:
            st.markdown(f"<div class='message-box'>{msg}</div>", unsafe_allow_html=True)

        # Bouton pour réinitialiser les messages envoyés
        if st.button("🗑️ Réinitialiser les messages envoyés"):
            reset_messages()  # Réinitialise les fichiers et les listes locales
            st.session_state.sent_messages = []  # Effacer les messages envoyés
            st.session_state.received_messages = []  # Effacer les messages reçus

        # Bouton pour rafraîchir les messages reçus sans recharger toute la page
        if st.button("🔄 Recharger les messages reçus"):
            try:
                updates = bot.get_updates(timeout=5)
                for update in updates:
                    if update.message and update.message.text:
                        received_message = f"De {update.message.chat.username or 'Inconnu'} : {update.message.text}"
                        if received_message not in st.session_state.received_messages:
                            st.session_state.received_messages.append(received_message)
                save_messages(received_messages_file, st.session_state.received_messages)
            except TelegramError as e:
                st.error(f"Erreur lors de la récupération des messages : {e}")

        # Affichage des messages reçus
        st.write("### 📥 Messages reçus :")
        for msg in st.session_state.received_messages:
            st.markdown(f"<div class='message-box'>{msg}</div>", unsafe_allow_html=True)

        # Bouton pour réinitialiser les messages reçus
        if st.button("🗑️ Réinitialiser les messages reçus"):
            reset_messages()  # Réinitialise les fichiers et les listes locales
            st.session_state.received_messages = []  # Effacer les messages reçus
            save_messages(received_messages_file, st.session_state.received_messages)  # Sauvegarder après réinitialisation