<?php
session_start();
$dbhost = 'oniddb.cws.oregonstate.edu';
$dbname = 'chanchek-db';
$dbuser = 'chanchek-db';
$dbpass = 'A8sePfr93XF1Jp1A';
$link = new mysqli($dbhost, $dbuser, $dbpass, $dbname);
if ($mysqli->connect_errno) {
    echo "Failed to connect to MySQL: (" . $mysqli->connect_errno . ") " . $mysqli->connect_error;
}
if (isset($_POST["submit"])) {
  $uid = mysqli_real_escape_string($link, $_POST["uid"]);
  $pwd = mysqli_real_escape_string($link, $_POST["pwd"]);

  // $kindarry=($_POST["beef"] || '0');
  // $newvalue=implode(",",$kindarry);
  // $uid = $_POST["uid"];
  // $pwd = $_POST["pwd"];
  $successsignup=0;
  // Error handlers
  // Check for empty fields
  if (empty($uid) || empty($pwd)) {
    $sql = "INSERT INTO user_dbb( user_uid, user_pwd ) 
                          VALUES ('$uid', '$pwd');";
      mysqli_query($link, $sql);
      $_SESSION['u_uid'] = $uid;
    header("Location: login.html?signup=empty");
    exit();
  } else {
    $sql = "SELECT * FROM `user_dbb` WHERE `user_uid`='$uid'";
    $result = mysqli_query($link, $sql);
    $resultCheck = mysqli_num_rows($result);
    if ($resultCheck > 0) {
      $query = "SELECT * FROM `user_dbb`  WHERE `user_uid` = '$uid' ";
      $result1 = mysqli_query($link, $query);
      $pref = mysqli_fetch_array($result, MYSQLI_NUM);
      $id=$pref[0];
      $_SESSION['u_uid'] = $uid;
      $_SESSION['u_id'] = $id;
      header("Location: ../~chanchek/about.html");
      exit();
    } else {
      // hashing passwordMeter
      // $hashedPwd = password_hash($pwd, PASSWORD_DEFAULT);
      // insert the user into the database
      // $sql = "INSERT INTO login_library (user_uid, user_pwd, email, beef, pork) VALUES ('$uid', '$pwd', '$email','$beef','$pork');";
      $sql = "INSERT INTO user_dbb( user_uid, user_pwd ) 
                          VALUES ('$uid', '$pwd');";
      mysqli_query($link, $sql);
      $_SESSION['u_uid'] = $uid;
      header("Location: ../~chanchek/login.html");
      exit();
    }
  }
} else {
  header("Location: login.html?signup=error");
  exit();
}