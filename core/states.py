from aiogram.fsm.state import State,StatesGroup
class InputStates(StatesGroup):
    waiting_url=State(); waiting_stars=State()
