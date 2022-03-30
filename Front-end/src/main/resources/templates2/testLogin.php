<?php
    session_start();
    if(isset($_POST['submit']) && !empty($_POST['username']) && !empty($_POST['password'])){
        $username = $_POST['username'];
        $password = $_POST['password'];
        $_SESSION['username'] = $username;
        $_SESSION['password'] = $password;
        header('Location: index.php');
    }
    else{
        header('Location: login.php');
    }
?>