from .keyboards import menu_keyboard,action_keyboard

def HELP_MENU_screen():
    return ('❓ Help & Support\\n\\nEverything stays inside one Master Message.',menu_keyboard())

def HELP_FAQ_screen():
    return ('📖 FAQ\\n\\nNavigation edits the Master Message; no Reply Keyboard is used.',action_keyboard())

def HELP_ABOUT_screen():
    return ('ℹ️ About NovaBot\\n\\nModular single-message mini-app architecture.',action_keyboard())
