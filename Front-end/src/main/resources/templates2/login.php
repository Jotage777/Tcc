<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Login</title>
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
        .navigation_header a{
            text-decoration: none;
            color: var(--color-white);
            font-weight: bold;
        }
        .content{
            display: block;
            background-color: rgba( 0,0,0,0.5);
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%,-50%);
            text-align: center;
            padding: 75px;
            border-radius: 15px;
        }
        .inputSubmit{
            position: absolute;
            text-decoration: none;
            color: white;
            border: 1px solid white;
            background-image: var(--color-gradient);
            padding: 5px;
            border-radius: 5px;
            transform: translate(-50%,-50%);
            width: 35%;
        }
        .inputSubmit:hover{
            cursor: pointer;
        }
    </style>
</head>
<body id="body">
    <div class="header" id="header">
        <div class="logo_header">
            <img scr="robo.png" class="img_logo_header" alt="Logo Greenzord">
        </div>
        <div class="navigation_header" id="navigation_header">
            <a>O robô para automatizar suas apostas esportivas</a>
        </div>
    </div>
    <div class="content" id="content">
        <h1>Login do Greenzord</h1>
        <br>
        <p>Informe seu usuario e senha</p>
        <br>
        <form action="testLogin.php" method="POST">
            <input type="text"  placeholder="Digite seu Usuario" name="username" /></label>
            <br><br>
            <input type="password"  placeholder="Digite sua Senha" name="password" /></label>
            <br><br><br>
            <input class="inputSubmit" type="submit" name="submit" value="Login">
        </form>
    </div>
</body>
</html>