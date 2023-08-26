from aiohttp import web
import socketio
import random

sio = socketio.AsyncServer(async_mode='aiohttp')
app = web.Application()
sio.attach(app)

client_count=0
a_count=0
b_count=0

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
  global client_count
  global a_count
  global b_count

  username = environ.get('HTTP_X_USERNAME')
  print('username: ', username)
  if not username:
    return False

  with sio.session(sid) as session:
    session['username'] = username

  sio.emit('user_joined', username)

  client_count += 1
  print(sid, 'connected')
  sio.start_background_task(task, sid)  
  await sio.emit('client_count', client_count)
  if random.random() > 0.5:
    sio.enter_room(sid, 'a')
    a_count += 1
    await sio.emit('room_count', a_count, to='a')
  else:
    sio.enter_room(sid, 'b')
    b_count += 1
    await sio.emit('room_count', b_count, to='b')

@sio.event
async def disconnect(sid):
  global client_count
  global a_count
  global b_count
  client_count -= 1
  print(sid, 'disconnected')
  await sio.emit('client_count', client_count)
  if ('a') in sio.rooms(sid):
    a_count -= 1
    await sio.emit('room_count', a_count, to='a')
  else:
    b_count -= 1
    await sio.emit('room_count', b_count, to='b')


@sio.event
async def sum(sid, data):
  result = data['numbers'][0] + data['numbers'][1]
  return result

app.router.add_static('/public', 'public')
app.router.add_get('/', index)

if __name__ == "__main__":
  web.run_app(app, host='192.168.1.191', port='3001')