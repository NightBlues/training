import time
import logging

from raven.handlers.logging import SentryHandler
from raven.conf import setup_logging

# SENTRY_URL = "https://xxxx:yyyyy@app.getsentry.com/11111"



LOG = logging.getLogger("c2")
LOG_APP1 = logging.getLogger("c2.app1")
LOG_APP2 = logging.getLogger("c2.app2")

def setup_log():
	logging.basicConfig()
	handler = SentryHandler(SENTRY_URL, tags={"az": "ru-msk-af315t"}, auto_log_stacks=True)
	# setup_logging(handler)
	logging.getLogger("c2").addHandler(handler)


def main():
	setup_log()
	LOG.debug("Hello")
	LOG_APP1.error("Error logged with .error method")
	try:
		x = 2
		raise RuntimeError("Not enough resourses")
	except:
		LOG_APP1.exception("Error ocured:\n")

	# time.sleep(40)
	# try:
	# 	raise Exception("Hello app2")
	# except:
	# 	LOG_APP2.exception("Error in app2")



if __name__ == "__main__":
	main()
