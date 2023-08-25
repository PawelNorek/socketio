from aiohttp import web
import socketio

sio = socketio.AsyncServer(async_mode='aiohttp')
app = web.Application()
sio.attach(app)

async def index(request):
  with open('./public/index.html') as f:
    return web.Response(text=f.read(), content_type='text/html')

async def task(sid):
  await sio.sleep(5)
  # await sio.emit('mult', {'numbers': [3, 4]}, callback=cb)
  result = await sio.call('mult', {'numbers': [3, 4]}, to=sid)
  print(result)

@sio.event
async def connect(sid, environ):
  print(sid, 'connected')
  sio.start_background_task(task, sid)  

@sio.event
async def disconnect(sid):
  print(sid, 'disconnected')

@sio.event
async def sum(sid, data):
  result = data['numbers'][0] + data['numbers'][1]
  return result

app.router.add_static('/public', 'public')
app.router.add_get('/', index)

if __name__ == "__main__":
  web.run_app(app, host='192.168.1.191', port='3001')