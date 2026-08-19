from pathlib import Path
from typing import Optional
import aiosqlite
from database.models import UserUIState
class UIStateRepository:
    def __init__(self,db_path): self.db_path=db_path; Path(db_path).parent.mkdir(parents=True,exist_ok=True)
    async def init_db(self):
        async with aiosqlite.connect(self.db_path,timeout=15) as db:
            await db.execute('PRAGMA journal_mode=WAL'); await db.execute('PRAGMA busy_timeout=15000')
            await db.execute("CREATE TABLE IF NOT EXISTS user_ui_state (user_id INTEGER PRIMARY KEY,chat_id INTEGER NOT NULL,master_message_id INTEGER NOT NULL,current_screen TEXT NOT NULL,navigation_stack TEXT NOT NULL,updated_at TEXT DEFAULT CURRENT_TIMESTAMP)")
            await db.commit()
    async def get_state(self,user_id)->Optional[UserUIState]:
        async with aiosqlite.connect(self.db_path,timeout=15) as db:
            cur=await db.execute('SELECT user_id,chat_id,master_message_id,current_screen,navigation_stack,updated_at FROM user_ui_state WHERE user_id=?',(user_id,)); row=await cur.fetchone(); await cur.close()
        if not row:return None
        return UserUIState(row[0],row[1],row[2],row[3],UserUIState.stack_from_json(row[4]),row[5])
    async def save_state(self,s):
        async with aiosqlite.connect(self.db_path,timeout=15) as db:
            await db.execute("INSERT INTO user_ui_state(user_id,chat_id,master_message_id,current_screen,navigation_stack,updated_at) VALUES(?,?,?,?,?,CURRENT_TIMESTAMP) ON CONFLICT(user_id) DO UPDATE SET chat_id=excluded.chat_id,master_message_id=excluded.master_message_id,current_screen=excluded.current_screen,navigation_stack=excluded.navigation_stack,updated_at=CURRENT_TIMESTAMP",(s.user_id,s.chat_id,s.master_message_id,s.current_screen,s.stack_to_json())); await db.commit()
