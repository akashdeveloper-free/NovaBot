from typing import Callable,Optional
from aiogram.types import Message
from core.master_message import MasterMessageManager
from database.repositories import UIStateRepository
class NavigationEngine:
    def __init__(self,master,repo): self.master=master; self.repo=repo; self.screens={}
    def register(self,name,renderer): self.screens[name]=renderer
    async def get_current_screen(self,user_id):
        state=await self.repo.get_state(user_id)
        return state.current_screen if state else None
    async def restore_state(self,user_id):
        return await self.repo.get_state(user_id)
    def render(self,name,**kw): return self.screens[name](**kw)
    async def go_to(self,user_id,screen,source_message:Optional[Message]=None,push=True,**kw):
        s=await self.repo.get_state(user_id)
        if not s:return False
        text,markup=self.render(screen,**kw)
        if push and (not s.navigation_stack or s.navigation_stack[-1]!=screen): s.navigation_stack.append(screen)
        elif not push: s.navigation_stack[-1:]=[screen]
        s.current_screen=screen
        ok=await self.master.edit(user_id,text,markup,source_message)
        if ok: await self.repo.save_state(s)
        return ok
    async def back(self,user_id,source_message=None):
        s=await self.repo.get_state(user_id)
        if not s:return False
        if len(s.navigation_stack)>1:s.navigation_stack.pop()
        return await self._set_existing(user_id,s,s.navigation_stack[-1],source_message)
    async def home(self,user_id,source_message=None):
        s=await self.repo.get_state(user_id)
        if not s:return False
        s.navigation_stack=['MAIN_MENU']; return await self._set_existing(user_id,s,'MAIN_MENU',source_message)
    async def _set_existing(self,user_id,s,screen,source_message):
        s.current_screen=screen; text,markup=self.render(screen); ok=await self.master.edit(user_id,text,markup,source_message)
        if ok: await self.repo.save_state(s)
        return ok

    async def replace_screen(self,user_id,screen,source_message=None,**kw):
        return await self.go_to(user_id,screen,source_message=source_message,push=False,**kw)
