<?php
    session_start();
    if(!isset($_SESSION['username']) == true && (!isset($_SESSION['password']) == true)){
        unset($_SESSION['username']);
        unset($_SESSION['password']);
        header('Location: login.php');
    }
    $logado = $_SESSION['username'];

    $saldo = "http://127.0.0.1:5000/greenzord/4/3/" . $logado;
    $saldo_usuario = json_decode(file_get_contents($saldo));
?>

<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <title>Relatorio</title>
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
            text-align: center;
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
        .navigation_header_busca a{
            text-decoration: none;
            color: var(--color-white);
            font-weight: bold;
        }
        .table-bg{
            background: rgba(0, 0, 0, 0.3);
            border-radius: 15px 15px 0 0;
        }
        .box-search{
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
            <a href="#" class="active">Relatorio</a>
            <a href="lista_bots.php">Bots</a>
        </div>
        <div class="navigation_header" id="navigation_header">
            <?php
            echo "<a>$logado</a>"
            ?>
            <?php
            echo "<a>$saldo_usuario</a>"
            ?>
            <a href="sair.php">Sair</a>
        </div>
    </div>
    <h1>Relatório</h1>
    <div class="box-search">
        <input type="search" class="form-control w-25" placeholder="Pesquisar" id="pesquisar">
        <button onclick="searchData()" class="btn btn-success">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16">
                <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
            </svg>
        </button>
    </div>
    <div class="m-5">
        <table class="table table-bg text-white">
            <thead>
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">Mercado</th>
                    <th scope="col">Responsabilidade</th>
                    <th scope="col">Odd</th>
                    <th scope="col">Bot</th>
                    <th scope="col">Campeonato</th>
                    <th scope="col">Casa</th>
                    <th scope="col">1</th>
                    <th scope="col">X</th>
                    <th scope="col">2</th>
                    <th scope="col">Fora</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <th scope="row">1</th>
                    <td>Vitoria Mandante</td>
                    <td>R$5,00</td>
                    <td>2.00</td>
                    <td>Mais Finalizações</td>
                    <td>Carioca</td>
                    <td>Flamengo</td>
                    <td>2</td>
                    <td>x</td>
                    <td>0</td>
                    <td>Fluminense</td>
                </tr>
                <tr>
                    <th scope="row">2</th>
                    <td>Vitoria Visitante</td>
                    <td>R$5,00</td>
                    <td>2.50</td>
                    <td>Mais Finalizações</td>
                    <td>Paulista</td>
                    <td>São Paulo</td>
                    <td>1</td>
                    <td>x</td>
                    <td>2</td>
                    <td>Palmeiras</td>
                </tr>
            </tbody>
        </table>
    </div>
</body>
<script>
    var search = document.getElementById('pesquisar');

    search.addEventListener("keydown", function (event){
        if (event.key == "Enter"){
            searchData();
        }
    });

    function searchData(){
        window.location = 'relatorio.php?search='+search.value;
    }
</script>
</html>