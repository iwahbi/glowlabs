var express = require('express');
var app = express();
var mysql = require('mysql');

app.set('view engine', 'ejs');
app.set('views', './views');

var con = mysql.createConnection({
  host: "localhost",
  user: "id19322426_rubangura",
  password: "Pleasework1!",
  database: "id19322426_alarmsystem"
});

var obj = {};

con.connect(function (err) {
  if (err) {
    console.error("Error connecting to the database: " + err.stack);
    return;
  }
  console.log("Connected to the database with id " + con.threadId);

  
});

app.get('/lesZones', function (req, res) {
  con.query("SELECT * FROM statuses", function (err, result, fields) {
    if (err) {
      console.error("Error querying the database: " + err.stack);
      res.status(500).send("Internal Server Error");
      return;
    }

    obj = { users: result };
    console.log(obj);
    res.render('ViewSQL', obj);
  });
});

var port = process.env.PORT || 3001;
app.listen(port, function () {
  console.log("Server is running on port: " + port);
});
