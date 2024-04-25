import json
import os
import requests
import logging
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

bot_token = os.environ['SLACK_BOT_TOKEN']
channel = os.environ['SLACK_CHANNEL']
client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))
logger = logging.getLogger(__name__)

def post_message_to_slack(text: str, blocks: dict[str, str]):
    message = text
    slack_url = "https://slack.com/api/chat.postMessage"

    try:
        # Call the chat.postMessage method using the WebClient
        result = client.chat_postMessage(
            channel=channel,
            text=text,
            blocks=json.dumps(blocks) if blocks else None
        )
        logger.info(result)

    except SlackApiError as e:
        logger.error(f" Error posting message: {e}")


def post_message_to_slack_with_attachment(text: str, blocks: dict[str, str]):
    message = text
    slack_url = "https://slack.com/api/chat.postMessage"
    attachment = [].json()
    try:
        # Call the chat.postMessage method using the WebClient
        result = client.chat_postMessage(
            channel=channel,
            text=text,
            attachments=attachment,
            blocks=json.dumps(blocks) if blocks else None
        )
        logger.info(result)

    except SlackApiError as e:
        logger.error(f" Error posting message: {e}")
