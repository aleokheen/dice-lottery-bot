from aiogram.dispatcher.filters.state import StatesGroup, State


class StakeState(StatesGroup):
    select = State()

    stake_1_prompt_case = State()
    stake_1_prompt_dice = State()

    stake_2_prompt_dice = State()

    stake_3_prompt_case = State()
    stake_3_prompt_dice = State()
