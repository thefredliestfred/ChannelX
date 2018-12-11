<?php
require_once("./api/config/membersite_config.php");

$cxmembersite->LogOut();
 ?>

<!DOCTYPE html>
<html>
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8"/>
  <title>Logout</title>
  <link rel="STYLESHEET" type='text/css' href="assets/css/style.css"/>
  <script type="text/javascript" src="scripts/gen_validatorv31.js"></script>
</head>
<body>
  <h2>You have logged out.</h2>
  <p>
    <a href="login.php">Login Again</a>
  </p>
</body>
</html>
