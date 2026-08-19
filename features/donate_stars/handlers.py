from aiogram import F,Router
from aiogram.types import CallbackQuery
router=Router()
def register(navigation):
    @router.callback_query(F.data=='donate:menu')
    async def h_0(c:CallbackQuery): await c.answer(); await navigation.go_to(c.from_user.id,'DONATE_MENU',source_message=c.message)
    @router.callback_query(F.data=='donate:custom')
    async def h_1(c:CallbackQuery): await c.answer(); await navigation.go_to(c.from_user.id,'DONATE_CUSTOM',source_message=c.message)
