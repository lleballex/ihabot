from time import sleep

from vk_api import VkApi
from vk_api.utils import get_random_id
from vk_api.longpoll import VkLongPoll, VkEventType


class VkBot:
	def __init__(self, token, message_delay=0, message_front='', reply_message=False, ignore_chats=[], ignore_users=[]):
		self.vk_session = VkApi(token=token)
		self.vk = self.vk_session.get_api()
		self.longpoll = VkLongPoll(self.vk_session)

		self.message_delay = message_delay
		self.message_front = message_front
		self.reply_message = reply_message
		self.ignore_chats = ignore_chats
		self.ignore_users = ignore_users

	def is_chat_new_message(self, event):
		if event.type == VkEventType.MESSAGE_NEW and event.from_chat and not event.chat_id in self.ignore_chats and not event.user_id in self.ignore_users and not event.from_me:
			return True
		return False

	def is_personal_new_message(self, event):
		if event.type == VkEventType.MESSAGE_NEW and event.from_user and not event.user_id in self.ignore_users and not event.from_me:
			return True
		return False

	def send_message(self, peer_id, message, reply_to=None):
		#self.vk.messages.setActivity(peer_id=peer_id, type='typing')
		sleep(self.message_delay)
		self.vk.messages.send(peer_id=peer_id, random_id=get_random_id(),
							  message=message, reply_to=reply_to)

	def transform_message(self, message, user_id):
		message = f'{self.vk.users.get(user_ids = (user_id))[0]["first_name"]}, {message}'
		if self.message_front:
			message = f'{self.message_front} {message}'
		return message

	def ignore_chat(self, chat_id):
		if not chat_id in self.ignore_chats:
			self.ignore_chats.append(chat_id)

	def ignore_user(self, user_id):
		if not user_id in self.ignore_users:
			self.ignore_users.append(user_id)

	def notice_user(self, user_id):
		if user_id in self.ignore_users:
			self.ignore_users.remove(user_id)