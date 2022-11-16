from aiogram import Bot,Dispatcher,executor,types
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold,hlink,hide_link,link as ai
from main import*
import json
import auth_data
#its version

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

    start_buttons=["Хоррор","Стратегия","Аркады","Детские","Головоломки","Шутеры","Инди",
    "Казуальные","Гонки","ММО","Экшены","Симуляторы","Приключения","Ролевые","Файтинги",
    "Спорт"]
    keyboards=types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboards.add(*start_buttons)

    await message.answer("Chooose genre:",reply_markup=keyboards)
    

   
    

@dsp.message_handler(Text(equals="Стратегия"))
async def get_discount_games_horror(message:types.Message):

    igromagaz.get__data(genre="strategy")

    with open ("igromagaz_discount.json",encoding="UTF-8") as file:
        data=json.load(file)
        
        for item in data:
            card=f'{hlink(item.get("Название"),item.get("Cсылка"))}\n'\
                f"Старая цена:{item.get('Cтарая цена')}\n"\
                f"Новая цена:{item.get('Новая цена')}\n"\
                f"Наличие:{item.get('Наличие')}\n"
            await message.answer(card)

@dsp.message_handler(Text(equals="Хоррор"))
async def get_discount_games_horror(message:types.Message):

    igromagaz.get__data(genre="horror")

    with open ("igromagaz_discount.json",encoding="UTF-8") as file:
        data=json.load(file)
        
        for item in data:
            card=f'{hlink(item.get("Название"),item.get("Cсылка"))}\n'\
                f"Старая цена:{item.get('Cтарая цена')}\n"\
                f"Новая цена:{item.get('Новая цена')}\n"\
                f"Наличие:{item.get('Наличие')}\n"
            await message.answer(card)

@dsp.message_handler(Text(equals="Аркады"))
async def get_discount_games_horror(message:types.Message):

    igromagaz.get__data(genre="arcade")

    with open ("igromagaz_discount.json",encoding="UTF-8") as file:
        data=json.load(file)
        
        for item in data:
            card=f'{hlink(item.get("Название"),item.get("Cсылка"))}\n'\
                f"Старая цена:{item.get('Cтарая цена')}\n"\
                f"Новая цена:{item.get('Новая цена')}\n"\
                f"Наличие:{item.get('Наличие')}\n"
            await message.answer(card)

@dsp.message_handler(Text(equals="Детские"))
async def get_discount_games_horror(message:types.Message):

    igromagaz.get__data(genre="children")

    with open ("igromagaz_discount.json",encoding="UTF-8") as file:
        data=json.load(file)
        
        for item in data:
            card=f'{hlink(item.get("Название"),item.get("Cсылка"))}\n'\
                f"Старая цена:{item.get('Cтарая цена')}\n"\
                f"Новая цена:{item.get('Новая цена')}\n"\
                f"Наличие:{item.get('Наличие')}\n"
            await message.answer(card)

@dsp.message_handler(Text(equals="Головоломки"))
async def get_discount_games_horror(message:types.Message):

    igromagaz.get__data(genre="mindgames")

    with open ("igromagaz_discount.json",encoding="UTF-8") as file:
        data=json.load(file)
        
        for item in data:
            card=f'{hlink(item.get("Название"),item.get("Cсылка"))}\n'\
                f"Старая цена:{item.get('Cтарая цена')}\n"\
                f"Новая цена:{item.get('Новая цена')}\n"\
                f"Наличие:{item.get('Наличие')}\n"
            await message.answer(card)

@dsp.message_handler(Text(equals="Шутеры"))
async def get_discount_games_horror(message:types.Message):

    igromagaz.get__data(genre="shooter")

    with open ("igromagaz_discount.json",encoding="UTF-8") as file:
        data=json.load(file)
        
        for item in data:
            card=f'{hlink(item.get("Название"),item.get("Cсылка"))}\n'\
                f"Старая цена:{item.get('Cтарая цена')}\n"\
                f"Новая цена:{item.get('Новая цена')}\n"\
                f"Наличие:{item.get('Наличие')}\n"
            await message.answer(card)
    
@dsp.message_handler(Text(equals="Инди"))
async def get_discount_games_horror(message:types.Message):

    igromagaz.get__data(genre="indie")

    with open ("igromagaz_discount.json",encoding="UTF-8") as file:
        data=json.load(file)
        
        for item in data:
            card=f'{hlink(item.get("Название"),item.get("Cсылка"))}\n'\
                f"Старая цена:{item.get('Cтарая цена')}\n"\
                f"Новая цена:{item.get('Новая цена')}\n"\
                f"Наличие:{item.get('Наличие')}\n"
            await message.answer(card)

@dsp.message_handler(Text(equals="Казуальные"))
async def get_discount_games_horror(message:types.Message):

    igromagaz.get__data(genre="casual")

    with open ("igromagaz_discount.json",encoding="UTF-8") as file:
        data=json.load(file)
        
        for item in data:
            card=f'{hlink(item.get("Название"),item.get("Cсылка"))}\n'\
                f"Старая цена:{item.get('Cтарая цена')}\n"\
                f"Новая цена:{item.get('Новая цена')}\n"\
                f"Наличие:{item.get('Наличие')}\n"
            await message.answer(card)

@dsp.message_handler(Text(equals="Гонки"))
async def get_discount_games_horror(message:types.Message):

    igromagaz.get__data(genre="race")

    with open ("igromagaz_discount.json",encoding="UTF-8") as file:
        data=json.load(file)
        
        for item in data:
            card=f'{hlink(item.get("Название"),item.get("Cсылка"))}\n'\
                f"Старая цена:{item.get('Cтарая цена')}\n"\
                f"Новая цена:{item.get('Новая цена')}\n"\
                f"Наличие:{item.get('Наличие')}\n"
            await message.answer(card)

@dsp.message_handler(Text(equals="ММО"))
async def get_discount_games_horror(message:types.Message):

    igromagaz.get__data(genre="mmo")

    with open ("igromagaz_discount.json",encoding="UTF-8") as file:
        data=json.load(file)
        
        for item in data:
            card=f'{hlink(item.get("Название"),item.get("Cсылка"))}\n'\
                f"Старая цена:{item.get('Cтарая цена')}\n"\
                f"Новая цена:{item.get('Новая цена')}\n"\
                f"Наличие:{item.get('Наличие')}\n"
            await message.answer(card)

@dsp.message_handler(Text(equals="Экшены"))
async def get_discount_games_horror(message:types.Message):

    igromagaz.get__data(genre="action")

    with open ("igromagaz_discount.json",encoding="UTF-8") as file:
        data=json.load(file)
        
        for item in data:
            card=f'{hlink(item.get("Название"),item.get("Cсылка"))}\n'\
                f"Старая цена:{item.get('Cтарая цена')}\n"\
                f"Новая цена:{item.get('Новая цена')}\n"\
                f"Наличие:{item.get('Наличие')}\n"
            await message.answer(card)

@dsp.message_handler(Text(equals="Симуляторы"))
async def get_discount_games_horror(message:types.Message):

    igromagaz.get__data(genre="simulator")

    with open ("igromagaz_discount.json",encoding="UTF-8") as file:
        data=json.load(file)
        
        for item in data:
            card=f'{hlink(item.get("Название"),item.get("Cсылка"))}\n'\
                f"Старая цена:{item.get('Cтарая цена')}\n"\
                f"Новая цена:{item.get('Новая цена')}\n"\
                f"Наличие:{item.get('Наличие')}\n"
            await message.answer(card)

@dsp.message_handler(Text(equals="Приключения"))
async def get_discount_games_horror(message:types.Message):

    igromagaz.get__data(genre="adventure")

    with open ("igromagaz_discount.json",encoding="UTF-8") as file:
        data=json.load(file)
        
        for item in data:
            card=f'{hlink(item.get("Название"),item.get("Cсылка"))}\n'\
                f"Старая цена:{item.get('Cтарая цена')}\n"\
                f"Новая цена:{item.get('Новая цена')}\n"\
                f"Наличие:{item.get('Наличие')}\n"
            await message.answer(card)

@dsp.message_handler(Text(equals="Ролевые"))
async def get_discount_games_horror(message:types.Message):

    igromagaz.get__data(genre="rpg")

    with open ("igromagaz_discount.json",encoding="UTF-8") as file:
        data=json.load(file)
        
        for item in data:
            card=f'{hlink(item.get("Название"),item.get("Cсылка"))}\n'\
                f"Старая цена:{item.get('Cтарая цена')}\n"\
                f"Новая цена:{item.get('Новая цена')}\n"\
                f"Наличие:{item.get('Наличие')}\n"
            await message.answer(card)

@dsp.message_handler(Text(equals="Файтинги"))
async def get_discount_games_horror(message:types.Message):

    igromagaz.get__data(genre="fighting")

    with open ("igromagaz_discount.json",encoding="UTF-8") as file:
        data=json.load(file)
        
        for item in data:
            card=f'{hlink(item.get("Название"),item.get("Cсылка"))}\n'\
                f"Старая цена:{item.get('Cтарая цена')}\n"\
                f"Новая цена:{item.get('Новая цена')}\n"\
                f"Наличие:{item.get('Наличие')}\n"
            await message.answer(card)

@dsp.message_handler(Text(equals="Спорт"))
async def get_discount_games_horror(message:types.Message):

    igromagaz.get__data(genre="sport")

    with open ("igromagaz_discount.json",encoding="UTF-8") as file:
        data=json.load(file)
        
        for item in data:
            card=f'{hlink(item.get("Название"),item.get("Cсылка"))}\n'\
                f"Старая цена:{item.get('Cтарая цена')}\n"\
                f"Новая цена:{item.get('Новая цена')}\n"\
                f"Наличие:{item.get('Наличие')}\n"
            await message.answer(card)




def main():
    executor.start_polling(dsp)

if __name__=="__main__":
    main()