from aiogram import Bot,Dispatcher,executor,types
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold,hlink,hide_link,link as ai
from main import*
import json
import auth_data


bot=Bot(token="5535738016:AAElQ4qifmYZrMW_fehZkrrRW8LGdiGr8FI",parse_mode=types.ParseMode.HTML)
dsp=Dispatcher(bot=bot)

@dsp.message_handler(commands="start")
async def start(message: types.Message):    
    start_buttons=["Игры","Железо"]
    keyboards=types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboards.add(*start_buttons)
    await message.answer("Товары со скидкой:",reply_markup=keyboards)
   
@dsp.message_handler(Text(equals="Игры"))
async def get_discount_games(message:types.Message):
    await message.answer("Please wait..")
    igromagaz.get_data()

    with open ("igromagaz_discount.json",encoding="UTF-8") as file:
        data=json.load(file)

    for item in data:
        card=f'{hlink(item.get("Название"),item.get("Cсылка"))}\n'\
            f"Цена:{item.get('Цена')}\n"
        await message.answer(card)


def main():
    executor.start_polling(dsp)

if __name__=="__main__":
    main()