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

$dados_ati = array(
    "ativado" => "1",
);

$dados_des = array(
    "ativado" => "0",
);

if (!empty($_GET['id'])) {
    $url = "http://127.0.0.1:5000/greenzord/5/2/" . $id;
    $bot_edit = json_decode(file_get_contents($url));
    if ($bot_edit != 0 and $bot_edit[14] == $resultado_id) {

        if($bot_edit[11]=="1"){
            $json = json_encode($dados_des);

            $url = "http://127.0.0.1:5000/greenzord/bots/editar/2/" . $id;

            $ch = curl_init($url);
            curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");
            curl_setopt($ch, CURLOPT_POSTFIELDS, $json);
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
            curl_setopt($ch, CURLOPT_HTTPHEADER, array(
                    'Content-Type: application/json',
                    'Content-Length: ' . strlen($json))
            );

            $jsonRet = json_decode(curl_exec($ch));

        }
        elseif ($bot_edit[11]=="0"){
            $json = json_encode($dados_ati);

            $url = "http://127.0.0.1:5000/greenzord/bots/editar/2/" . $id;

            $ch = curl_init($url);
            curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");
            curl_setopt($ch, CURLOPT_POSTFIELDS, $json);
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
            curl_setopt($ch, CURLOPT_HTTPHEADER, array(
                    'Content-Type: application/json',
                    'Content-Length: ' . strlen($json))
            );

            $jsonRet = json_decode(curl_exec($ch));

        }

        header('Location: lista_bots.php');
    } else {
        header('Location: lista_bots.php');
    }
} else {
    header('Location: lista_bots.php');
}
?>