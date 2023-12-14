import openai
import random

from PIL import Image, ImageDraw, ImageEnhance

from .translation.atr import atr

from config import Config

from Log.log import Log

from io      import BytesIO
from pathlib import Path


class Change:
    __log = Log("change")

    @staticmethod
    def photo(fp: str | bytes | Path ) -> BytesIO:
        try:
            return Change.__photo(fp)
        except Exception as ex:
            Change.__log.error(ex)

    @staticmethod
    def __photo(fp: str | bytes | Path ) -> BytesIO:
        try:
            image = Image.open(fp)
        except Exception as ex:
            Change.__log.error(ex)
            return

        # Изменение контрастности
        contrast = ImageEnhance.Contrast(image)
        enhanced_image = contrast.enhance(random.uniform(0.9, 1.1))

        # Изменение резкости
        sharpness = ImageEnhance.Sharpness(enhanced_image)
        sharpened_image = sharpness.enhance(random.uniform(0.9, 1.1))

        # Изменение насыщенности
        saturation = ImageEnhance.Color(sharpened_image)
        final_image = saturation.enhance(random.uniform(0.9, 1.1))

        # рисуем линии
        width, height = image.size
        transparent_shape = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(transparent_shape)
        
        for _ in range(random.randint(20, 30)):
            x1, y1 = random.randint(0, width), random.randint(0, height)
            x2, y2 = random.randint(0, width), random.randint(0, height)
            
            draw.line([(x1, y1), (x2, y2)], fill = (255, 255, 255, 10))

        # объединяем
        result = Image.alpha_composite(final_image.convert('RGBA'), transparent_shape)

        image_stream = BytesIO()
        result.save(image_stream, format = 'PNG')
        image_stream.seek(0)

        return image_stream
    

class ChatGPT:
    __log = Log("gpt")
    __messages = [
        {
            "role": "system", 
            "content": atr.t1
        }
    ]
            
    openai.api_key = Config.API_KEY
    limit = 940

    @staticmethod
    def create(text: str | None) -> str:
        if not text:
            return

        out = ""
        for i in [
            text[i:i + ChatGPT.limit] 
            for i in range(0, len(text), ChatGPT.limit)
        ]:
            ChatGPT.__messages.append(
                {
                    "role": "user", 
                    "content": i
                }
            )

            try:
                request = openai.ChatCompletion.create(
                    model = "gpt-3.5-turbo-1106",
                    messages = ChatGPT.__messages,
                    max_tokens = ChatGPT.limit // 2,
                    temperature = 1
                )

                msg = request.choices[-1].message["content"]

                ChatGPT.__messages.append(
                    {
                        "role": "assistant", 
                        "content": msg
                    }
                )

                out += msg
            except Exception as ex:
                ChatGPT.__log.error(ex)

        return out
