import logic
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

FILE_NAME = 'Kruzok.mp4'
BOT_API = '7524906492:AAF9xsRGtv3rDX3BjMyR3iXmyya5meWZewE'

bot = Bot(BOT_API)
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f'Отпрвьте сюда кружок, чтоб узнать дату его записи')


@dp.message()
async def video_handler(message: Message):
    if message.content_type == 'video_note':
        info = await bot.get_file(message.video_note.file_id)
        file_path = info.file_path
        await bot.download_file(file_path, FILE_NAME)
        date = logic.get_metadata_pymediainfo(FILE_NAME)
        await message.answer(f'Зписан сегодня? {logic.is_equal_to_today(date)}\n'
                             f'Дата: {date}')


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())