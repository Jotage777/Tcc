from contextlib import closing
import sqlite3


def criar_BD() -> None:
    with sqlite3.connect('Greenzord.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('PRAGMA foreign_keys = ON;')
            cursor.execute('''
                CREATE TABLE Campeonato(
                    id_campeonato INTEGER primary key AUTOINCREMENT ,
                    name VARCHAR(45) NOT NULL
                    )''')
            cursor.execute('''
                CREATE TABLE Times(
                    id_time INTEGER primary key AUTOINCREMENT ,
                    name VARCHAR(45) NOT NULL
                    )''')
            cursor.execute('''
                CREATE TABLE Jogos_Encerrados(
                    id_jogo VARCHAR (20) primary key ,
                    fk_id_casa INTEGER NOT NULL,
                    fk_id_campeonato INTEGER NOT NULL,
                    fk_id_fora INTEGER  NOT NULL ,
                    resultado_fora INTEGER NOT NULL ,
                    resultado_casa INTEGER NOT NULL ,
                    date VARCHAR(10) NOT NULL,
                    FOREIGN KEY(fk_id_casa) REFERENCES Times (id_time),
                    FOREIGN KEY(fk_id_fora) REFERENCES Times (id_time),
                    FOREIGN KEY(fk_id_campeonato) REFERENCES Campeonato (id_campeonato)
                    )''')
            cursor.execute('''
                CREATE TABLE Jogos_AoVivo(
                    id_jogo VARCHAR (20) primary key ,
                    time_casa VARCHAR (40) NOT NULL,
                    nome_campeonato VARCHAR (40) NOT NULL,
                    time_fora VARCHAR (20) NOT NULL ,
                    resultado_casa INTEGER NOT NULL ,
                    resultado_fora INTEGER NOT NULL ,
                    tempo INTEGER NOT NULL, 
                    date VARCHAR(10) NOT NULL,
                    posse_bola_casa INTEGER NOT NULL,
                    posse_bola_fora INTEGER  NOT NULL,
                    finalizacao_casa INTEGER NOT NULL ,
                    finalizacao_fora INTEGER NOT NULL ,
                    odd_casa FLOAT NOT NUll,
                    odd_fora FLOAT NOT NUll,
                    odd_empate FLOAT NOT NULL,
                    fk_id_campeonato INTEGER NOT NULL ,
                    FOREIGN KEY(fk_id_campeonato) REFERENCES Campeonato (id_campeonato)
                    )''')
            cursor.execute('''
                CREATE TABLE Usuario(
                    id_usuario INTEGER primary key AUTOINCREMENT ,
                    username VARCHAR(45) NOT NULL,
                    nome VARCHAR (45) NOT NULL ,
                    email VARCHAR (45) NOT NULL ,
                    data_Nascimento DATE NOT NULL,
                    saldo FLOAT NOT NULL,
                    senha VARCHAR (20) NOT NULL
                    )''')
            cursor.execute('''
                CREATE TABLE Bots(
                    id_bot INTEGER primary key AUTOINCREMENT ,
                    nome VARCHAR (45) NOT NULL ,
                    responsabilidade FLOAT NOT NULL ,
                    odd_minima FLOAT NOT NULL,
                    odd_maxima FLOAT NOT NULL,
                    tempo_jogo_minimo INTEGER NOT NULL,
                    tempo_jogo_maximo INTEGER NOT NULL,
                    finalizacao_min INTEGER NOT NULL,
                    finalizacao_max INTEGER NOT NULL,
                    posse_bola_min INTEGER NOT NULL,
                    posse_bola_max INTEGER NOT NULL,
                    ativado BIT NOT NULL,
                    apostar VARCHAR (10) NOT NULL ,
                    analisar VARCHAR (10) NOT NULL ,
                    fk_id_usuario INTEGER NOT NULL,
                    FOREIGN KEY(fk_id_usuario) REFERENCES Usuario (id_usuario)
                    )''')
            cursor.execute('''
                CREATE TABLE Apostas(
                    id_apostas INTEGER primary key AUTOINCREMENT ,
                    mercado VARCHAR(45) NOT NULL,
                    valor_apostado FLOAT NOT NULL,
                    odd_aposta FLOAT NOT NULL ,
                    retorno FLOAT NOT NULL ,
                    situacao VARCHAR (15) NOT NULL ,
                    time_casa VARCHAR (30) NOT NULL ,
                    time_fora VARCHAR (30) NOT NULL ,
                    data VARCHAR (30) NOT NULL ,
                    fk_id_bot INTEGER NOT NULL,
                    fk_id_jogos INTEGER NOT NULL ,
                    casa_fora INTEGER NOT NULL ,
                    fk_id_usuario INTEGER NOT NULL ,
                    nome_bot VARCHAR (30) NOT NULL ,
                    FOREIGN KEY(fk_id_bot) REFERENCES Bots(id_bot),
                    FOREIGN KEY(fk_id_jogos) REFERENCES Jogos(id_jogo),
                    FOREIGN KEY(fk_id_usuario) REFERENCES Usuario(id_usuario)
                    )''')
            cursor.execute('''
                CREATE TABLE Relatorio(
                    id_relatorio INTEGER primary key AUTOINCREMENT ,
                    greens INTEGER NOT NULL,
                    reds INTEGER NOT NULL,
                    lucro FLOAT NOT NULL,
                    total_apostas INTEGER NOT NULL,
                    apostas_abertas INTEGER NOT NULL,
                    fk_id_bot INTEGER NOT NULL,
                    FOREIGN KEY(fk_id_bot) REFERENCES Bots(id_bot)
                    )''')
            conn.commit()


def add_campeonato(campeonato: str) -> int:
    with sqlite3.connect('Greenzord.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('PRAGMA foreign_keys = ON;')
            cursor.execute('''SELECT id_campeonato FROM Campeonato WHERE name = ?''', (campeonato,))
            result = cursor.fetchone()
            if result is None:
                cursor.execute('''INSERT INTO Campeonato (name) VALUES(?)''', (campeonato,))
                cursor.execute('''SELECT id_campeonato FROM Campeonato WHERE name = ?''', (campeonato,))
                result = cursor.fetchone()
                conn.commit()
                return result[0]
            else:
                conn.commit()
                return result[0]


def add_times(time: str) -> int:
    with sqlite3.connect('Greenzord.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('PRAGMA foreign_keys = ON;')
            cursor.execute('''SELECT id_time FROM Times WHERE name = ?''', (time,))
            result = cursor.fetchone()
            if result is None:
                cursor.execute('''INSERT INTO Times (name) VALUES(?)''', (time,))
                cursor.execute('''SELECT id_time FROM Times WHERE name = ?''', (time,))
                result = cursor.fetchone()
                conn.commit()
                return result[0]
            else:
                conn.commit()
                return result[0]


def consultar_jogos(id: str) -> int:
    with sqlite3.connect('Greenzord.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('PRAGMA foreign_keys = ON;')
            cursor.execute('''SELECT id_jogo FROM Jogos WHERE id_jogo = ?''', (id,))
            result = cursor.fetchone()
            if result is None:
                print("Não existe esse jogo na base de dados")
                conn.commit()
            else:
                conn.commit()


def add_jogos_aovivo(campeonato: str, id: str, casa: str, resultado_casa: int, fora: str, resultado_fora: int,
                     tempo: int, data: str, posse_casa: int, posse_fora: int, finalizacao_casa: int,
                     finalizacao_fora: int, odd_casa: float, odd_empate: float, odd_fora: float) -> int:
    with sqlite3.connect('Greenzord.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('PRAGMA foreign_keys = ON;')
            cursor.execute('''SELECT id_jogo FROM Jogos_AoVivo WHERE id_jogo = ?''', (id,))
            result = cursor.fetchone()
            if result is None:
                fk_id_campeonato = add_campeonato(campeonato)
                cursor.execute('''INSERT INTO Jogos_AoVivo (id_jogo, time_casa,nome_campeonato,time_fora, resultado_casa
                , resultado_fora, tempo, date, posse_bola_casa, posse_bola_fora, finalizacao_casa, finalizacao_fora, 
                odd_casa, odd_empate, odd_fora, fk_id_campeonato)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (
                    id, casa, campeonato, fora, resultado_casa, resultado_fora, tempo, data, posse_casa, posse_fora,
                    finalizacao_casa, finalizacao_fora, odd_casa, odd_empate, odd_fora, fk_id_campeonato))
                conn.commit()
            else:
                conn.commit()


def add_jogos_encerrados(campeonato: str, id: str, casa: str, resultado_casa: int, fora: str, resultado_fora: int,
                         data: str) -> int:
    with sqlite3.connect('Greenzord.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('PRAGMA foreign_keys = ON;')
            cursor.execute('''SELECT id_jogo FROM Jogos_Encerrados WHERE id_jogo = ?''', (id,))
            result = cursor.fetchone()
            if result is None:
                fk_id_campeonato = add_campeonato(campeonato)
                fk_id_casa = add_times(casa)
                fk_id_fora = add_times(fora)
                cursor.execute('''INSERT INTO Jogos_Encerrados (id_jogo, fk_id_casa, resultado_casa, fk_id_fora,
                resultado_fora, date, fk_id_campeonato)
                VALUES(?,?,?,?,?,?,?)''', (id, fk_id_casa, resultado_casa, fk_id_fora, resultado_fora, data,
                                           fk_id_campeonato))
                conn.commit()
            else:
                conn.commit()


def consultar_usuario(username: str) -> int:
    with sqlite3.connect('Greenzord.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('PRAGMA foreign_keys = ON;')
            cursor.execute('''SELECT * FROM Usuario WHERE username = ?''', (username,))
            result = cursor.fetchall()
            id = result[0][0]
            if id is None:
                print("Não existe esse username na base de dados")
                conn.commit()
            else:
                return id
                conn.commit()


def consultar_login(username: str, senha: str) -> int:
    with sqlite3.connect('Greenzord.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('PRAGMA foreign_keys = ON;')
            cursor.execute('''SELECT * FROM Usuario WHERE username = ?''', (username,))
            result = cursor.fetchall()
            if result[0][1] == username and result[0][6] == senha:
                return True
                conn.commit()
            else:
                return False
                conn.commit()


def consultar_usuario_saldo(id: int) -> int:
    with sqlite3.connect('Greenzord.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('PRAGMA foreign_keys = ON;')
            cursor.execute('''SELECT * FROM Usuario WHERE id_usuario = ?''', (id,))
            result = cursor.fetchall()
            saldo = result[0][5]
            if saldo is None:
                print("Não existe esse usuario na base de dados")
                conn.commit()
            else:
                return saldo
                conn.commit()


def atulizar_usuario(valor, id_usuario, tipo):
    with sqlite3.connect('Greenzord.db') as conn:
        if tipo == 1:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''UPDATE Usuario SET username = ? WHERE id_usuario =?''', (valor, id_usuario,))
                conn.commit()
        elif tipo == 2:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''UPDATE Usuario SET nome = ? WHERE id_usuario =?''', (valor, id_usuario,))
                conn.commit()
        elif tipo == 3:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''UPDATE Usuario SET email = ? WHERE id_usuario =?''', (valor, id_usuario,))
                conn.commit()
        elif tipo == 4:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''UPDATE Usuario SET data_Nascimento = ? WHERE id_usuario =?''', (valor, id_usuario,))
                conn.commit()
        elif tipo == 5:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''UPDATE Usuario SET saldo = ? WHERE id_usuario =?''', (valor, id_usuario,))
                conn.commit()
        elif tipo == 6:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''UPDATE Usuario SET senha = ? WHERE id_usuario =?''', (valor, id_usuario,))
                conn.commit()


def add_usuario(username: str, nome: str, email: str, data_Nascimento: str, saldo: float, senha: str) -> int:
    with sqlite3.connect('Greenzord.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('PRAGMA foreign_keys = ON;')
            cursor.execute('''SELECT username FROM Usuario WHERE username = ?''', (username,))
            result = cursor.fetchone()
            if result is None:
                cursor.execute('''INSERT INTO Usuario (username , nome , email , data_Nascimento , saldo,senha)
                VALUES(?,?,?,?,?,?)''', (username, nome, email, data_Nascimento, saldo, senha))
                conn.commit()
            else:

                conn.commit()


def consultar_bots(nome: str) -> int:
    with sqlite3.connect('Greenzord.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('PRAGMA foreign_keys = ON;')
            cursor.execute('''SELECT * FROM Bots WHERE nome = ?''', (nome,))
            result = cursor.fetchone()
            id_bot = result[0]
            if id_bot is None:
                print("Não existe esse bot na base de dados")
                conn.commit()
            else:
                return id_bot
                conn.commit()


def consultar_usuario_bots(id_bot) -> int:
    with sqlite3.connect('Greenzord.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('PRAGMA foreign_keys = ON;')
            cursor.execute('''SELECT * FROM Bots WHERE id_bot = ?''', (id_bot,))
            result = cursor.fetchone()
            id_usuario = result[14]
            if id_usuario is None:
                print("Não existe esse bot na base de dados")
                conn.commit()
            else:
                return id_usuario
                conn.commit()


def add_bots(nome: str, responsabilidade: float, odd_minima: float, odd_maxima: float, tempo_jogo_minimo: int,
             tempo_de_jogo_maximo: int, finalizacao_min: int, finalizacao_max: int, posse_bola_min: int,
             posse_de_bola_max: int, ativado: bool, apostar: str, analisar: str, username: str) -> int:
    with sqlite3.connect('Greenzord.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('PRAGMA foreign_keys = ON;')
            cursor.execute('''SELECT id_bot FROM Bots WHERE nome = ?''', (nome,))
            result = cursor.fetchone()
            if result is None:
                fk_id_usuario = consultar_usuario(username)
                cursor.execute('''INSERT INTO Bots (nome, responsabilidade, odd_minima, odd_maxima, tempo_jogo_minimo,
                tempo_jogo_maximo, finalizacao_min, finalizacao_max, posse_bola_min, posse_bola_max,
                ativado, apostar, analisar, fk_id_usuario)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (nome, responsabilidade, odd_minima, odd_maxima,
                                                         tempo_jogo_minimo, tempo_de_jogo_maximo, finalizacao_min,
                                                         finalizacao_max, posse_bola_min, posse_de_bola_max, ativado,
                                                         apostar, analisar, fk_id_usuario))
                conn.commit()
            else:
                conn.commit()


def atulizar_bots(valor, id_bot, tipo):
    with sqlite3.connect('Greenzord.db') as conn:
        if tipo == 1:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''UPDATE Bots SET nome = ? WHERE id_bot =?''', (valor, id_bot,))
                conn.commit()
        elif tipo == 2:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''UPDATE Bots SET responsabilidade = ? WHERE id_bot =?''', (valor, id_bot,))
                conn.commit()
        elif tipo == 3:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''UPDATE Bots SET odd_minima = ? WHERE id_bot =?''', (valor, id_bot,))
                conn.commit()
        elif tipo == 4:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''UPDATE Bots SET odd_maxima = ? WHERE id_bot =?''', (valor, id_bot,))
                conn.commit()
        elif tipo == 5:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''UPDATE Bots SET tempo_jogo_minimo = ? WHERE id_bot =?''', (valor, id_bot,))
                conn.commit()
        elif tipo == 6:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''UPDATE Bots SET tempo_jogo_maximo  = ? WHERE id_bot =?''', (valor, id_bot,))
                conn.commit()
        elif tipo == 7:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''UPDATE Bots SET finalizacao_min   = ? WHERE id_bot =?''', (valor, id_bot,))
                conn.commit()
        elif tipo == 8:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''UPDATE Bots SET finalizacao_max = ? WHERE id_bot =?''', (valor, id_bot,))
                conn.commit()
        elif tipo == 9:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''UPDATE Bots SET posse_bola_min = ? WHERE id_bot =?''', (valor, id_bot,))
                conn.commit()
        elif tipo == 10:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''UPDATE Bots SET posse_bola_max = ? WHERE id_bot =?''', (valor, id_bot,))
                conn.commit()
        elif tipo == 11:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''UPDATE Bots SET ativado = ? WHERE id_bot =?''', (valor, id_bot,))
                conn.commit()
        elif tipo == 12:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''UPDATE Bots SET apostar = ? WHERE id_bot =?''', (valor, id_bot,))
                conn.commit()
        elif tipo == 13:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''UPDATE Bots SET analisar = ? WHERE id_bot =?''', (valor, id_bot,))
                conn.commit()


def consultar_aposta(id_aposta) -> int:
    with sqlite3.connect('Greenzord.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('PRAGMA foreign_keys = ON;')
            cursor.execute('''SELECT id_aposta FROM Apostas WHERE id_aposta = ?''', (id_aposta,))
            result = cursor.fetchone()
            if result is None:
                print("Não existe essa aposta na base de dados")
                conn.commit()
            else:
                conn.commit()


def consultar_aposta_bot(id, tipo) -> int:
    with sqlite3.connect('Greenzord.db') as conn:
        if tipo == 1:
            with closing(conn.cursor()) as cursor:
                cursor.execute('''SELECT * FROM Apostas WHERE fk_id_bot=?''', (id,))
                result = cursor.fetchall()
                print(result)
                return result
        elif tipo == 2:
            situacao = "aberto"
            with closing(conn.cursor()) as cursor:
                cursor.execute('''SELECT * FROM Apostas WHERE situacao =? AND fk_id_usuario=?''', (situacao, id,))
                result = cursor.fetchall()
                print(result)
                return result


def verificar_apostas(id_jogo, id_bot) -> int:
    try:
        with sqlite3.connect('Greenzord.db') as conn:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''SELECT * FROM Apostas WHERE fk_id_bot = ?''', (id_bot,))
                result = cursor.fetchall()
                for i in range(len(result)):
                    if result[i][9] == id_bot and result[i][10] == id_jogo:
                        return True
                return False
    except:
        return False


def add_apostas(mercado: str, valor_apostado: float, odd_aposta: float, retorno: float, situacao: str, time_casa: str,
                time_fora: str, data: str, id_bot: str, id_jogo: str, casa_fora: int, id_usuario: int,nome_bot:str) -> int:
    with sqlite3.connect('Greenzord.db') as conn:
        with closing(conn.cursor()) as cursor:
            fk_id_bot = id_bot
            fk_id_jogos = id_jogo
            fk_id_usuario = id_usuario
            cursor.execute('''INSERT INTO Apostas (mercado, valor_apostado, odd_aposta,retorno,situacao,time_casa,time_fora,data,fk_id_bot,fk_id_jogos,casa_fora,fk_id_usuario,nome_bot)
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)''', (
            mercado, valor_apostado, odd_aposta, retorno, situacao, time_casa, time_fora, data, fk_id_bot, fk_id_jogos,
            casa_fora, fk_id_usuario,nome_bot))
            conn.commit()


def atulizar_aposta(valor, id_aposta, tipo):
    with sqlite3.connect('Greenzord.db') as conn:
        if tipo == 1:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''UPDATE Apostas  SET situacao = ? WHERE id_apostas =?''', (valor, id_aposta,))
                conn.commit()
        elif tipo == 2:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''UPDATE Apostas  SET retorno = ? WHERE id_apostas =?''', (valor, id_aposta,))
                conn.commit()


def add_relatorio(greens: int, reds: int, lucro: float, total_apostas: int, apostas_abertas:int, fk_id_bot: str) -> int:
    with sqlite3.connect('Greenzord.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('PRAGMA foreign_keys = ON;')
            cursor.execute('''INSERT INTO Relatorio (greens , reds, lucro,total_apostas,apostas_abertas,fk_id_bot) VALUES(?,?,?,?,?,?)''',
                           (greens, reds, lucro, total_apostas,apostas_abertas, fk_id_bot))
            conn.commit()


def atualizar_relatorio(tipo,id,valor):
    with sqlite3.connect('Greenzord.db') as conn:
        if tipo == 1:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''UPDATE Relatorio SET greens = ? WHERE fk_id_bot =?''', (valor, id,))
                conn.commit()
        elif tipo == 2:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''UPDATE Relatorio SET reds = ? WHERE fk_id_bot =?''', (valor, id,))
                conn.commit()
        elif tipo == 3:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''UPDATE Relatorio SET lucro = ? WHERE fk_id_bot =?''', (valor, id,))
                conn.commit()
        elif tipo == 4:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''UPDATE Relatorio SET total_apostas = ? WHERE fk_id_bot =?''', (valor, id,))
                conn.commit()
        elif tipo == 5:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''UPDATE Relatorio SET apostas_abertas = ? WHERE fk_id_bot =?''', (valor, id,))
                conn.commit()


def consultar_relatorio(id:int):
    with sqlite3.connect('Greenzord.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('PRAGMA foreign_keys = ON;')
            cursor.execute('''SELECT * FROM Relatorio WHERE fk_id_bot  =?''',(id,))
            tudo = cursor.fetchone()
            return tudo
            conn.commit()


def consultas(acao):
    with sqlite3.connect('Greenzord.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute(acao)
            tudo = cursor.fetchall()
            return tudo
            conn.commit()


def atualizar_jogosAoVivo(valor, id, tipo):
    with sqlite3.connect('Greenzord.db') as conn:
        if tipo == 1:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''UPDATE Jogos_AoVivo SET resultado_casa = ? WHERE id_jogo =?''', (valor, id,))
                conn.commit()
        elif tipo == 2:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''UPDATE Jogos_AoVivo SET resultado_fora = ? WHERE id_jogo =?''', (valor, id,))
                conn.commit()
        elif tipo == 3:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''UPDATE Jogos_AoVivo SET tempo = ? WHERE id_jogo =?''', (valor, id,))
                conn.commit()
        elif tipo == 4:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''UPDATE Jogos_AoVivo SET posse_bola_casa = ? WHERE id_jogo =?''', (valor, id,))
                conn.commit()
        elif tipo == 5:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''UPDATE Jogos_AoVivo SET posse_bola_fora = ? WHERE id_jogo =?''', (valor, id,))
                conn.commit()
        elif tipo == 6:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''UPDATE Jogos_AoVivo SET finalizacao_casa = ? WHERE id_jogo =?''', (valor, id,))
                conn.commit()
        elif tipo == 7:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''UPDATE Jogos_AoVivo SET finalizacao_fora = ? WHERE id_jogo =?''', (valor, id,))
                conn.commit()
        elif tipo == 8:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''UPDATE Jogos_AoVivo SET odd_casa = ? WHERE id_jogo =?''', (valor, id,))
                conn.commit()
        elif tipo == 9:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''UPDATE Jogos_AoVivo SET odd_fora = ? WHERE id_jogo =?''', (valor, id,))
                conn.commit()
        elif tipo == 10:
            with closing(conn.cursor()) as cursor:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute('''UPDATE Jogos_AoVivo SET odd_empate = ? WHERE id_jogo =?''', (valor, id,))
                conn.commit()


def deletar(acao):
    with sqlite3.connect('Greenzord.db') as conn:
        with closing(conn.cursor()) as cursor:
            try:
                cursor.execute(acao)
                conn.commit()
            except:
                print("erro")
            finally:
                print("Registro excluido")


def deletar_bot(id: int):
    with sqlite3.connect('Greenzord.db') as conn:
        with closing(conn.cursor()) as cursor:
            try:
                cursor.execute('''DELETE FROM Bots WHERE id_bot = ?''', (id,))
                conn.commit()
            except:
                print("erro")
            finally:
                print("Registro excluido")


def deletar_jogoAoVivo(id):
    with sqlite3.connect('Greenzord.db') as conn:
        with closing(conn.cursor()) as cursor:
            try:
                cursor.execute('''DELETE FROM Jogos_AoVivo WHERE id_jogo = ?''', (id,))
                conn.commit()
            except:
                print("erro")
            finally:
                print("Registro excluido")
