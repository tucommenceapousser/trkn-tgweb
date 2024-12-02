import streamlit as st
from telegram import Bot
from telegram.error import TelegramError
import datetime
import time

# Configuration de la mise en page avec un style plus attrayant
st.markdown("""
    <style>
    .main {
        background-color: #121212;  /* Arrière-plan sombre */
        color: #ffffff;              /* Texte en blanc */
        font-family: 'Arial', sans-serif;
    }
    .button {
        background-color: #ff4081; /* Couleur fluo pour les boutons */
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
    }
    h1 {
        color: #ff4081; /* Titre flashy */
    }
    </style>
""", unsafe_allow_html=True)

# Demander le token du bot à l'utilisateur
token = st.text_input("Entrez votre token API Telegram Bot:", type="password")

if token:
    bot = Bot(token=token)
    st.write("Votre bot est prêt à être utilisé!")

    # Zone pour entrer le chat ID du destinataire
    recipient_chat_id = st.text_input("Entrez le chat ID du destinataire:")

    # Zone pour entrer un message
    message = st.text_input("Entrez un message à envoyer au destinataire:")

    # Initialiser l'horodatage de réinitialisation
    if 'reset_time' not in st.session_state:
        st.session_state.reset_time = datetime.datetime.now(datetime.timezone.utc)

    # Initialiser les messages si ce n'est pas déjà fait
    if 'messages_received' not in st.session_state:
        st.session_state.messages_received = []
    if 'messages_sent' not in st.session_state:
        st.session_state.messages_sent = []

    # Fonction pour récupérer les mises à jour
    def get_updates():
        updates = bot.get_updates()
        for update in updates:
            if update.message and update.message.chat:
                message_date = update.message.date.replace(tzinfo=datetime.timezone.utc)
                if message_date >= st.session_state.reset_time:
                    message_text = f"Message de {update.message.chat.id}: {update.message.text}"
                    st.session_state.messages_received.append(message_text)

    # Récupérer les messages à chaque recharge
    get_updates()

    # Bouton pour envoyer le message
    if st.button("Envoyer le message"):
        if recipient_chat_id and message:
            try:
                bot.send_message(chat_id=recipient_chat_id, text=message)
                st.success("Message envoyé avec succès!")
                st.session_state.messages_sent.append(f"Message envoyé à {recipient_chat_id}: {message}")
                get_updates()  # Récupérer les mises à jour après l'envoi
            except TelegramError as e:
                st.error(f"Erreur lors de l'envoi du message: {e}")
        else:
            st.warning("Veuillez entrer un chat ID et un message.")

    # Bouton pour réinitialiser tous les messages
    if st.button("Réinitialiser tous les messages"):
        st.session_state.messages_received.clear()
        st.session_state.messages_sent.clear()
        st.session_state.reset_time = datetime.datetime.now(datetime.timezone.utc)
        st.success("Tous les messages ont été réinitialisés.")

    # Afficher tous les messages reçus
    if st.session_state.messages_received:
        st.write("Messages reçus:")
        for msg in st.session_state.messages_received:
            st.write(msg)
    else:
        st.write("Aucun message reçu.")

    # Afficher tous les messages envoyés
    if st.session_state.messages_sent:
        st.write("Messages envoyés:")
        for msg in st.session_state.messages_sent:
            st.write(msg)
    else:
        st.write("Aucun message envoyé.")

    st.write("Après avoir envoyé un message à votre bot, veuillez entrer votre chat ID ci-dessus pour continuer.")

    # Bouton pour rafraîchir manuellement
    if st.button("Rafraîchir les messages"):
        time.sleep(1)  # Pause pour éviter les requêtes trop rapides
        get_updates()  # Récupérer les mises à jour manuellement

else:
    st.warning("Veuillez d'abord entrer votre token API.")