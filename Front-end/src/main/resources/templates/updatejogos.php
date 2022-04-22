<?php
    $jogos = "http://127.0.0.1:5000/greenzord/jogos";
    $resultjogos = json_decode(file_get_contents($jogos));

    header('Location: index.php');
?>