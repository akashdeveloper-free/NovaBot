from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
def nav(back=True,home=True):
    row=[]
    if back:row.append(InlineKeyboardButton(text='⬅️ Back',callback_data='nav:back'))
    if home:row.append(InlineKeyboardButton(text='🏠 Main Menu',callback_data='nav:home'))
    return InlineKeyboardMarkup(inline_keyboard=[row] if row else [])
