from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
from keyboards import all_back_to_main_default
from loader import dp
from utils.screenshoter import take_screenshot


@dp.callback_query_handler(text_startswith="screenshot", state="*")
async def input_screenshot_link(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.answer("<b>Пришли сылку на страницу</b>", reply_markup=all_back_to_main_default)
    await state.set_state("here_input_link")


@dp.message_handler(state="here_input_link")
async def get_screenshot_link(message: Message, state: FSMContext):
    link = message.text
    del_msg = await message.answer(f'Делаю скриншот страницы: {link}')

    status, screenshot_filename = await take_screenshot(link)
    await del_msg.delete()
    if status:
        with open(screenshot_filename, 'rb') as photo:
            await message.answer_photo(photo=photo)
    else:
        await message.answer(f'Ошибка скриншота сайта {link}')
    await state.finish()

