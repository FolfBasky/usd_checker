from aiogram import Bot, Dispatcher, executor, types
from aiogram import types
from usd import usd_cbr, usd_tinkoff
import asyncio
import time

bot = Bot(token="6149143790:AAEUfwLGmw7Nv9nARmBvyyhdx5KKBtcfMuI")
dp = Dispatcher(bot)
admin_chat_id = 879165748

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Starting...')
    usd_value_i_buy = 92.57
    usd_value_new_tinkoff = usd_tinkoff()
    await message.answer('USD: {}'.format(usd_value_new_tinkoff))   
    cday = time.time()
    usd_value_tinkoff_lasts = usd_value_cbr_lasts = 0
    while True:
        if (time.time() - cday) % (60*60*24):
            if usd_value_cbr_lasts != (usd_value_cbr_new := usd_cbr()):
                await message.answer('#'*20) 
                await message.answer(f'CBR: {usd_value_cbr_new}')
                await message.answer('#'*20) 
        usd_value_new_tinkoff = usd_tinkoff()
        if usd_value_new_tinkoff <= round(usd_value_i_buy,-1)-10:
            for _ in range(10):
                await message.answer('Low USD price! USD: {}'.format(usd_value_new_tinkoff))
        elif usd_value_new_tinkoff >= round(usd_value_i_buy,-1)+10:
            for _ in range(10):
                await message.answer('High USD price! USD: {}'.format(usd_value_new_tinkoff))
        else:
            if not usd_value_tinkoff_lasts: usd_value_tinkoff_last = usd_value_new_tinkoff 
            if usd_value_new_tinkoff > usd_value_tinkoff_last:
                await message.answer('Usd value is higher than the previous one. Up to {} USD'.format(usd_value_new_tinkoff))
            elif usd_value_new_tinkoff < usd_value_tinkoff_last:
                await message.answer('Usd value is lower than the previous one. Down to {} USD'.format(usd_value_new_tinkoff))  
            usd_value_tinkoff_last = usd_value_new_tinkoff   
            await asyncio.sleep(60*30)  




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)