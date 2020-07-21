import config
from misc import bot, dp

from vk_api.exceptions import ApiError


@dp.message_handler(command='/stop', admin=True)
def stop(event):
	bot.send_message(event.peer_id, 'Бот остановлен', reply_to=event.message_id)
	raise SystemExit

@dp.message_handler(command='/set_message_front', admin=True)
def start(event):
	new_front = event.text.replace('/set_message_front', '')
	if new_front:
		bot.message_front = new_front.strip()
		bot.send_message(event.peer_id, f'Начало сообщения обновлено', reply_to=event.message_id)
	else:
		bot.send_message(event.peer_id, f'Введите продолжение команды', reply_to=event.message_id)

@dp.message_handler(command='/set_message_delay', admin=True)
def set_message_delay(event):
	new_delay = event.text.replace('/set_message_delay', '')
	if new_delay:
		try:
			new_delay = int(new_delay)
			bot.send_message(event.peer_id, f'Новое значение задержки перед отправлением сообщения установлено', reply_to=event.message_id)
			bot.message_delay = new_delay
		except ValueError:
			bot.send_message(event.peer_id, f'Значение должно быть числом', reply_to=event.message_id)
	else:
		bot.send_message(event.peer_id, 'Введите продолжение команды', reply_to=event.message_id)

@dp.message_handler(command='/toggle_reply_message', admin=True)
def toggle_reply_message(event):
	if bot.reply_message:
		bot.reply_message = False
		bot.send_message(event.peer_id, 'Пересылка сообщений выключена', reply_to=event.message_id)
	else:
		bot.reply_message = True
		bot.send_message(event.peer_id, 'Пересылка сообщений включена', reply_to=event.message_id)

@dp.message_handler(command='/ignore_chat', admin=True, from_user=False)
def ignore_chat_from_chat(event):
	bot.ignore_chat(event.chat_id)
	print(event.chat_id, event.peer_id)
	bot.send_message(event.peer_id, 'Этот чат теперь будет игнорироваться', reply_to=event.message_id)

@dp.message_handler(command='/ignore_user', admin=True)
def ignore_user(event):
	user_id = event.text.replace('/ignore_user', '')

	if user_id:
		try:
			bot.ignore_user(int(user_id))
			bot.send_message(event.peer_id, 'Этот пользователь теперь будет игнорироваться', reply_to=event.message_id)
		except ValueError:
			bot.send_message(event.peer_id, 'Значение должно быть числом', reply_to=event.message_id)
	else:
		bot.send_message(event.peer_id, 'Введите продолжение команды', reply_to=event.message_id)

@dp.message_handler(command='/notice_user', admin=True)
def notice_user(event):
	user_id = event.text.replace('/notice_user', '')

	if user_id:
		try:
			bot.notice_user(int(user_id))
			bot.send_message(event.peer_id, 'Этот пользователь теперь не будет игнорироваться', reply_to=event.message_id)
		except ValueError:
			bot.send_message(event.peer_id, 'Значение должно быть числом', reply_to=event.message_id)
	else:
		bot.send_message(event.peer_id, 'Введите продолжение команды', reply_to=event.message_id)

@dp.message_handler(command='/kick', admin=True, from_user=False)
def kick_user(event):
	user_id = event.text.replace('/kick', '')

	if user_id:
		try:
			bot.vk.messages.removeChatUser(chat_id=event.chat_id, user_id=int(user_id))
			bot.send_message(event.peer_id, 'Этот пользователь исключен из чата', reply_to=event.message_id)
		except ValueError:
			bot.send_message(event.peer_id, 'Значение должно быть числом', reply_to=event.message_id)
		except ApiError as e:
			bot.send_message(event.peer_id, f'Ошибка - {e}', reply_to=event.message_id)
	else:
		bot.send_message(event.peer_id, 'Введите продолжение команды', reply_to=event.message_id)
