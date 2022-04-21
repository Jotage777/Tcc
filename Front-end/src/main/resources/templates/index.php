<?php
    session_start();
    if(!isset($_SESSION['username']) == true && (!isset($_SESSION['password']) == true)){
        unset($_SESSION['username']);
        unset($_SESSION['password']);
        header('Location: login.php');
    }
    $logado = $_SESSION['username'];

    $id_user = "http://127.0.0.1:5000/greenzord/4/2/" . $logado;
    $resultado_id_user = json_decode(file_get_contents($id_user));

    $jogos = "http://127.0.0.1:5000/greenzord/3/1/" . $resultado_id_user;
    $jogos_live = json_decode(file_get_contents($jogos));

    $apostas = "http://127.0.0.1:5000/greenzord/apostas/usuario/" . $resultado_id_user;
    $apostas_feitas = json_decode(file_get_contents($apostas));

//    $url = "http://127.0.0.1:5000/greenzord/3/2/" . $resultado_id_user;
//    $response = file_get_contents($url);

//    var_dump($jogos_live);
?>

<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <title>Index</title>
    <style>
        :root{
            --color-white: #fff;
            --color-green: #2E8B57;
            --color-green2: #32CD32;
            --color-gradient: linear-gradient(45deg,green,cyan);
        }
        body{
            font-family: Arial, Helvetica, sans-serif;
            background-image: var(--color-gradient);
            color: var(--color-white);
        }
        *{
            margin: 0;
            padding: 0;
        }
        .img_logo_header{
            width: 45px;
        }
        .header,
        .navigation_header{
            display: flex;
            flex-direction: row;
            align-items: center;
        }
        .header{
            background-color: var(--color-green);
            box-shadow: 1px 1px 4px var(--color-green2);
            height: 56px;
            justify-content: space-between;
            padding: 0 5%;
        }
        .navigation_header{
            gap: 48px;
        }
        .navigation_header a{
            text-decoration: none;
            color: var(--color-white);
            font-weight: bold;
        }
        .active{
            background-color: var(--color-green2);
            padding: 10px;
            border-radius: 10px;
        }
        .content{
            text-align: center;
            padding-top: 16px;
        }
        .table-bg{
            background: rgba(0, 0, 0, 0.3);
            border-radius: 15px 15px 0 0;
        }
    </style>
</head>
<body id="body">
    <div class="header" id="header">
        <div class="logo_header">
            <img scr="robo.png" class="img_logo_header" alt="Logo Greenzord">
        </div>
        <div class="navigation_header" id="navigation_header">
            <a href="#" class="active">Home</a>
            <a href="relatorio.php">Relatorio</a>
            <a href="lista_bots.php">Bots</a>
        </div>
        <div class="navigation_header" id="navigation_header">
            <?php
                echo "<a>$logado</a>"
            ?>
            <?php
                echo "<a>Saldo</a>"
            ?>
            <a href="sair.php">Sair</a>
        </div>
    </div>
    <div>
        <div class="content" id="content">
            <h1>Lista de Jogos</h1>
        </div>
        <div class="m-5">
            <table class="table table-bg text-white">
                <thead>
                <tr>
                    <th scope="col">Data</th>
                    <th scope="col">Campeonato</th>
                    <th scope="col">Casa</th>
                    <th scope="col">Gols</th>
                    <th scope="col">Gols</th>
                    <th scope="col">Fora</th>
                    <th scope="col">Posse</th>
                    <th scope="col">Finalização</th>
                    <th scope="col">1</th>
                    <th scope="col">X</th>
                    <th scope="col">2</th>
                </tr>
                </thead>
                <tbody>
                <?php
                foreach ($jogos_live as $bot){
                    echo "<tr>";
                    echo "<td>" . $bot[6] . " minutos</td>"; //tempo
                    echo "<td>" . $bot[2] . "</td>"; //id_campeonato
                    echo "<td>" . $bot[1] . "</td>"; //time_casa
                    echo "<td>" . $bot[4] . "</td>"; //resultado_casa
                    echo "<td>" . $bot[5] . "</td>"; //resultado_fora
                    echo "<td>" . $bot[3] . "</td>"; //time_fora
                    echo "<td>" . $bot[8] . "% x " . $bot[9] . "%</td>"; //posse
                    echo "<td>" . $bot[10] . " x " . $bot[11] . "</td>"; //finalização
                    echo "<td>" . $bot[12] . "</td>"; //odd_casa
                    echo "<td>" . $bot[13] . "</td>"; //odd_fora
                    echo "<td>" . $bot[14] . "</td>"; //odd_empate
                    echo "<tr>";
                }
                ?>
                </tbody>
            </table>
        </div>
    </div>
    <div>
        <div class="content" id="content">
            <h1>Lista de Apostas</h1>
        </div>
        <div class="m-5">
            <table class="table table-bg text-white">
                <thead>
                <tr>
                    <th scope="col">Mercado</th>
                    <th scope="col">Valor Apo</th>
                    <th scope="col">Odd</th>
                    <th scope="col">Situação</th>
                    <th scope="col">bot</th>
                    <th scope="col">jogo</th>
                    <th scope="col">usuario</th>
                    <th scope="col">casa_fora</th>
                </tr>
                </thead>
                <tbody>
                <?php
                foreach ($apostas_feitas as $aposta){
                    echo "<tr>";
                    echo "<td>" . $aposta[1] . "</td>"; //Mercado
                    echo "<td>" . $aposta[2] . "</td>"; //valor apostado
                    echo "<td>" . $aposta[3] . "</td>"; //odd
                    echo "<td>" . $aposta[4] . "</td>"; //situaão
                    echo "<td>" . $aposta[5] . "</td>"; //id bot
                    echo "<td>" . $aposta[6] . "</td>"; //id jogo
                    echo "<td>" . $aposta[7] . "</td>"; //id usuario
                    echo "<td>" . $aposta[8] . "</td>"; //casa_fora
                    echo "<tr>";
                }
                ?>
                </tbody>
            </table>
        </div>
    </div>
</body>
</html>