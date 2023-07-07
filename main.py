from aiogram import Bot, Dispatcher, executor, types
from aiogram import types
from usd import usd
import asyncio

bot = Bot(token="6149143790:AAEUfwLGmw7Nv9nARmBvyyhdx5KKBtcfMuI")
dp = Dispatcher(bot)
admin_chat_id = 879165748

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Starting...')
    usd_value = 92.57
    usd_value_new = usd()
    await message.answer('USD: {}'.format(usd_value_new))   
    while True:
        usd_value_new = usd()
        if usd_value_new <= 90:
            for _ in range(10):
                await message.answer('Low USD price! USD: {}'.format(usd_value_new))
        elif usd_value_new >= 100:
            for _ in range(10):
                await message.answer('High USD price! USD: {}'.format(usd_value_new))
        else:
            if usd_value_new > usd_value:
                await message.answer('Usd value is higher than the previous one. Up to {} USD'.format(usd_value_new))
            elif usd_value_new < usd_value:
                await message.answer('Usd value is lower than the previous one. Down to {} USD'.format(usd_value_new))  
            usd_value = usd_value_new   
            await asyncio.sleep(60*30)  




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)