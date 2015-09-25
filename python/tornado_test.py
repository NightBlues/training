import time
import threading

import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.gen

def threaded(fn):
    def run(*k, **kw):
        t = threading.Thread(target=fn, args=k, kwargs=kw)
        t.start()
    return run

def defertothread(func):

    @threaded
    def task_func(*args, **kwargs):
        callback = kwargs["callback"]
        del kwargs["callback"]
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            result = e
        callback(result)

    def handler(self, *args, **kwargs):
        result = yield tornado.gen.Task(task_func, self, *args, **kwargs)
        if isinstance(result, Exception):
            raise result
        elif isinstance(result, tuple) and len(result) == 3:
            method, a, kwa = result
            getattr(self, method)(*a, **kwa)

    return handler

class Application(tornado.web.Application):
    """Main application class."""

    def __init__(self):
        """Init handlers and settings."""

        handlers = [
            (r"/$", MyHandler),
        ]
        settings = dict(
            debug=True
        )
        super(Application, self).__init__(handlers, **settings)


class MyHandler(tornado.web.RequestHandler):

    @tornado.gen.coroutine
    @defertothread
    def get(self):
        time.sleep(5)
        # raise RuntimeError("hello")
        return ("write", ["Done"], {})
        # self.write("Done")

tornado.httpserver.HTTPServer(Application()).listen(8080)
tornado.ioloop.IOLoop.instance().start()
