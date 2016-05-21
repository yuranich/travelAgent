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
	answer = json.loads(urlfetch.fetch(url = PLATFORM_URL.format(chat_id, text), method = "GET").content
	answer_test = answer.get('text')
	answer_
	logging.info("Answering {}".format(answer))
	if answer:
		return Response(status_int = 200, body = json.dumps({'method': 'sendMessage', 'chat_id' : chat_id, 'text' : answe}), content_type = 'application/json')
	else:
		return Response(status_int = 200, body = None)