from aiogram import F
from aiogram.types import CallbackQuery
def register(dp,navigation):
    @dp.callback_query(F.data=='nav:back')
    async def back(c:CallbackQuery): await c.answer(); await navigation.back(c.from_user.id,c.message)
    @dp.callback_query(F.data=='nav:home')
    async def home(c:CallbackQuery): await c.answer(); await navigation.home(c.from_user.id,c.message)
    @dp.callback_query(F.data=='nav:noop')
    async def noop(c:CallbackQuery): await c.answer()
