<?php
    session_start();
    if(!isset($_SESSION['username']) == true && (!isset($_SESSION['password']) == true)){
        unset($_SESSION['username']);
        unset($_SESSION['password']);
        header('Location: login.php');
    }
    $logado = $_SESSION['username'];
?>

<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
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
            height: 100vh;
        }
        .header_busca,
        .navigation_header_busca{
            display: flex;
            flex-direction: row;
            align-items: center;
        }
        .header_busca{
            background-color: var(--color-green);
            box-shadow: 1px 1px 4px var(--color-green2);
            height: 56px;
            padding: 0 5%;
        }
        .navigation_header_busca{
            gap: 48px;
        }
        .navigation_header_busca a{
            text-decoration: none;
            color: var(--color-white);
            font-weight: bold;
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
            <a href="criar_bot.php">Adicionar Bot</a>
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
    <div class="content" id="content">
        <h1>Relatório</h1>
        <div class="header_busca" id="header_busca">
            <div class="navigation_header_busca" id="navigation_header_busca">
                <form>
                    <a>Escolher Bot ou todos</a>
                    <a>Escolher Data ou todas</a>
                </form>
            </div>
        </div>
    </div>
    <div>
        <table class="table">
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

            </tbody>
        </table>
    </div>
</body>
</html>