from .keyboards import menu_keyboard,action_keyboard

def FILE_MENU_screen():
    return ('📁 File Tools\\n\\nChoose a file utility.',menu_keyboard())

def FILE_CONVERT_screen():
    return ('🔄 Convert File\\n\\nUI placeholder for file conversion.',action_keyboard())

def FILE_COMPRESS_screen():
    return ('🗜️ Compress File\\n\\nUI placeholder for compression.',action_keyboard())
