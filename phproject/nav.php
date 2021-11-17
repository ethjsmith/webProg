<?php
echo '
<nav>
<div class="nava">
<a href = "/"> Home</a>
<a href = "login">Login</a>
<a href = "register">Register</a>
<a href = "create">Create a list !</a>
<a href = "saved"> Your lists</a>
<a href = "about">About the site</a>
<a href = "test">       Name:';
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}
if (isset($_SESSION["username"])) {
  echo $_SESSION["username"];
}else {
  echo "Not logged in";
}
echo '</a> 
<br>
</div>
<br>
</nav>';
?>
