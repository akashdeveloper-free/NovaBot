from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
def main_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
      [InlineKeyboardButton(text='🎬 Video Downloader',callback_data='video:menu')],
      [InlineKeyboardButton(text='⭐ Donate Stars',callback_data='donate:menu')],
      [InlineKeyboardButton(text='📁 File Tools',callback_data='files:menu'),InlineKeyboardButton(text='🛡️ Security Tools',callback_data='security:menu')],
      [InlineKeyboardButton(text='⚙️ Settings',callback_data='settings:menu'),InlineKeyboardButton(text='❓ Help',callback_data='help:menu')]])
