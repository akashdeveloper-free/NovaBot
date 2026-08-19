from aiogram import F,Router
from aiogram.types import CallbackQuery
router=Router()
def register(navigation):
    @router.callback_query(F.data=='help:menu')
    async def h_0(c:CallbackQuery): await c.answer(); await navigation.go_to(c.from_user.id,'HELP_MENU',source_message=c.message)
    @router.callback_query(F.data=='help:faq')
    async def h_1(c:CallbackQuery): await c.answer(); await navigation.go_to(c.from_user.id,'HELP_FAQ',source_message=c.message)
    @router.callback_query(F.data=='help:about')
    async def h_2(c:CallbackQuery): await c.answer(); await navigation.go_to(c.from_user.id,'HELP_ABOUT',source_message=c.message)
