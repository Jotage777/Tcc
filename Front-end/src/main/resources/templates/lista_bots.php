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

if(!empty($_GET['search']))
{
    $data = $_GET['search'];
    $urlbots = "http://127.0.0.1:5000/greenzord/nomes/" . $resultado_id . "/2/" . $data;
    $resultado_bots = json_decode(file_get_contents($urlbots));
}
else{
    $urlbots = "http://127.0.0.1:5000/greenzord/5/1/" . $resultado_id;
    $resultado_bots = json_decode(file_get_contents($urlbots));
}

$saldo = "http://127.0.0.1:5000/greenzord/4/3/" . $resultado_id;
$saldo_usuario = json_decode(file_get_contents($saldo));

//    var_dump($resultado_bots);
?>

<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <title>ListaBot</title>
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

        .box-search {
            display: flex;
            justify-content: center;
            gap: 0.25%;
        }
    </style>
</head>
<body id="body">
<div class="header" id="header">
    <div class="logo_header">
        <img scr="robo.png" class="img_logo_header" alt="Logo Greenzord">
    </div>
    <div class="navigation_header" id="navigation_header">
        <a href="index.php">Home</a>
        <a href="relatorio.php">Relatorio</a>
        <a href="#" class="active">Bots</a>
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
<h1>Lista de Bots</h1>
<div class="box-search">
    <input type="search" class="form-control w-25" placeholder="Pesquisar" id="pesquisar">
    <button onclick="searchData()" class="btn btn-success">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-search"
             viewBox="0 0 16 16">
            <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
        </svg>
    </button>
</div>
<div class="m-5">
    <table class="table table-bg text-white">
        <thead>
        <tr>
            <th scope="col">#</th>
            <th scope="col">Nome</th>
            <th scope="col">Time para Apostar</th>
            <th scope="col">Time para Analisar</th>
            <th scope="col">Responsabilidade</th>
            <th scope="col">Intervalo Odd</th>
            <th scope="col">Intervalo de Jogo</th>
            <th scope="col">Finalizações</th>
            <th scope="col">Posse</th>
            <th scope="col">...</th>
            <th scope="col">Ati/Des</th>
        </tr>
        </thead>
        <tbody>
        <?php
        foreach ($resultado_bots as $bot) {
            echo "<tr>";
            echo "<td>1</td>";
            echo "<td>" . $bot[1] . "</td>"; //nome
            if ($bot[12] == "casaapo") {
                echo "<td>Casa</td>";
            }
            elseif ($bot[12] == "foraapo") {
                echo "<td>Fora</td>";
            }
            elseif ($bot[12] == "favapo") {
                echo "<td>Favorito</td>";
            }
            elseif ($bot[12] == "zebraapo") {
                echo "<td>Zebra</td>";
            }
            if ($bot[13] == "casaesta") {
                echo "<td>Casa</td>";
            }
            elseif ($bot[13] == "foraesta") {
                echo "<td>Fora</td>";
            }
            elseif ($bot[13] == "favesta") {
                echo "<td>Favorito</td>";
            }
            elseif ($bot[13] == "zebraesta") {
                echo "<td>Zebra</td>";
            }
            echo "<td>" . $bot[2] . "</td>"; //responsabilidade
            echo "<td>" . $bot[3] . " ~ " . $bot[4] . "</td>"; //intervalo odd
            echo "<td>" . $bot[5] . " ~ " . $bot[6] . "</td>"; //intervalo jogo
            echo "<td>" . $bot[7] . " ~ " . $bot[8] . "</td>"; //finalizações
            echo "<td>" . $bot[9] . " ~ " . $bot[10] . "</td>"; //posse de bola
            echo "<td>
                    <a class='btn btn-primary btn-sm' href='relabot.php?id=$bot[0]?$bot[1]'>
                    <svg xmlns='http://www.w3.org/2000/svg' width='16' height='16' fill='currentColor' class='bi bi-clipboard-data' viewBox='0 0 16 16'>
                        <path d='M4 11a1 1 0 1 1 2 0v1a1 1 0 1 1-2 0v-1zm6-4a1 1 0 1 1 2 0v5a1 1 0 1 1-2 0V7zM7 9a1 1 0 0 1 2 0v3a1 1 0 1 1-2 0V9z'/>
                        <path d='M4 1.5H3a2 2 0 0 0-2 2V14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V3.5a2 2 0 0 0-2-2h-1v1h1a1 1 0 0 1 1 1V14a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V3.5a1 1 0 0 1 1-1h1v-1z'/>
                        <path d='M9.5 1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-3a.5.5 0 0 1-.5-.5v-1a.5.5 0 0 1 .5-.5h3zm-3-1A1.5 1.5 0 0 0 5 1.5v1A1.5 1.5 0 0 0 6.5 4h3A1.5 1.5 0 0 0 11 2.5v-1A1.5 1.5 0 0 0 9.5 0h-3z'/>
                    </svg>
                    </a>
                    <a class='btn btn-success btn-sm' href='editbot.php?id=$bot[0]'>
                    <svg xmlns='http://www.w3.org/2000/svg' width='16' height='16' fill='currentColor' class='bi bi-pencil' viewBox='0 0 16 16'>
                        <path d='M12.146.146a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1 0 .708l-10 10a.5.5 0 0 1-.168.11l-5 2a.5.5 0 0 1-.65-.65l2-5a.5.5 0 0 1 .11-.168l10-10zM11.207 2.5 13.5 4.793 14.793 3.5 12.5 1.207 11.207 2.5zm1.586 3L10.5 3.207 4 9.707V10h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.293l6.5-6.5zm-9.761 5.175-.106.106-1.528 3.821 3.821-1.528.106-.106A.5.5 0 0 1 5 12.5V12h-.5a.5.5 0 0 1-.5-.5V11h-.5a.5.5 0 0 1-.468-.325z'/>
                    </svg>
                    </a>
                    <a class='btn btn-danger btn-sm' href='deletebot.php?id=$bot[0]'>
                    <svg xmlns='http://www.w3.org/2000/svg' width='16' height='16' fill='currentColor' class='bi bi-trash-fill' viewBox='0 0 16 16'>
                        <path d='M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1H2.5zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5zM8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5zm3 .5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 1 0z'/>
                    </svg>
                </td>";
            if($bot[11]=="0"){
                echo "<td>
                        </a>
                        <a class='btn btn-success btn-sm' href='ativado.php?id=$bot[0]'>
                        <svg xmlns='http://www.w3.org/2000/svg' width='16' height='16' fill='currentColor' class='bi bi-check-square' viewBox='0 0 16 16'>
                            <path d='M14 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12zM2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z'/>
                            <path d='M10.97 4.97a.75.75 0 0 1 1.071 1.05l-3.992 4.99a.75.75 0 0 1-1.08.02L4.324 8.384a.75.75 0 1 1 1.06-1.06l2.094 2.093 3.473-4.425a.235.235 0 0 1 .02-.022z'/>
                        </svg>
                        </a>
                    </td>";
            }
            elseif ($bot[11]=="1"){
                echo "<td>
                        </a>
                        <a class='btn btn-success btn-sm' href='ativado.php?id=$bot[0]'>
                        <svg xmlns='http://www.w3.org/2000/svg' width='16' height='16' fill='currentColor' class='bi bi-check-square-fill' viewBox='0 0 16 16'>
                            <path d='M2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2zm10.03 4.97a.75.75 0 0 1 .011 1.05l-3.992 4.99a.75.75 0 0 1-1.08.02L4.324 8.384a.75.75 0 1 1 1.06-1.06l2.094 2.093 3.473-4.425a.75.75 0 0 1 1.08-.022z'/>
                        </svg>
                        </a>
                    </td>";
            }
            echo "<tr>";
        }
        ?>
        </tbody>
    </table>
</div>
</body>
<script>
    var search = document.getElementById('pesquisar');

    search.addEventListener("keydown", function (event) {
        if (event.key == "Enter") {
            searchData();
        }
    });

    function searchData() {
        window.location = 'lista_bots.php?search=' + search.value;
    }
</script>
</html>