import typing

from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class ChatIdFilter(BoundFilter):
    key = 'chat_id'

    def __init__(self, chat_id: typing.Union[typing.Iterable, int]):
        if isinstance(chat_id, int):
            chat_id = [chat_id]
        self.chat_id = chat_id

    def check(self, message: types.Message) -> bool:
        return message.chat.id in self.chat_id
