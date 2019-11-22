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
  $uname = mysqli_real_escape_string($link, $_POST["uname"]);
  $uphone = mysqli_real_escape_string($link, $_POST["uphone"]);
  $uorder1 = mysqli_real_escape_string($link, $_POST["uorder1"]);
  $uorder2 = mysqli_real_escape_string($link, $_POST["uorder2"]);
  // $kindarry=($_POST["beef"] || '0');
  // $newvalue=implode(",",$kindarry);
  // $uid = $_POST["uid"];
  // $pwd = $_POST["pwd"];
  $successsignup=0;
  // Error handlers
  // Check for empty fields
  if (empty($uname) || empty($uphone)||empty($uorder1)||empty($uorder2)) {
    $sql = "INSERT INTO Order( u_name, u_phone,order1,order2 ) 
                          VALUES ('$uname', '$uphone','$uorder1','$uorder2');";
      mysqli_query($link, $sql);
      $_SESSION['u_name'] = $uname;
    header("Location: login.html?signup=empty");
    exit();
  } else {
    $sql = "SELECT * FROM `Order` WHERE `u_name`='$uname'";
    $result = mysqli_query($link, $sql);
    $resultCheck = mysqli_num_rows($result);
    if ($resultCheck > 0) {
      $query = "SELECT * FROM `Order`  WHERE `u_phone` = '$uphone' ";
      $result1 = mysqli_query($link, $query);
      $pref = mysqli_fetch_array($result, MYSQLI_NUM);
      $id=$pref[0];
      $_SESSION['u_name'] = $uname;
      $_SESSION['u_name'] = $uname;
      header("Location: ../~chanchek/about.html");
      exit();
    } else {
      // hashing passwordMeter
      // $hashedPwd = password_hash($pwd, PASSWORD_DEFAULT);
      // insert the user into the database
      // $sql = "INSERT INTO login_library (user_uid, user_pwd, email, beef, pork) VALUES ('$uid', '$pwd', '$email','$beef','$pork');";
      $sql = "INSERT INTO `Order` (u_name, u_phone, order1, order2) 
                          VALUES ('$uname', '$uphone','$uorder1','$uorder2');";
      mysqli_query($link, $sql);
      $_SESSION['u_name'] = $uname;
      header("Location: ../~chanchek/menu.html");
      exit();
    }
  }
} else {
  header("Location: ../~chanchek/login.html");
  exit();
}