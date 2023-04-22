# FastAPI LINE Messaging API Webhook

This project is a FastAPI webhook for the LINE Messaging API. It demonstrates how to set up a webhook to receive messages and events from the LINE platform and respond to users.

## Getting Started

1. Clone the repository.
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Set up your LINE Channel by following the instructions [here](https://developers.line.biz/en/docs/messaging-api/getting-started/).
4. Add your `LINE_CHANNEL_SECRET` and `LINE_CHANNEL_ACCESS_TOKEN` to the `.env` file.
5. Run the FastAPI application using uvicorn:
    ```bash
    uvicorn main:app --reload
    ```

6. Expose your local server to the internet using a tool like ngrok.
    ```bash
    ngrok http 8000
    ```

7. Set your webhook URL in the LINE Developers Console to the HTTPS URL provided by ngrok, followed by `/webhook`. For example: `https://your_ngrok_url/webhook`

## Usage

This webhook is set up to handle text messages. When a user sends a text message to your LINE bot, the webhook will reply with "You said: [text]".

Feel free to customize the `app/handlers/message_handler.py` file to create your own message handling logic.