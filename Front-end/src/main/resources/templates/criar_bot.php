<?php
    session_start();
    if(!isset($_SESSION['username']) == true && (!isset($_SESSION['password']) == true)){
        unset($_SESSION['username']);
        unset($_SESSION['password']);
        header('Location: login.php');
    }

    $logado = $_SESSION['username'];

    $urlid = "http://127.0.0.1:5000/greenzord/4/2/" . $logado;
    $resultado_id = json_decode(file_get_contents($urlid));

    $saldo = "http://127.0.0.1:5000/greenzord/4/3/" . $resultado_id;
    $saldo_usuario = json_decode(file_get_contents($saldo));

    if(isset($_POST['submit'])) {

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
            "ativado" => "1",
            "username" => $logado
        );

        $json = json_encode($dados);

        $url = "http://127.0.0.1:5000/greenzord/bots";

        $ch = curl_init($url);
        curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");
        curl_setopt($ch, CURLOPT_POSTFIELDS, $json);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_HTTPHEADER, array(
                'Content-Type: application/json',
                'Content-Length: ' . strlen($json))
        );

        $jsonRet = json_decode(curl_exec($ch));
    }
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
            padding: 5px;
            border-radius: 10px;
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
            padding: 5px;
        }
        legend{
            border: 1px solid #fff;
            padding: 8px;
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
            echo "<a>R$ $saldo_usuario</a>"
            ?>
            <a href="sair.php">Sair</a>
        </div>
    </div>
    <div class="content" id="content">
        <form action="criar_bot.php" method="POST">
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
                <!-- Entrada da odd aceita pelo bot -->
                <p>Odds:</p>
                <div class="inputBox">
                    <label for="oddmin">de:</label>
                    <input type="number" step="0.01" name="oddmin" id="oddmin" class="inputBotIntervalo" value="0.0" min="0" max="999.99" required>
                    <label for="oddmax">á:</label>
                    <input type="number" step="0.01" name="oddmax" id="oddmax" class="inputBotIntervalo" value="999.99" min="0" max="999.99" required>
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
                    <input type="number" name="tempomin" id="tempomin" class="inputBotIntervalo" value="0" min="0" max="99" required>
                    <label for="tempomin">á:</label>
                    <input type="number" name="tempomax" id="tempomax" class="inputBotIntervalo" value="99" min="0" max="99" required>
                </div>
                <!-- Finalizações do time ou ambos no jogo todo -->
                <p>Finalizações:</p>
                <div class="inputBox">
                    <label for="finamin">de:</label>
                    <input type="number" name="finamin" id="finamin" class="inputBotIntervalo" value="0" min="0" max="99" required>
                    <label for="finamax">á:</label>
                    <input type="number" name="finamax" id="finamax" class="inputBotIntervalo" value="99" min="0" max="99" required>
                </div>
                <!-- Adicionar posse de bola minima e maxima -->
                <p>Posse de Bola:</p>
                <div class="inputBox">
                    <label for="possemin">de:</label>
                    <input type="number" name="possemin" id="possemin" class="inputBotIntervalo" value="0" min="0" max="100" required>
                    <label for="possemax">á:</label>
                    <input type="number" name="possemax" id="possemax" class="inputBotIntervalo" value="100" min="0" max="100" required>
                </div>
                <br>
                <input type="submit" name="submit" id="submit" value="Adicionar">
            </fieldset>
        </form>
    </div>
</body>
</html>