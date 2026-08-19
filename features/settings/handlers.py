from aiogram import F,Router
from aiogram.types import CallbackQuery
router=Router()
def register(navigation):
    @router.callback_query(F.data=='settings:menu')
    async def h_0(c:CallbackQuery): await c.answer(); await navigation.go_to(c.from_user.id,'SETTINGS_MENU',source_message=c.message)
    @router.callback_query(F.data=='settings:language')
    async def h_1(c:CallbackQuery): await c.answer(); await navigation.go_to(c.from_user.id,'SETTINGS_LANGUAGE',source_message=c.message)
    @router.callback_query(F.data=='settings:notifications')
    async def h_2(c:CallbackQuery): await c.answer(); await navigation.go_to(c.from_user.id,'SETTINGS_NOTIFICATIONS',source_message=c.message)
