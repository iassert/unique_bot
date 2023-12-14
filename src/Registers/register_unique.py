from aiogram                    import types
from aiogram.dispatcher.filters import MediaGroupFilter

from Bot.bot import Bot_

from Handlers.unique import Unique

Bot_.dp.register_message_handler(
    Unique.change_media_group,
    MediaGroupFilter(is_media_group = True),
    content_types = types.ContentTypes.PHOTO + types.ContentTypes.VIDEO,
)
Bot_.dp.register_message_handler(
    Unique.change_media,
    content_types = types.ContentTypes.PHOTO + types.ContentTypes.VIDEO,
)
Bot_.dp.register_message_handler(
    Unique.change_text,
    content_types = types.ContentTypes.TEXT,
)