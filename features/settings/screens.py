from .keyboards import menu_keyboard,action_keyboard

def SETTINGS_MENU_screen():
    return ('⚙️ Settings\\n\\nConfigure NovaBot preferences.',menu_keyboard())

def SETTINGS_LANGUAGE_screen():
    return ('🌐 Language\\n\\nLanguage selector placeholder.',action_keyboard())

def SETTINGS_NOTIFICATIONS_screen():
    return ('🔔 Notifications\\n\\nNotification controls placeholder.',action_keyboard())
