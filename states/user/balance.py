from aiogram.dispatcher.filters.state import StatesGroup, State


class BalanceState(StatesGroup):
    show = State()

    confirm_for_refill = State()
    pending_for_refill = State()

    set_amount_for_withdraw = State()
    set_comment_for_withdraw = State()
