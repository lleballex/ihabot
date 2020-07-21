from extra_patterns import patterns

import sqlite3
from re import match
from random import choice


class Database:
	def __init__(self, **kwargs):
		self.connection = sqlite3.connect(**kwargs)
		self.cursor = self.connection.cursor()

	def _get_from_main_patterns(self, text):
		answers = self.cursor.execute('SELECT `answer` FROM `main_patterns` WHERE `pattern` = ?', (text.lower(),)).fetchall()
		if answers:
			return choice(answers)[0]
		return None

	def _get_from_extra_patterns(self, text):
		for pattern in patterns:
			if match(pattern, text.lower()):
				answer = choice(patterns[pattern])
				return answer
		return None

	def get_answer(self, text):
		answer = self._get_from_main_patterns(text)
		if answer:
			return answer

		answer = self._get_from_extra_patterns(text)
		if answer:
			return answer