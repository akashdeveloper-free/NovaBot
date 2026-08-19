import logging
from typing import Optional
from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import InlineKeyboardMarkup, Message
from database.repositories import UIStateRepository
from database.models import UserUIState
log=logging.getLogger(__name__)
class MasterMessageManager:
    def __init__(self,bot:Bot,repo:UIStateRepository): self.bot=bot; self.repo=repo
    async def create(self,user_id,chat_id,text,markup):
        sent=await self.bot.send_message(chat_id=chat_id,text=text,reply_markup=markup)
        s=UserUIState(user_id,chat_id,sent.message_id,'MAIN_MENU',['MAIN_MENU']); await self.repo.save_state(s); return s
    async def edit(self,user_id,text,markup,source_message:Optional[Message]=None):
        s=await self.repo.get_state(user_id)
        if not s:return False
        try:
            if source_message and source_message.chat.id==s.chat_id and source_message.message_id==s.master_message_id:
                await source_message.edit_text(text=text,reply_markup=markup)
            else:
                await self.bot.edit_message_text(chat_id=s.chat_id,message_id=s.master_message_id,text=text,reply_markup=markup)
            return True
        except TelegramBadRequest as e:
            if 'message is not modified' in str(e).lower(): return True
            log.warning('Master message edit failed for %s: %s',user_id,e); return False
