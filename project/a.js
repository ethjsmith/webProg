var express = require('express');
const redis = require('redis');

var nunjucks = require("nunjucks");
var bodyparser = require("body-parser");
var request = require('request'); // "Request" library
var cors = require('cors');
var querystring = require('querystring');
var cookieParser = require('cookie-parser');
var session = require('express-session');
var MemoryStore = require("memorystore")(session);

let RedisStore = require('connect-redis')(session);
var client  = redis.createClient();


const app = express();

nunjucks.configure('views', {
    autoescape: true,
    express: app
});
(async () => {
await client.connect();
await client.set('key', 'something');
const value = await client.get('key');
console.log(value);
})();
//Configure redis client
// const redisClient = redis.createClient({
//     host: 'localhost',
//     port: 6379
// })
// redisClient.on('error', function (err) {
//     console.log('Could not establish a connection with redis. ' + err);
// });
// redisClient.on('connect', function () {
//     console.log('Connected to redis successfully');
// });

// redisClient.set('foo', 'bar', (err, reply) => {
//     if (err) throw err;
//     console.log(reply);
//
//     redisClient.get('foo', (err, reply) => {
//         if (err) throw err;
//         console.log(reply);
//     });
// });
app.use(express.static(__dirname + '/public'))
.use(cors())
.use(bodyparser.urlencoded({extended:true}))
.use(session({
    secret: 'TEMPlol91823810',
    // create new redis store.
    //store: new RedisStore({client:client}),
    store: new MemoryStore({checkPeriod:86400000}),
    saveUninitialized: false,
    resave: false,
    cookie: {
        secure: false, // if true only transmit cookie over https
        httpOnly: false, // if true prevent client side JS from reading the cookie
        maxAge: 1000 * 60 * 10 // session max age in miliseconds
    }
}))
.use(cookieParser());

app.set("view engine", "nunjucks")
var aa = require("./n")
client.on('error', console.error)

app.use(aa)
app.listen(8888, () => {
  console.log(`Listening to requests on http://localhost:8888`);
});
