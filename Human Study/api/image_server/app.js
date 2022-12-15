/* This is the code for the image server.
   Very little programming is required as express can easily be configured to be a static image server.
*/
const express = require('express')
const app = express()
const port = 3030

app.get('/', (req, res) => {
  res.send('Hello World!')
})

const path = require('path');
app.use(express.static(path.join(__dirname, 'public'))) // this is the folder from which we serve our images

app.listen(port, () => {
  console.log(`App listening on port ${port}`)
})