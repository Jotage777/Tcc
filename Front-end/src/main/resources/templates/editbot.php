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

    $id = $_GET['id'];

    if(!empty($_GET['id'])) {
        $url = "http://127.0.0.1:5000/greenzord/5/2/".$id;
        $bot_edit = json_decode(file_get_contents($url));
        if($bot_edit != 0 and $bot_edit[14] == $resultado_id){
            $nome = $bot_edit[1];
            $responsabilidade = $bot_edit[2];
            $odd_minima = $bot_edit[3];
            $odd_maxima = $bot_edit[4];
            $tempo_jogo_minimo = $bot_edit[5];
            $tempo_jogo_maximo = $bot_edit[6];
            $finalizacao_min = $bot_edit[7];
            $finalizacao_max = $bot_edit[8];
            $posse_bola_min = $bot_edit[9];
            $posse_bola_max = $bot_edit[10];
            $apostar = $bot_edit[12];
            $analisar = $bot_edit[13];
            $ativado = $bot_edit[11];
        }
        else{
            header('Location: lista_bots.php');
        }
    }
    else{
        header('Location: lista_bots.php');
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
        #update{
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
        <form action="saveEdit.php" method="POST"
<!--        <form action="editbot.php" method="POST">-->
            <fieldset>
                <legend><b>Editar Bot</b></legend>
                <br><br>
                <!-- Entrada nome do bot -->
                <div class="inputBox">
                    <input type="text" name="nome" id="nome" class="inputBot" value="<?php echo $nome ?>" required>
                    <label for="nome" class="labelInput">Nome do Bot</label>
                </div>
                <br>
                <!-- Entrada responsabilidade da aposta do bot -->
                <div class="inputBox">
                    <input type="number" name="responsa" id="responsa" class="inputBot" value="<?php echo $responsabilidade ?>" required>
                    <label for="responsa" class="labelInput">Responsabilidade</label>
                </div>
                <!-- Entrada da odd aceita pelo bot -->
                <p>Odds:</p>
                <div class="inputBox">
                    <label for="oddmin">de:</label>
                    <input type="number" step="0.01" name="oddmin" id="oddmin" class="inputBotIntervalo" value="<?php echo $odd_minima ?>" min="0.01" max="999.99" required>
                    <label for="oddmax">á:</label>
                    <input type="number" step="0.01" name="oddmax" id="oddmax" class="inputBotIntervalo" value="<?php echo $odd_maxima ?>" min="0.01" max="999.99" required>
                </div>
                <br>
                <!-- Times a serem apostados -->
                <p>Times (Para Apostar):</p>
                <input type="radio" id="favapo" name="timapo" value="favapo" <?php echo $apostar == 'favapo' ? 'checked' : '' ?> required>
                <label for="casa">Favorito</label>
                <br>
                <input type="radio" id="zebraapo" name="timapo" value="zebraapo" <?php echo $apostar == 'zebraapo' ? 'checked' : '' ?> required>
                <label for="fora">Zebra</label>
                <br>
                <input type="radio" id="casaapo" name="timapo" value="casaapo" <?php echo $apostar == 'casaapo' ? 'checked' : '' ?> required>
                <label for="ambos">Casa</label>
                <br>
                <input type="radio" id="foraapo" name="timapo" value="foraapo" <?php echo $apostar == 'foraapo' ? 'checked' : '' ?> required>
                <label for="ambos">Fora</label>
                <br>
                <!-- Times a serem analisados -->
                <p>Times (Para Estatísticas):</p>
                <input type="radio" id="favesta" name="timesta" value="favesta" <?php echo $analisar == 'favesta' ? 'checked' : '' ?> required>
                <label for="casa">Favorito</label>
                <br>
                <input type="radio" id="zebraesta" name="timesta" value="zebraesta" <?php echo $analisar == 'zebraesta' ? 'checked' : '' ?> required>
                <label for="fora">Zebra</label>
                <br>
                <input type="radio" id="casaesta" name="timesta" value="casaesta" <?php echo $analisar == 'casaesta' ? 'checked' : '' ?> required>
                <label for="casa">Casa</label>
                <br>
                <input type="radio" id="foraesta" name="timesta" value="foraesta" <?php echo $analisar == 'foraesta' ? 'checked' : '' ?> required>
                <label for="fora">Fora</label>
                <br>
                <!-- Tempo de jogo a ser apostado -->
                <p>Tempo de Jogo(0 a 90):</p>
                <div class="inputBox">
                    <label for="tempomin">de:</label>
                    <input type="number" name="tempomin" id="tempomin" class="inputBotIntervalo" value="<?php echo $tempo_jogo_minimo ?>" min="0" max="99" required>
                    <label for="tempomin">á:</label>
                    <input type="number" name="tempomax" id="tempomax" class="inputBotIntervalo" value="<?php echo $tempo_jogo_maximo ?>" min="0" max="99" required>
                </div>
                <!-- Finalizações do time ou ambos no jogo todo -->
                <p>Finalizações:</p>
                <div class="inputBox">
                    <label for="finamin">de:</label>
                    <input type="number" name="finamin" id="finamin" class="inputBotIntervalo" value="<?php echo $finalizacao_min ?>" min="0" max="99" required>
                    <label for="finamax">á:</label>
                    <input type="number" name="finamax" id="finamax" class="inputBotIntervalo" value="<?php echo $finalizacao_max ?>" min="0" max="99" required>
                </div>
                <!-- Adicionar posse de bola minima e maxima -->
                <p>Posse de Bola:</p>
                <div class="inputBox">
                    <label for="possemin">de:</label>
                    <input type="number" name="possemin" id="possemin" class="inputBotIntervalo" value="<?php echo $posse_bola_min ?>" min="0" max="100" required>
                    <label for="possemax">á:</label>
                    <input type="number" name="possemax" id="possemax" class="inputBotIntervalo" value="<?php echo $posse_bola_max ?>" min="0" max="100" required>
                </div>
                <br>
                <input type="hidden" name="id" value="<?php echo $id ?>">
                <input type="submit" name="update" id="update" value="Salvar">
            </fieldset>
        </form>
    </div>
</body>
</html>