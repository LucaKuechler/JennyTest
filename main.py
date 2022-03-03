const express = require("express");

let app = express();

app.get('/api', (req, res) => {
  res.send('Hello World!');
});

app.listen(3001, () =>
  console.log('Example app listening on port 3001!'),
);
