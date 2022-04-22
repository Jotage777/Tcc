<?php
    $apostar = "http://127.0.0.1:5000/greenzord/apostar";
    $resultapostar = json_decode(file_get_contents($apostar));

    header('Location: index.php');
?>