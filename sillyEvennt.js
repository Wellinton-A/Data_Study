const EventEmitter = require('events')

const celebrity = new EventEmitter()

celebrity.on('race win', () => {
    console.log('Congratulations!')
})

celebrity.on('race lose', () => console.log('Sorry you lost!'))

celebrity.emit('race win')