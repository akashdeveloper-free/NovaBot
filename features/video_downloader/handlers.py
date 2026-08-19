from aiogram import F,Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery,Message
from core.states import InputStates
from .service import DownloaderService
router=Router(); service=DownloaderService()
def register(navigation):
    @router.callback_query(F.data=='video:menu')
    async def menu(c:CallbackQuery): await c.answer(); await navigation.go_to(c.from_user.id,'VIDEO_MENU',source_message=c.message)
    for platform,state in [('tiktok',InputStates.waiting_url),('youtube',InputStates.waiting_url),('facebook',InputStates.waiting_url),('instagram',InputStates.waiting_url)]:
        @router.callback_query(F.data==f'video:{platform}')
        async def open_platform(c:CallbackQuery,platform=platform): await c.answer(); await navigation.go_to(c.from_user.id,'VIDEO_'+platform.upper(),source_message=c.message)
        @router.callback_query(F.data==f'video:input:{platform}')
        async def input_url(c:CallbackQuery,state_ctx:FSMContext,platform=platform): await c.answer('Send the URL in chat.'); await state_ctx.update_data(platform=platform); await state_ctx.set_state(state)
    @router.message(InputStates.waiting_url)
    async def receive(message:Message,state:FSMContext):
        data=await state.get_data(); p=data.get('platform','tiktok'); url=(message.text or '').strip()
        if not url:
            await navigation.go_to(message.from_user.id,'VIDEO_'+p.upper()); return
        await navigation.replace_screen(message.from_user.id,'VIDEO_PROCESSING',platform_name=p)
        r=await service.inspect_url(p,url); await state.clear()
        await navigation.replace_screen(message.from_user.id,'VIDEO_RESULT',platform_name=p,title=r['title'])
    @router.callback_query(F.data.startswith('video:mock:'))
    async def mock(c:CallbackQuery): await c.answer('Backend/download service is not connected yet.',show_alert=True)
