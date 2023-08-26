import { io } from 'https://cdn.socket.io/4.4.1/socket.io.esm.min.js'

console.log('test')

const sio = io()

sio.on('connect', () => {
	console.log('connected')
	sio.emit('sum', { numbers: [1, 2] }, result => {
		console.log(result)
	})
})

sio.on('disconnect', () => {
	console.log('disconnected')
})

sio.on('mult', (data, cb) => {
	const result = data.numbers[0] * data.numbers[1]
	cb(result)
})

sio.on('client_count', data => {
	console.log(data)
})

sio.on('room_count', count => {
	console.log('Thera are ', count, ' clients in my room.')
})

sio.on('user_joined', username => {
	console.log('User ', username, ' has joined.')
})

sio.on('user_left', username => {
	console.log('User ', username, ' has left.')
})
