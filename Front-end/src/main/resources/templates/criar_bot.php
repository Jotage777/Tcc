<?php
    session_start();
    if(!isset($_SESSION['username']) == true && (!isset($_SESSION['password']) == true)){
        unset($_SESSION['username']);
        unset($_SESSION['password']);
        header('Location: login.php');
    }
    $logado = $_SESSION['username'];
//    if(isset($_POST['submit'])){
//        print_r('Nome: ' . $_POST['nome']);
//        print_r('<br>');
//        print_r('Responsabilidade: ' . $_POST['responsa']);
//        print_r('<br>');
//        print_r('Oddmin: ' . $_POST['oddmin']);
//        print_r('<br>');
//        print_r('Oddmax: ' . $_POST['oddmax']);
//        print_r('<br>');
//        print_r('favapo: ' . $_POST['favapo']);
//        print_r('<br>');
//        print_r('zebraapo: ' . $_POST['zebraapo']);
//        print_r('<br>');
//        print_r('casaapo: ' . $_POST['casaapo']);
//        print_r('<br>');
//        print_r('foraapo: ' . $_POST['foraapo']);
//        print_r('<br>');
//        print_r('favesta: ' . $_POST['favesta']);
//        print_r('<br>');
//        print_r('zebraesta: ' . $_POST['zebraesta']);
//        print_r('<br>');
//        print_r('casaesta: ' . $_POST['casaesta']);
//        print_r('<br>');
//        print_r('foraesta: ' . $_POST['foraesta']);
//        print_r('<br>');
//        print_r('tempomin: ' . $_POST['tempomin']);
//        print_r('<br>');
//        print_r('tempomax: ' . $_POST['tempomax']);
//        print_r('<br>');
//        print_r('finamin: ' . $_POST['finamin']);
//        print_r('<br>');
//        print_r('finamax: ' . $_POST['finamax']);
//        print_r('<br>');
//    }
    if(isset($_POST['submit'])) {
        $dados = [
            "nome" => $_POST['nome'],
            "responsabilidade" => $_POST['responsa'],
            "odd_minima" => $_POST['oddmin'],
            "odd_maxima" => $_POST['oddmax'],
            "tempo_jogo_minimo" => $_POST['tempomin'],
            "tempo_jogo_maximo" => $_POST['tempomax'],
            "finalizacao_min" => $_POST['finamin'],
            "finalizacao_max" => $_POST['finamax'],
            "posse_bola_min" => $_POST[55],
            "posse_bola_max" => $_POST[75],
            "apostar" => $_POST['timeapo'],
            "analisar" => $_POST['timesta'],
        ];
        $json = json_decode($dados);
        $headers = [
            'Content-type: application/json',
            'Content-length:' . strlen($json),
        ];
        $context = stream_context_create([
            'http' => [
                'method' => 'POST',
                'header' => $headers,
                'content' => $json
            ],
        ]);
        $url = "http://127.0.0.1:5000/greenzord/bots";
        file_get_contents($url, false, $context);
        fopen($url, 'r', false, $context);
    };
?>

<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <title>AdicionarBot</title>
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
        .content{
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%,-50%);
            background-color: rgba( 0,0,0,0.5);
            text-align: center;
            padding: 8px;
            border-radius: 15px;
            width: 33%;
        }
        #submit{
            background-image: var(--color-gradient);
            width: 100%;
            border: 1px solid white;
            padding: 12px;
            color: white;
            font-size: 15px;
            cursor: pointer;
            border-radius: 10px;
        }
        fieldset{
            border: 3px solid #fff;
            padding: 8px;
        }
        legend{
            border: 1px solid #fff;
            padding: 10px;
            text-align: center;
            border-radius: 8px;
        }
        .inputBox{
            position: relative;
        }
        .inputBot{
            background: none;
            border: none;
            border-bottom: 1px solid white;
            outline: none;
            color: white;
            font-size: 12px;
            width: 100%;
        }
        .inputBotIntervalo{
            background: none;
            border: none;
            border-bottom: 1px solid white;
            outline: none;
            color: white;
            font-size: 12px;
        }
        .labelInput{
            position: absolute;
            top: 0px;
            left: 0px;
            pointer-events: none;
            transition: .5s;
        }
        .inputBot:focus ~ .labelInput,
        .inputBot:valid ~ .labelInput{
            top: -20px;
            font-size: 12px;
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
    <div class="content" id="content">
        <form action="" method="GET">
            <fieldset>
                <legend><b>Adicionar Bot</b></legend>
                <br><br>
                <!-- Entrada nome do bot -->
                <div class="inputBox">
                    <input type="text" name="nome" id="nome" class="inputBot" required>
                    <label for="nome" class="labelInput">Nome do Bot</label>
                </div>
                <br>
                <!-- Entrada responsabilidade da aposta do bot -->
                <div class="inputBox">
                    <input type="number" name="responsa" id="responsa" class="inputBot" required>
                    <label for="responsa" class="labelInput">Responsabilidade</label>
                </div>
                <br>
                <!-- Entrada da odd aceita pelo bot -->
                <p>Odds:</p>
                <div class="inputBox">
                    <label for="oddmin">de:</label>
                    <input type="number" name="oddmin" id="oddmin" class="inputBotIntervalo" required>
                    <label for="oddmax">á:</label>
                    <input type="number" name="oddmax" id="oddmax" class="inputBotIntervalo" required>
                </div>
                <br>
                <!-- Times a serem apostados -->
                <p>Times (Para Apostar):</p>
                <input type="radio" id="favapo" name="timapo" value="favapo" required>
                <label for="casa">Favorito</label>
                <br>
                <input type="radio" id="zebraapo" name="timapo" value="zebraapo" required>
                <label for="fora">Zebra</label>
                <br>
                <input type="radio" id="casaapo" name="timapo" value="casaapo" required>
                <label for="ambos">Casa</label>
                <br>
                <input type="radio" id="foraapo" name="timapo" value="foraapo" required>
                <label for="ambos">Fora</label>
                <br>
                <!-- Times a serem analisados -->
                <p>Times (Para Estatísticas):</p>
                <input type="radio" id="favesta" name="timesta" value="favesta" required>
                <label for="casa">Favorito</label>
                <br>
                <input type="radio" id="zebraesta" name="timesta" value="zebraesta" required>
                <label for="fora">Zebra</label>
                <br>
                <input type="radio" id="casaesta" name="timesta" value="casaesta" required>
                <label for="casa">Casa</label>
                <br>
                <input type="radio" id="foraesta" name="timesta" value="foraesta" required>
                <label for="fora">Fora</label>
                <br>
                <!-- Tempo de jogo a ser apostado -->
                <p>Tempo de Jogo(0 a 90):</p>
                <div class="inputBox">
                    <label for="tempomin">de:</label>
                    <input type="number" name="tempomin" id="tempomin" class="inputBotIntervalo" required>
                    <label for="tempomin">á:</label>
                    <input type="number" name="tempomax" id="tempomax" class="inputBotIntervalo" required>
                </div>
                <br>
                <!-- Finalizações do time ou ambos no jogo todo -->
                <p>Finalizações:</p>
                <div class="inputBox">
                    <label for="finamin">de:</label>
                    <input type="number" name="finamin" id="finamin" class="inputBotIntervalo" required>
                    <label for="finamax">á:</label>
                    <input type="number" name="finamax" id="finamax" class="inputBotIntervalo" required>
                </div>
                <br>
                <!-- Adicionar posse de bola minima e maxima -->
                <input type="submit" name="submit" id="submit" value="Adicionar">
            </fieldset>
        </form>
    </div>
</body>
</html>

http://127.0.0.1:5000/greenzord/bots