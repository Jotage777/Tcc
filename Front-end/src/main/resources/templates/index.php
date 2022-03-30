<?php
    session_start();
    if(!isset($_SESSION['username']) == true && (!isset($_SESSION['password']) == true)){
        unset($_SESSION['username']);
        unset($_SESSION['password']);
        header('Location: login.php');
    }
    $logado = $_SESSION['username'];
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Greenzord</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <style>
        body{
            font-family: Arial, Helvetica, sans-serif;
            background-image: linear-gradient(45deg,green,cyan);
            color: white;
        }
        section ul{
            list-style: none;
        }
        section ul li{
            display: inline-block;
            margin-right: 10px;
        }
        section ul li a{
            text-decoration: none;
        }
        footer{
            clear: both;
            top: 98%;
            transform: translate(0%, 0%);
            position: absolute;
        }
        a:link{
            text-decoration:none;
            color:white;
        }
        a:link {color:#FFFFFF;}
        d-flex{

        }
    </style>
</head>
<body>

    <!-- NavBar -->

    <nav class="navbar navbar-expand-lg" style="background-color: rgba( 0,0,0,0.15);">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">
                <img src="robo.png" alt="Logo Greenzord" width="30" height="24" class="d-inline-block align-text-top">
                Greenzord
            </a>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a class="nav-link" href="relatorio.php">Relatorio</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="criar_bot.php">Adicionar bot</a>
                    </li>
                    <?php
                        echo "<a>$logado</a>"
                    ?>
                    <a>Saldo</a>
                    <div class="d-lg-flex">
                        <a class="btn btn-danger me-5" href='sair.php'>Sair</a>
                    </div>
                </ul>
            </div>

        </div>
    </nav>

    <!-- Detalhes -->

        <section>
            <div>
                <h1>Jogos ao vivo</h1>
            </div>
            <div>
                <h1>Bots criados</h1>
            </div>
        </section>

    <!-- Programadores -->

        <footer>
            Projeto de Tcc de João Gabriel e João Messias
        </footer>
    </div>
</body>
</html>