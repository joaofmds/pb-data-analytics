const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
    res.send('Olá, minha imagem! Eu me chamo João')
})

app.listen(port, () => {
    console.log(`Executando na porta: ${port}`)
})