import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, filters

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Define a command handler for '/start'
def start(update, context):
    update.message.reply_text('Hello! This is your bot.')

# Define a message handler
def echo(update, context):
    update.message.reply_text(update.message.text)

def main():
    # Replace 'YOUR_BOT_TOKEN_HERE' with your actual bot token
    token = 'YOUR_BOT_TOKEN_HERE'

    # Create the Updater and pass it your bot's token.
    updater = Updater(token, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add a command handler for '/start'
    dispatcher.add_handler(CommandHandler("start", start))

    # Add a message handler
    dispatcher.add_handler(MessageHandler(filters.text & ~filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
