import streamlit as st
from telegram import Bot
from telegram.error import TelegramError
import os
import json

sent_messages_file = "sent_messages.json"
received_messages_file = "received_messages.json"

def load_messages(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return json.load(f)
    return []

def save_messages(file_path, messages):
    with open(file_path, "w") as f:
        json.dump(messages, f)

def reset_messages():
    save_messages(sent_messages_file, [])
    save_messages(received_messages_file, [])

    st.session_state.received_messages = []
    st.session_state.sent_messages = []

if "sent_messages" not in st.session_state:
    st.session_state.sent_messages = load_messages(sent_messages_file)
if "received_messages" not in st.session_state:
    st.session_state.received_messages = load_messages(received_messages_file)

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "page" not in st.session_state:
    st.session_state.page = "login"

if st.session_state.authenticated:
    st.session_state.page = "main"

if st.session_state.page == "login":

    st.image("https://a.top4top.io/p_3257d4x8a0.png", width=300)
    password = st.text_input("🔑 Entrez le mot de passe:", type="password")

    if password == "P@ssw0rd":
        st.session_state.authenticated = True
        st.success("Connexion réussie! ✅")
        st.session_state.page = "main"
    elif password:
        st.error("Mot de passe incorrect.")

if st.session_state.page == "main":

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
    st.image("https://c.top4top.io/p_3257z2e3f1.jpg", width=500)
    st.title("🌍 Free Gaza Telegram Bot Dev by")
    st.markdown(
        """
        <h1 style='text-align: center; color: #FF0000; font-size: 2.5em; text-shadow: 0 0 5px #33FF33, 0 0 10px #33FF33, 0 0 20px #33FF33;'>
            <img src='https://upload.wikimedia.org/wikipedia/commons/7/7a/Anarchy-symbol.svg' width='50' style='vertical-align: middle;'>TRHACKNON<img src='https://upload.wikimedia.org/wikipedia/commons/7/7a/Anarchy-symbol.svg' width='50' style='vertical-align: middle;'>
        </h1>
        """,
        unsafe_allow_html=True,
    )
    token = st.text_input("🔑 Entrez votre token API Telegram Bot:", type="password", key="token")

    if token:
        bot = Bot(token=token)
        st.success("✅ Votre bot est prêt à être utilisé!")

        recipient_chat_id = st.text_input("📩 Entrez le chat ID du destinataire:")

        message = st.text_area("💬 Entrez un message à envoyer au destinataire:")

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

        st.write("### 📜 Messages envoyés :")
        for msg in st.session_state.sent_messages:
            st.markdown(f"<div class='message-box'>{msg}</div>", unsafe_allow_html=True)

        if st.button("🗑️ Réinitialiser les messages envoyés"):
            reset_messages()
            st.session_state.sent_messages = []
            st.session_state.received_messages = []

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

        st.write("### 📥 Messages reçus :")
        for msg in st.session_state.received_messages:
            st.markdown(f"<div class='message-box'>{msg}</div>", unsafe_allow_html=True)

        if st.button("🗑️ Réinitialiser les messages reçus"):
            reset_messages()
            st.session_state.received_messages = []
            save_messages(received_messages_file, st.session_state.received_messages)
