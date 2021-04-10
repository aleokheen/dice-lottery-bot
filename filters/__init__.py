from loader import dp
from .chat_id import ChatIdFilter


if __name__ == "filters":
    dp.filters_factory.bind(ChatIdFilter)
    pass
