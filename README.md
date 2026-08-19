# NovaBot Master — Single Master Message UI

UI-only implementation of the requested architecture. One persistent Master Message acts as the bot's mini-app dashboard.

## Rules
- Navigation edits the existing Master Message; no bot navigation messages are sent.
- No ReplyKeyboardMarkup anywhere.
- Persistent SQLite state stores user_id, chat_id, master_message_id, current_screen, navigation_stack.
- First /start may create the Master Message; later /start edits/restores it.
- User URL/amount messages are user-authored input; the bot edits the Master Message instead of answering with a new menu message.
- UI, handlers, routers, keyboards and services are separated.
- Real APIs/download/payment backends are intentionally not implemented yet.

## Run
1. `pip install -r requirements.txt`
2. Copy `.env.example` to `.env` and set BOT_TOKEN.
3. `python main.py`
