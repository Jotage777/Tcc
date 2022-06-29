<?php
session_start();
if (!isset($_SESSION['username']) == true && (!isset($_SESSION['password']) == true)) {
    unset($_SESSION['username']);
    unset($_SESSION['password']);
    header('Location: login.php');
}
$logado = $_SESSION['username'];

$dados = explode("?", $_GET['id']);
$id = $dados[0];
$nome = $dados[1];

$urlid = "http://127.0.0.1:5000/greenzord/4/2/" . $logado;
$resultado_id = json_decode(file_get_contents($urlid));

$apostas = "http://127.0.0.1:5000/greenzord/apostas/bot/" . $id . "/1";
$apostas_feitas = json_decode(file_get_contents($apostas));

$saldo = "http://127.0.0.1:5000/greenzord/4/3/" . $resultado_id;
$saldo_usuario = json_decode(file_get_contents($saldo));

$relatorio = "http://127.0.0.1:5000/greenzord/relatorio/1/" . $id;
$relatorio_bot = json_decode(file_get_contents($relatorio));
?>

<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <title>RelatorioBot</title>
    <style>
        :root {
            --color-white: #fff;
            --color-green: #2E8B57;
            --color-green2: #32CD32;
            --color-gradient: linear-gradient(45deg, green, cyan);
        }

        body {
            font-family: Arial, Helvetica, sans-serif;
            background-image: var(--color-gradient);
            color: var(--color-white);
            text-align: center;
        }

        * {
            margin: 0;
            padding: 0;
        }

        .img_logo_header {
            width: 45px;
        }

        .header,
        .navigation_header {
            display: flex;
            flex-direction: row;
            align-items: center;
        }

        .header {
            background-color: var(--color-green);
            box-shadow: 1px 1px 4px var(--color-green2);
            height: 56px;
            justify-content: space-between;
            padding: 0 5%;
        }

        .navigation_header {
            gap: 48px;
        }

        .navigation_header a {
            text-decoration: none;
            color: var(--color-white);
            font-weight: bold;
        }

        .active {
            background-color: var(--color-green2);
            padding: 10px;
            border-radius: 10px;
        }

        .table-bg {
            background: rgba(0, 0, 0, 0.3);
            border-radius: 15px 15px 0 0;
        }
    </style>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
        google.charts.load('current', {'packages': ['corechart']});
        google.charts.setOnLoadCallback(drawChart);

        function drawChart() {
            var data = google.visualization.arrayToDataTable([
                ["Resultado", "Quantidade"],
                ["Greens", <?php echo $relatorio_bot[1] ?>],
                ["Reds", <?php echo $relatorio_bot[2] ?>]
            ]);
            var options = {
                title: 'Greens X Reds',
                backgroundColor: ''
            };
            var chart = new google.visualization.PieChart(document.getElementById('piechart'));
            chart.draw(data, options);
        }
    </script>
</head>
<body id="body">
<div class="header" id="header">
    <div class="logo_header">
        <img scr="robo.png" class="img_logo_header" alt="Logo Greenzord">
    </div>
    <div class="navigation_header" id="navigation_header">
        <a href="index.php">Home</a>
        <a href="relatorio.php">Relatorio</a>
        <a href="lista_bots.php">Bots</a>
        <a href="#" class="active">
            <?php
            echo $nome;
            ?>
        </a>
        <a href="criar_bot.php">Adicionar Bot</a>
    </div>
    <div class="navigation_header" id="navigation_header">
        <?php
        echo "<a>$logado</a>"
        ?>
        <?php
        echo "<a>R$ $saldo_usuario</a>"
        ?>
        <a href="sair.php">Sair</a>
    </div>
</div>
<br>
<h1>Relatório</h1>
<div class="m-5">
    <table class="table table-bg text-white">
        <thead>
        <tr>
            <th scope="col">Total Apostas</th>
            <th scope="col">Abertas</th>
            <th scope="col">Greens</th>
            <th scope="col">Reds</th>
            <th scope="col">Lucro</th>
        </tr>
        </thead>
        <tbody>
        <?php
        echo "<tr>";
        echo "<td>" . $relatorio_bot[4] . "</td>";
        echo "<td>" . $relatorio_bot[5] . "</td>";
        echo "<td>" . $relatorio_bot[1] . "</td>";
        echo "<td>" . $relatorio_bot[2] . "</td>";
        echo "<td>" . $relatorio_bot[3] . "</td>";
        echo "<tr>";
        ?>
        </tbody>
    </table>
</div>

<center>
    <?php
    if($relatorio_bot[4]>0){
        echo "<div id='piechart' style ='width: 450px; height: 250px;' ></div>";
    }
    ?>

</center>
<br>
<h1>Lista de Apostas do Bot
    <?php
    echo $nome;
    ?>
</h1>
<div class="m-5">
    <table class="table table-bg text-white">
        <thead>
        <tr>
            <th scope="col">Data</th>
            <th scope="col">Casa</th>
            <th scope="col">X</th>
            <th scope="col">Fora</th>
            <th scope="col">Mercado</th>
            <th scope="col">Odd</th>
            <th scope="col">Aposta</th>
            <th scope="col">Retorno</th>
            <th scope="col">Situação</th>
        </tr>
        </thead>
        <tbody>
        <?php
        foreach ($apostas_feitas as $aposta) {
            echo "<tr>";
            echo "<td>" . $aposta[8] . "</td>";
            echo "<td>" . $aposta[6] . "</td>";
            echo "<td>x</td>";
            echo "<td>" . $aposta[7] . "</td>";
            if ($aposta[1] == "casaapo") {
                echo "<td>Casa</td>";
            }
            elseif ($aposta[1] == "foraapo") {
                echo "<td>Fora</td>";
            }
            elseif ($aposta[1] == "favapo") {
                echo "<td>Favorito</td>";
            }
            elseif ($aposta[1] == "zebraapo") {
                echo "<td>Zebra</td>";
            }
            echo "<td>" . $aposta[3] . "</td>";
            echo "<td>" . $aposta[2] . "</td>";
            echo "<td>" . $aposta[4] . "</td>";
            echo "<td>" . $aposta[5] . "</td>";
            echo "<tr>";
        }
        ?>
        </tbody>
    </table>
</div>
</body>
</html>