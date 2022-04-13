<?php
    session_start();
    if(!isset($_SESSION['username']) == true && (!isset($_SESSION['password']) == true)){
        unset($_SESSION['username']);
        unset($_SESSION['password']);
        header('Location: login.php');
    }

    $logado = $_SESSION['username'];
    $id = $_POST['id'];
    if(isset($_POST['update'])) {

        $dados = array(
            "nome" => $_POST['nome'],
            "responsabilidade" => $_POST['responsa'],
            "odd_minima" => $_POST['oddmin'],
            "odd_maxima" => $_POST['oddmax'],
            "tempo_jogo_minimo" => $_POST['tempomin'],
            "tempo_jogo_maximo" => $_POST['tempomax'],
            "finalizacao_min" => $_POST['finamin'],
            "finalizacao_max" => $_POST['finamax'],
            "posse_bola_min" => $_POST['possemin'],
            "posse_bola_max" => $_POST['possemax'],
            "apostar" => $_POST['timapo'],
            "analisar" => $_POST['timesta'],
            "ativado" => "1",
            "username" => $logado
        );

        $json = json_encode($dados);

        $url = "http://127.0.0.1:5000/greenzord/bots/editar/" . $id;

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
?>