from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application
from functional import f
class MainHandler(RequestHandler):
    def get(self, pos):

        c = f(pos)
        self.write({"num" : c})

app = Application([
    (r"/([0-9]+)?", MainHandler)
])
app.listen(8080)

IOLoop.current().start()