import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from slack_bolt.adapter.flask import SlackRequestHandler
from slack_bolt import App
from dotenv import find_dotenv, load_dotenv
from flask import Flask, request
from functions import edit_writing, proposal_writer

# Load environment variables from .env file
load_dotenv(find_dotenv())

# Set Slack API credentials
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_SIGNING_SECRET = os.getenv("SLACK_SIGNING_SECRET")
SLACK_BOT_USER_ID = os.getenv("SLACK_BOT_USER_ID")

# Initialize the Slack app
app = App(token=SLACK_BOT_TOKEN)

# Initialize the Flask app
flask_app = Flask(__name__)
handler = SlackRequestHandler(app)

# Dictionary that maps keywords to function handlers
COMMAND_HANDLERS = {
    "edit": edit_writing,
    "draft": proposal_writer,
    "help with a draft": proposal_writer,
    "make up a draft for me": proposal_writer,
    "write a proposal": proposal_writer
}

@app.event("app_mention")
def handle_mentions(body, say):
    """
    Event listener for mentions in Slack.
    When the bot is mentioned, this function processes the text and sends a response.
    """
    text = body["event"]["text"]
    mention = f"<@{SLACK_BOT_USER_ID}>"

    # Split the text by the bot's mention and get the text after it
    parts = text.split(mention)
    if len(parts) > 1:
        text_without_mention = parts[1].strip().lower()
    else:
        # If the mention is not there or not as expected, use the full text
        text_without_mention = text.strip().lower()

    for command, function in COMMAND_HANDLERS.items():
        if text_without_mention.startswith(command):
            command_input = text_without_mention[len(command):].strip()
            # Call the appropriate function with the necessary arguments
            response = function(user_input=command_input, name='YourSlackNameHere')
            say(response)
            return

    say("I'm sorry, I didn't understand that. Try *edit* or *proposal* followed by your message.")

@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    """
    Route for handling Slack events.
    This function passes the incoming HTTP request to the SlackRequestHandler for processing.
    """
    return handler.handle(request)

# Run the Flask app
if __name__ == "__main__":
    flask_app.run()