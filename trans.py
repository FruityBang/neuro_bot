import asyncio
from deep_translator import GoogleTranslator


async def make_tatar_wisdom(joke: str) -> str:
    translator_yi = GoogleTranslator(source='ru', target='yi')
    translator_tt = GoogleTranslator(source='yi', target='tt')
    translator_ru = GoogleTranslator(source='tt', target='ru')
    quarter_wisdom = translator_yi.translate(joke)
    half_wisdom = translator_tt.translate(quarter_wisdom)
    pure_wisdom = translator_ru.translate(half_wisdom)
    await asyncio.sleep(1)
    return pure_wisdom
