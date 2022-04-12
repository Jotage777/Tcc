<?php
    session_start();
    if(!isset($_SESSION['username']) == true && (!isset($_SESSION['password']) == true)){
        unset($_SESSION['username']);
        unset($_SESSION['password']);
        header('Location: login.php');
    }

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
        );
    }
    header('Location: lista_bots.php');
?>