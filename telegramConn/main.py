from google.appengine.api import urlfetch
from google.appengine.ext import vendor
vendor.add("libs")
import logging
import json
import telegram
import framework
from webapp2 import Response


TELEGRAM_API_TOKEN = "234472068:AAHspi0uV9ip_NVNeCkePcJJCqbaPoG9xEg"
PLATFORM_URL = "http://yuranich-server.ddns.net:8080/travel-agent/rest/dialog?userid={}&text={}"

app = framework.WSGIApplication()
bot = telegram.Bot(token=TELEGRAM_API_TOKEN)
webhook = bot.setWebhook('https://magellan-telegram.appspot.com/messagehandler')

@app.route("/messagehandler")
def messagehandler(request, *args, **kwargs):
	update = telegram.Update.de_json(json.loads(request.body))
	chat_id = update.message.chat.id
	text = update.message.text.encode('utf-8')

	logging.info("Received {} from {}".format(text, chat_id))
	try:
		answer = json.loads(urlfetch.fetch(url = PLATFORM_URL.format(chat_id, text), method = "GET").content)
	except:
		return ""
	answer_text = answer.get('response')
	answer_buttons = answer.get('buttons')
	logging.info("Got {}".format(answer))
	if answer_text:
		body = {'method': 'sendMessage', 'chat_id' : chat_id, 'text' : answer_text}
		if answer_buttons:
			body['reply_markup'] = {'keyboard' : [[str(button) for button in json.loads(answer_buttons)]], 'resize_keyboard' : True}
		body = json.dumps(body)
	else:
		body = None
	logging.info('Body is {}'.format(body))
	return Response(status_int = 200, body = body, content_type = 'application/json')