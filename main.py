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
    usd_value_tinkoff_last = usd_value_cbr_last = 0
    while True:

        if usd_value_tinkoff_last != (value := usd_tinkoff()):
            if value > usd_value_i_buy: 
                for _ in range(10):
                    await message.answer('Should sell USD! {}'.format(value))
            if usd_value_tinkoff_last < value:
                await message.answer(f'🔻🔻🔻\nUSD Tinkoff: {usd_value_tinkoff_last}\n🔻🔻🔻')
            elif usd_value_tinkoff_last > value:
                await message.answer(f'✅✅✅\nUSD Tinkoff: {usd_value_tinkoff_last}\n✅✅✅')
            usd_value_tinkoff_last = value
        if usd_value_cbr_last != (value := usd_cbr()):
            if usd_value_tinkoff_last < value:
                await message.answer(f'🔻🔻🔻\nUSD CBR: {usd_value_cbr_last}\n🔻🔻🔻')
            elif usd_value_tinkoff_last > value:
                await message.answer(f'✅✅✅\nUSD CBR: {usd_value_cbr_last}\n✅✅✅')
            usd_value_cbr_last = value

        await asyncio.sleep(5*60)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)