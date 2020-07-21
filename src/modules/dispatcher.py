class Dispatcher:
	def __init__(self, bot, admins=[]):
		self.bot = bot
		self.handlers = []
		self.admins = admins

	def add_admin(id):
		if not id in self.admins:
			self.admins.append(id)

	def message_handler(self, command, from_chat=True, from_user=True, admin=False):
		def decorator(func):
			self.handlers.append({
				'command': command,
				'from_chat': from_chat,
				'from_user': from_user,
				'admin': admin,
				'func': func,
				})
			return func
		return decorator

	def handle(self, event):
		for handler in self.handlers:
			if event.text.startswith(handler['command']):
				if not handler['admin'] or (handler['admin'] and event.user_id in self.admins):
					if (event.from_user and handler['from_user']) or (event.from_chat and handler['from_chat']):
						handler['func'](event)
						return True
				else:
					self.bot.send_message(event.peer_id, 'Эта команда только для администраторов', reply_to=event.message_id)

		return False