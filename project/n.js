var express = require('express');
var session = require('express-session');
var router = express.Router();
var qs = require("querystring");
//var sess;
// https://medium.com/@kiesp/playing-with-spotify-api-using-expressjs-bd8f25392ff3
var SpotifyWebApi = require('spotify-web-api-node');

// variables set up for new auth type
var scopes = ['user-read-private', 'user-read-email','playlist-modify-public','playlist-modify-private'],
redirectUri= 'http://localhost:8888/callback',
clientId= "6048c6185d4941dbba9e5e61f4e57c44",
state = "",
showDialog= true,
responseType= "code";
// https://github.com/thelinmichael/spotify-web-api-node
require('dotenv').config();

var spotifyApi = new SpotifyWebApi({
  redirectUri:redirectUri,
  clientSecret: '9095881a9eae48179b801202372a135c',
  clientId:clientId
});

router.get('/', function(req, res, next) {
  sess = req.session;
  res.render('index.html', { title: 'Express' });
});

// middleware function to check if user is authenticated.
// app.get('/protectedRoute', loggedIn, (req, res) => {
function checklogin(req, res, next) {
  if ("token" in req)  {
    // check if it's still valid?
    next();
  } else {
    res.redirect("/login");
  }
}
// contruct a credential for a user? haha
function constructCredentials(code) {
  return creds = {
    clientId:"",
    clientSecret:"",
    accessToken:""
  };
}

router.get('/login', (req,res) => {
  res.redirect(spotifyApi.createAuthorizeURL(scopes));
});

router.get('/callback', async (req,res) => {
  //console.log(JSON.stringify(result.tracks.items, null, 2));
    //ses = req.session;
    var error = req.query.error;
    var code = req.query.code;
    var state = req.query.state;
    res.cookie("code",code);
    if (error) {
   console.error('Callback Error:', error);
   res.send(`Callback Error: ${error}`);
   return;
 }
 spotifyApi
    .authorizationCodeGrant(code)
    .then(data => {
      const access_token = data.body['access_token'];
      const refresh_token = data.body['refresh_token'];
      const expires_in = data.body['expires_in'];

      req.session.access = access_token;
      req.session.refresh = refresh_token;

      spotifyApi.setAccessToken(access_token);
      spotifyApi.setRefreshToken(refresh_token);

      console.log('access_token:', access_token);
      console.log('refresh_token:', refresh_token);

      console.log(
        `Sucessfully retreived access token. Expires in ${expires_in} s.`
      );

      setInterval(async () => {
        const data = await spotifyApi.refreshAccessToken();
        const access_token = data.body['access_token'];

        console.log('The access token has been refreshed!');
        console.log('access_token:', access_token);
        res.cookie("code",access_token);
        spotifyApi.setAccessToken(access_token);
      }, expires_in / 2 * 1000);
    })
    .catch(error => {
      console.error('Error getting Tokens:', error);
      res.send(`Error getting Tokens: ${error}`);
    });
  res.redirect("/");
});

router.get('/userinfo', async (req,res) => {
    try {
      var result = await spotifyApi.getMe();
      console.log(result.body);
      res.status(200).send(result.body)
    } catch (err) {
      res.status(400).send(err)
    }
});

router.get('/saved', async (req,res) => {
  console.log("code for auth:" + req.cookies["code"]);

    var s = spotifyApi
    .authorizationCodeGrant(req.cookies['code'])
    .then(function(data) {
      spotifyApi.setAccessToken(data.body['access_token']);
      return spotifyApi.getUserPlaylists();
    })
    .then (function(data) {
      console.log("successful retrival? " + data)
      res.render("saved.html",{lists:data});

    })
    .catch(function(err) {
      console.log("error lol" + err.message);
    });
});
router.get('/me', async(req,res) => {
  console.log(req.session.access);
  console.log(req.sess);
  spotifyApi.setAccessToken(req.session.access);
  spotifyApi.setRefreshToken(req.session.refresh);
  var result = await spotifyApi.getMe()
  console.log()
  res.redirect("/");
});
router.get('/register', async(req,res) => {
  res.render('register.html', { title: 'Express' });

});
router.get('/create', async(req,res) => {
  if (req.method == 'POST') {
    var body="";
    req.on('data', function (data) {
      body += data;
      if (body.length > 1e6)
               request.connection.destroy();
       });

       request.on('end', function () {
           var post = qs.parse(body);
           // use post['blah'], etc.

       });
    console.log(post['inp']);
    }
    res.render('create.html', { title: 'Express' });

  });
router.post("/create", async(req,res) => {
  var result = ""
  spotifyApi.searchTracks(req.body.inp).then(
    function(data) {
      console.log("DATA recieved");
      result=data.body;
      console.log(result);
      console.log(result.tracks.items);
      if (result.tracks.items.length == 0) {
        // no results found ,error :)
        console.log("ERROR no tracks?")
        res.render("base.html",{contents:"Error, no results returned"});
      }else {

        res.render("searchresults.html",{results:result.tracks.items, title:"search results"});
      }
      //console.log(JSON.stringify(result.tracks.items, null, 2));

    },
    function(err) {
      console.log("error", err);
      result = "ERROR OCCURED sadge"
      res.render("create.html",{})
    }
  );

  //res.redirect("/create");
});

// Yeah dawg

// router.post('/create', async(req,res) => {
//   spotifyApi.searchTracks(req.)
//   .then(function(data) {
//     console.log('Search by "Love"', data.body);
//   }, function(err) {
//     console.error(err);
//   });
// });
router.get('/saved2', async(req,res) => {
  res.render('saved.html', { title: 'Express' });

});
router.get('/about', async(req,res) => {
  res.render('about.html', { title: 'Express' });

});
router.get('/test', async(req,res) => {
  res.render('index.html', { title: 'Express' });

});


module.exports = router;
