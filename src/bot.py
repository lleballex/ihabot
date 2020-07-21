from misc import bot, dp, database
import handlers

import traceback


if __name__ == '__main__':
	print('Бот начал работу!')

	for event in bot.longpoll.listen():
		try:
			if bot.is_chat_new_message(event):
				if not dp.handle(event):
					message = database.get_answer(event.text)
					if message and bot.reply_message:
						bot.send_message(event.peer_id, bot.transform_message(message, event.user_id), reply_to=event.message_id)
					elif message and not bot.reply_message:
						bot.send_message(event.peer_id, bot.transform_message(message, event.user_id))
			
			#elif bot.is_personal_new_message(event):
			#	print('New personal message')
			#	dp.handle(event)

		except Exception as e:
			print(traceback.format_exc())