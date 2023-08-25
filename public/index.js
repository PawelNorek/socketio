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
