<?php
session_start();
if (!isset($_SESSION['username']) == true && (!isset($_SESSION['password']) == true)) {
    unset($_SESSION['username']);
    unset($_SESSION['password']);
    header('Location: login.php');
}

$logado = $_SESSION['username'];

$urlid = "http://127.0.0.1:5000/greenzord/4/2/" . $logado;
$resultado_id = json_decode(file_get_contents($urlid));

$id = $_GET['id'];

if (!empty($_GET['id'])) {
    $url = "http://127.0.0.1:5000/greenzord/5/2/" . $id;
    $bot_edit = json_decode(file_get_contents($url));
    if ($bot_edit != 0 and $bot_edit[14] == $resultado_id) {
        $urldel = "http://127.0.0.1:5000/greenzord/bots/deletar/" . $id;
        $response = file_get_contents($urldel);
        header('Location: lista_bots.php');
    } else {
        header('Location: lista_bots.php');
    }
} else {
    header('Location: lista_bots.php');
}
?>