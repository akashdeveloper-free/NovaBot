from aiogram.filters import CommandStart
from aiogram.types import Message
from ui.screens.main_menu import main_menu_screen
def register(dp,master,navigation):
    @dp.message(CommandStart())
    async def start(message:Message):
        uid=message.from_user.id; text,markup=main_menu_screen(); state=await master.repo.get_state(uid)
        if state:
            if await master.edit(uid,text,markup):
                await navigation.home(uid); return
        await master.create(uid,message.chat.id,text,markup)
