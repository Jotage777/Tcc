<?php
    session_start();
    if(isset($_POST['submit']) && !empty($_POST['username']) && !empty($_POST['password'])){
        $username = $_POST['username'];
        $password = $_POST['password'];

        $dados = array(
            "username" => $username,
            "password" => $password
        );

        $json = json_encode($dados);

        $url = "http://127.0.0.1:5000/greenzord/login_cadastro";

        $ch = curl_init($url);
        curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "GET");
        curl_setopt($ch, CURLOPT_POSTFIELDS, $json);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_HTTPHEADER, array(
                'Content-Type: application/json',
                'Content-Length: ' . strlen($json))
        );

        $jsonRet = json_decode(curl_exec($ch));

        if($jsonRet){
            $_SESSION['username'] = $username;
            $_SESSION['password'] = $password;
            header('Location: index.php');
        }
        else{
            unset($_SESSION['username']);
            unset($_SESSION['password']);
            header('Location: login.php?entrar=erro');
        }
    }
    else{
        unset($_SESSION['username']);
        unset($_SESSION['password']);
        header('Location: login.php?entrar=erro');
    }
?>