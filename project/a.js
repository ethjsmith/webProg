var express = require('express');
var nunjucks = require("nunjucks");

var request = require('request'); // "Request" library
var cors = require('cors');
var querystring = require('querystring');
var cookieParser = require('cookie-parser');

const app = express();
var aa = require("./n")

nunjucks.configure('views', {
    autoescape: true,
    express: app
});
app.use(express.static(__dirname + '/public'))
.use(cors())
.use(cookieParser());
app.set("view engine", "nunjucks")

app.use(aa)
app.listen(8888, () => {
  console.log(`Listening to requests on http://localhost:8888`);
});
