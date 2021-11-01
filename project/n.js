var express = require('express');
var router = express.Router();

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
  res.render('index.html', { title: 'Express' });
});

router.get('/login', (req,res) => {
  var html = spotifyApi.createAuthorizeURL(scopes)
  console.log(html)
  res.send(html+"&show_dialog=true")
})

router.get('/callback', async (req,res) => {
  const { code } = req.query;
  console.log(code)
  try {
    var data = await spotifyApi.authorizationCodeGrant(code)
    const { access_token, refresh_token } = data.body;
    spotifyApi.setAccessToken(access_token);
    spotifyApi.setRefreshToken(refresh_token);

    res.redirect('http://localhost:3001/home');
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

router.get('/playlists', async (req,res) => {
  try {
    var result = await spotifyApi.getUserPlaylists();
    console.log(result.body);
    res.status(200).send(result.body);
  } catch (err) {
    res.status(400).send(err)
  }

});


module.exports = router;
