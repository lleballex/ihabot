# iHA bot

## Instalation

To install and run the bot, follow these steps:

Clone the repository
```bash
git clone https://github.com/lleballex/ihabot.git
cd ihabot
```

Create a virtual environment. If you don't want to do this, skip this step
```bash
python -m venv env
env\scripts\activate.bat
```

Set up your bot. Go to 'src/config.py' and set the value of the 'API_TOKEN' variable (access token).  
Create a database 'db.sqlite3' (for the main response patterns) with the 'main_patterns' table. This table should have two columns: 'pattern' (user message) and 'answer' (your answer).  
Then create a file 'src/extra_patterns.py'. One more templates will be stored in it, but with regular expressions. Write them down by sample:
```python
patterns = {
	'.*pattern_1.*': [
		'answer_1',
		'answer_2',
	],
	'pattern_2[//!//?]': [
		'answer_1',
		'answer_2',
	],
}
```

Install modules and run the bot
```bash
pip install -r requirements.txt
cd src
python bot.py
```