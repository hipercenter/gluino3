import tornado.ioloop
import tornado.web
from gluino import wrapper, DAL, Field, SQLFORM, cache, IS_NOT_EMPTY
import time

# configure the gluino wrapper                                               
wrapper.debug = True
wrapper.http = lambda code, message: tornado.web.HTTPError(code)
wrapper.redirect = lambda status, url: tornado.web.RequestHandler.redirect(url)

# create database and table
db=DAL('sqlite://storage.sqlite')
db.define_table('person',Field('name',requires=IS_NOT_EMPTY()))

# define action
def index(request):
    vars = wrapper.extract_vars(request.arguments)
    form = SQLFORM(db.person)
    if form.accepts(vars):
        message = 'hello %s' % form.vars.name
    else:
        message = 'hello anonymous'
    people = db(db.person).select()
    now  = cache.ram('time',lambda:time.ctime(),10)
    return locals()

class MainHandler(tornado.web.RequestHandler):
    @wrapper(view='templates/index.html',dbs=[db])
    def get(self): return index(self.request)
    def post(self): return self.get()

# configure routes
application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "static"}),
        ])

# start web server
if __name__ == "__main__":
    port = 8080
    application.listen(port)
    print('serving from http://0.0.0.0:%s ' % (port))
    tornado.ioloop.IOLoop.instance().start()
