import { io } from 'https://cdn.socket.io/4.4.1/socket.io.esm.min.js'

console.log('test')

const sio = io()

sio.on('connect', () => {
	console.log('connected')
	sio.emit('sum', { numbers: [1, 2] })
})

sio.on('disconnect', () => {
	console.log('disconnected')
})

sio.on('sum_result', data => {
	console.log(data)
})
