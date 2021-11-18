var express = require('express');
var router = express.Router();
var qs = require("querystring");
// https://medium.com/@kiesp/playing-with-spotify-api-using-expressjs-bd8f25392ff3
var SpotifyWebApi = require('spotify-web-api-node');
scopes = ['user-read-private', 'user-read-email','playlist-modify-public','playlist-modify-private']
// https://github.com/thelinmichael/spotify-web-api-node
require('dotenv').config();

var spotifyApi = new SpotifyWebApi({
  clientId: '6048c6185d4941dbba9e5e61f4e57c44',
  clientSecret: '9095881a9eae48179b801202372a135c',
  redirectUri: 'http://localhost:8888/callback',
});

/* GET home page. */
router.get('/', function(req, res, next) {
  // if (typeof spotifyApi.getUser() !== "undefined" && spotifyApi.getUser()) {
  //   req.user = spotifyApi.getUser()
  // }
  // else {
  //   req.user="Not Logged In"
  // }
  res.render('index.html', { title: 'Express' });
});

router.get('/login', (req,res) => {
  var html = spotifyApi.createAuthorizeURL(scopes)
  console.log(html)
  //res.send(html+"&show_dialog=true")
  res.redirect(html)
  //res.render('index.html', { title: 'Express' });
})

router.get('/callback', async (req,res) => {
  const { code } = req.query;
  console.log("GOT THE CODE :) ")
  console.log(code)
  try {
    var data = await spotifyApi.authorizationCodeGrant(code)
    const { access_token, refresh_token } = data.body;
    spotifyApi.setAccessToken(access_token);
    spotifyApi.setRefreshToken(refresh_token);

    res.redirect('http://localhost:8888');
  } catch(err) {
    res.redirect('/#/error/invalid token');
  }
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
  try {
    var result = await spotifyApi.getUserPlaylists();
    console.log(result.body);
    //res.status(200).send(result.body);
    res.render("base.html",{contents:result.body});
  } catch (err) {
    res.status(400).send(err)
  }

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
