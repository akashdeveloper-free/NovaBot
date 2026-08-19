from .keyboards import menu_keyboard,action_keyboard

def DONATE_MENU_screen():
    return ('⭐ Donate Stars\\n\\nSupport NovaBot with Telegram Stars. Payment backend later.',menu_keyboard())

def DONATE_CUSTOM_screen():
    return ('💫 Custom Stars\\n\\nSend a whole-number amount. Payment is mock in this phase.',action_keyboard())
