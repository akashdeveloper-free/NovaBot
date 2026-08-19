import asyncio,logging
from aiogram import Bot,Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config.settings import settings
from database.repositories import UIStateRepository
from core.master_message import MasterMessageManager
from core.navigation import NavigationEngine
from core.start_handler import register as register_start
from core.navigation_handlers import register as register_nav
from ui.screens.main_menu import main_menu_screen
from features.video_downloader.screens import register as register_video_screens
from features.video_downloader.handlers import register as register_video_handlers
from features.video_downloader.router import router as video_router
from features.donate_stars.screens import DONATE_MENU_screen,DONATE_CUSTOM_screen
from features.donate_stars.router import router as donate_router
from features.file_tools.screens import FILE_MENU_screen,FILE_CONVERT_screen,FILE_COMPRESS_screen
from features.file_tools.router import router as file_router
from features.security_tools.screens import SECURITY_MENU_screen,SECURITY_SCAN_screen,SECURITY_PASSWORD_screen
from features.security_tools.router import router as security_router
from features.settings.screens import SETTINGS_MENU_screen,SETTINGS_LANGUAGE_screen,SETTINGS_NOTIFICATIONS_screen
from features.settings.router import router as settings_router
from features.help.screens import HELP_MENU_screen,HELP_FAQ_screen,HELP_ABOUT_screen
from features.help.router import router as help_router
logging.basicConfig(level=getattr(logging,settings.LOG_LEVEL.upper(),logging.INFO))
async def main():
    bot=Bot(settings.BOT_TOKEN,default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN)); dp=Dispatcher(); repo=UIStateRepository(settings.DB_PATH); await repo.init_db(); master=MasterMessageManager(bot,repo); nav=NavigationEngine(master,repo)
    nav.register('MAIN_MENU',main_menu_screen); register_video_screens(nav)
    for n,fn in [('DONATE_MENU',DONATE_MENU_screen),('DONATE_CUSTOM',DONATE_CUSTOM_screen),('FILE_MENU',FILE_MENU_screen),('FILE_CONVERT',FILE_CONVERT_screen),('FILE_COMPRESS',FILE_COMPRESS_screen),('SECURITY_MENU',SECURITY_MENU_screen),('SECURITY_SCAN',SECURITY_SCAN_screen),('SECURITY_PASSWORD',SECURITY_PASSWORD_screen),('SETTINGS_MENU',SETTINGS_MENU_screen),('SETTINGS_LANGUAGE',SETTINGS_LANGUAGE_screen),('SETTINGS_NOTIFICATIONS',SETTINGS_NOTIFICATIONS_screen),('HELP_MENU',HELP_MENU_screen),('HELP_FAQ',HELP_FAQ_screen),('HELP_ABOUT',HELP_ABOUT_screen)]: nav.register(n,fn)
    register_video_handlers(nav)
    # Other feature routers register their callbacks through their own module functions.
    from features.donate_stars.handlers import register as rd; from features.file_tools.handlers import register as rf; from features.security_tools.handlers import register as rs; from features.settings.handlers import register as rt; from features.help.handlers import register as rh
    rd(nav); rf(nav); rs(nav); rt(nav); rh(nav)
    register_start(dp,master,nav); register_nav(dp,nav)
    dp.include_router(video_router); dp.include_router(donate_router); dp.include_router(file_router); dp.include_router(security_router); dp.include_router(settings_router); dp.include_router(help_router)
    logging.info('NovaBot Master started'); await dp.start_polling(bot)
if __name__=='__main__': asyncio.run(main())
