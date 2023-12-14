from aiogram             import types
from aiogram.types       import MediaGroup, InputMediaPhoto
from aiogram_media_group import media_group_handler

from Accest.change          import Change, ChatGPT
from Accest.translation.ttr import ttr
from Accest.translation.etr import etr

from Bot.bot import Bot_


class Unique:
    @media_group_handler
    async def change_media_group(messages: list[types.Message]):
        await Unique.change_media(messages)

    async def change_media(messages: types.Message | list[types.Message]):
        if isinstance(messages, types.Message):
            messages = [messages]
        _message = messages[0]

        await Bot_(_message).answer(ttr.t2)

        caption_ = None
        for message_ in messages:
            if message_.caption is not None:
                caption_ = message_.caption
                break

        _caption = None
        if caption_:
            await Bot_(_message).answer(ttr.t3)

            _caption = ChatGPT.create(caption_)

        if caption_ and not _caption:
            await Bot_(_message).answer(etr.t6)

        await Bot_(_message).answer(ttr.t4)

        downloaded_files = []
        for message_ in messages:
            downloaded_file = await Bot_(message_).custom_download_file()

            if not downloaded_file:
                await Bot_(message_).reply(etr.t1)
                continue

            downloaded_files.append([downloaded_file, message_])

        if not downloaded_files:    
            return await Bot_(_message).answer(etr.t4)

        await Bot_(_message).answer(ttr.t5)

        ioBases: MediaGroup = MediaGroup()
        for i, (downloaded_file, message_) in enumerate(downloaded_files):
            ioBase = Change.photo(downloaded_file)
            
            if not ioBase:
                await Bot_(message_).reply(etr.t2)
                continue

            caption__ = None
            if i == 0:
                caption__ = _caption

            ioBases.attach_photo(InputMediaPhoto(ioBase, caption = caption__))

        if not ioBases:
            return await Bot_(_message).answer(etr.t5)

        msg = await Bot_(_message).answer_media_group(ioBases)
        if not msg:
            return await Bot_(_message).answer(etr.t3)
    
    async def change_text(message: types.Message):
        await Bot_(message).answer(ttr.t3)

        _caption = ChatGPT.create(message.text)
        if _caption is None:
            return await Bot_(message).answer(etr.t6)
        
        await Bot_(message).answer(_caption)