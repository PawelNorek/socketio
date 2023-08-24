from aiohttp import web
import socketio

sio = socketio.AsyncServer(async_mode='aiohttp')
app = web.Application()
sio.attach(app)

async def index(request):
  with open('./public/index.html') as f:
    return web.Response(text=f.read(), content_type='text/html')

@sio.event
def connect(sid, environ):
  print(sid, 'connected')

@sio.event
def disconnect(sid):
  print(sid, 'disconnected')

app.router.add_static('/public', 'public')
app.router.add_get('/', index)

if __name__ == "__main__":
  web.run_app(app, host='192.168.1.191', port='3001')