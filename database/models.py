from dataclasses import dataclass, field
import json
from typing import List, Optional
@dataclass
class UserUIState:
    user_id:int; chat_id:int; master_message_id:int; current_screen:str
    navigation_stack:List[str]=field(default_factory=lambda:['MAIN_MENU'])
    updated_at:Optional[str]=None
    def stack_to_json(self): return json.dumps(self.navigation_stack,separators=(',',':'))
    @staticmethod
    def stack_from_json(raw):
        try:
            v=json.loads(raw)
            return [str(x) for x in v] if isinstance(v,list) and v else ['MAIN_MENU']
        except Exception: return ['MAIN_MENU']
