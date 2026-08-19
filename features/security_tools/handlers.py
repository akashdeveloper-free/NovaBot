from aiogram import F,Router
from aiogram.types import CallbackQuery
router=Router()
def register(navigation):
    @router.callback_query(F.data=='security:menu')
    async def h_0(c:CallbackQuery): await c.answer(); await navigation.go_to(c.from_user.id,'SECURITY_MENU',source_message=c.message)
    @router.callback_query(F.data=='security:scan')
    async def h_1(c:CallbackQuery): await c.answer(); await navigation.go_to(c.from_user.id,'SECURITY_SCAN',source_message=c.message)
    @router.callback_query(F.data=='security:password')
    async def h_2(c:CallbackQuery): await c.answer(); await navigation.go_to(c.from_user.id,'SECURITY_PASSWORD',source_message=c.message)
