import config
from modules.vkbot import VkBot
from modules.database import Database
from modules.dispatcher import Dispatcher


bot = VkBot(token=config.API_TOKEN, message_delay=config.MESSAGE_DELAY, message_front=config.MESSAGE_FRONT,
			reply_message=config.REPLY_MESSAGE, ignore_chats=config.IGNORE_CHATS, ignore_users=config.IGNORE_USERS)
dp = Dispatcher(bot, admins=config.ADMINS)
database = Database(**config.DATABASE)