from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove
from aiogram.types.contact import Contact
from keyboards.start import make_keyboard
from keyboards.get_phone import get_phone

router = Router()

class Registration(StatesGroup):
    first = State()

@router.message(Command("start"))
async def cmd_start(message):
    await message.answer("Добро пожаловать! Это бот кошелек. Здесь вы можете вести учет ваших доходов и расходов. Для начала работы бота нажмите кнопку Регистрация или наберите с клавиатуры комманду /reg ", reply_markup=make_keyboard(['Регистрация',]))

@router.message(StateFilter(None), F.text == 'Регистрация')
@router.message(StateFilter(None), Command(commands=['reg']))
async def cmd_reg(message, state):
    await state.set_state(Registration.first)
    await message.answer('Нажмите на кнопку ниже, что бы поделиться контактной информацией', reply_markup = await get_phone(['Поделиться контактом',]))
    

@router.message(Registration.first, F.contact)
async def reg_second(message, state):
    contact = message.contact
    await state.update_data(user_contact = contact.phone_number)
    await state.update_data(user_id = contact.user_id)
    await state.update_data(user_fullname = message.from_user.full_name)
    user_data = await state.get_data()
    await message.answer(f'Спасибо за регистрацию.\nВаш номер {user_data['user_contact']}')

    
