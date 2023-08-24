import { io } from 'https://cdn.socket.io/4.4.1/socket.io.esm.min.js'

console.log('test')

const sio = io()

sio.on('connect', () => {
	console.log('connected')
})

sio.on('disconnect', () => {
	console.log('disconnected')
})
