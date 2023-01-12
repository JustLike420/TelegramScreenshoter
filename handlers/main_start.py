from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from keyboards import main_menu_inl
from loader import dp


@dp.message_handler(text=['⬅ На главную', '/start'], state="*")
async def start(message: Message, state: FSMContext):
    await state.finish()
    await message.answer(f"🤘 Салют, {message.chat.username}!\n",
                         reply_markup=main_menu_inl)
