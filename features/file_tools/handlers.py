from aiogram import F,Router
from aiogram.types import CallbackQuery
router=Router()
def register(navigation):
    @router.callback_query(F.data=='files:menu')
    async def h_0(c:CallbackQuery): await c.answer(); await navigation.go_to(c.from_user.id,'FILE_MENU',source_message=c.message)
    @router.callback_query(F.data=='files:convert')
    async def h_1(c:CallbackQuery): await c.answer(); await navigation.go_to(c.from_user.id,'FILE_CONVERT',source_message=c.message)
    @router.callback_query(F.data=='files:compress')
    async def h_2(c:CallbackQuery): await c.answer(); await navigation.go_to(c.from_user.id,'FILE_COMPRESS',source_message=c.message)
