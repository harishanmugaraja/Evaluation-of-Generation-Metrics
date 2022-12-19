/* This is the code for the image server.
   Very little programming is required as express can easily be configured to be a static image server.
*/
const express = require('express')
const bp = require('body-parser')
const cors = require('cors');
const app = express()
const port = 3030

app.use(cors())
app.use(bp.json())
app.use(bp.urlencoded({ extended: true }))

app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.post('/submit-form', (req, res) => {
  // req.body contains the form data
  console.log(req.body)

  // do something with the form data, like save it to a database or send it via email

  // send a response to the client
  res.send('Form submitted successfully!')
})

const path = require('path');
app.use(express.static(path.join(__dirname, 'public'))) // this is the folder from which we serve our images

app.listen(port, () => {
  console.log(`App listening on port ${port}`)
})