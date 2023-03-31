import logging
from aiogram import executor

from configuration.config import dp

from user_handlers.reg_mes_hand import reg_mes_handlers


reg_mes_handlers(dp)


if __name__ == '__main__':
	logging.basicConfig(level=logging.INFO)
	executor.start_polling(dp, skip_updates=True)
