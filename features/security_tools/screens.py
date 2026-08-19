from .keyboards import menu_keyboard,action_keyboard

def SECURITY_MENU_screen():
    return ('🛡️ Security Tools\\n\\nAuthorized security utilities will be added later.',menu_keyboard())

def SECURITY_SCAN_screen():
    return ('🔎 Security Scan\\n\\nUI placeholder; no external scan is executed.',action_keyboard())

def SECURITY_PASSWORD_screen():
    return ('🔐 Password Tools\\n\\nUI placeholder for safe password-strength utilities.',action_keyboard())
