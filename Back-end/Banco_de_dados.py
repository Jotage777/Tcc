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
                CREATE TABLE Jogos(
                    id_jogo VARCHAR (20) primary key ,
                    fk_id_casa INTEGER NOT NULL,
                    fk_id_campeonato INTEGER NOT NULL,
                    fk_id_fora INTEGER  NOT NULL ,
                    resultado_fora INTEGER NOT NULL ,
                    resultado_casa INTEGER NOT NULL ,
                    date VARCHAR(10) NOT NULL,
                    odd_casa FLOAT NOT NUll,
                    odd_fora FLOAT NOT NUll,
                    odd_empate FLOAT NOT NULL,
                    FOREIGN KEY(fk_id_casa) REFERENCES Times (id_time),
                    FOREIGN KEY(fk_id_fora) REFERENCES Times (id_time),
                    FOREIGN KEY(fk_id_campeonato) REFERENCES Campeonato (id_campeonato)
                    )''')
            cursor.execute('''
                CREATE TABLE Usuario(
                    id_usuario INTEGER primary key AUTOINCREMENT ,
                    username VARCHAR(45) NOT NULL,
                    nome VARCHAR (45) NOT NULL ,
                    email VARCHAR (45) NOT NULL ,
                    data_Nascimento DATE NOT NULL,
                    saldo FLOAT NOT NULL
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
                    fk_id_bot INTEGER NOT NULL,
                    fk_id_jogos INTEGER NOT NULL ,
                    FOREIGN KEY(fk_id_bot) REFERENCES Bots(id_bot),
                    FOREIGN KEY(fk_id_jogos) REFERENCES Jogos(id_jogo)
                    )''')
            cursor.execute('''
                CREATE TABLE Relatorio(
                    id_relatorio INTEGER primary key AUTOINCREMENT ,
                    greens INTEGER NOT NULL,
                    reds INTEGER NOT NULL,
                    lucro FLOAT NOT NULL,
                    total_apostas INTEGER NOT NULL,
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


def add_jogos(campeonato: str, id: str, casa: str, resultado_casa: int, fora: str, resultado_fora: int, data: str,
              odd_casa: float, odd_fora: float, odd_empate: float) -> int:
    with sqlite3.connect('Greenzord.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('PRAGMA foreign_keys = ON;')
            cursor.execute('''SELECT id_jogo FROM Jogos WHERE id_jogo = ?''', (id,))
            result = cursor.fetchone()
            if result is None:
                fk_id_campeonato = add_campeonato(campeonato)
                fk_id_casa = add_times(casa)
                fk_id_fora = add_times(fora)
                cursor.execute('''INSERT INTO Jogos (id_jogo, fk_id_casa, resultado_casa, fk_id_fora, resultado_fora,
                date, fk_id_campeonato, odd_casa, odd_fora, odd_empate)
                VALUES(?,?,?,?,?,?,?,?,?,?)''', (id, fk_id_casa, resultado_casa, fk_id_fora, resultado_fora, data,
                                                 fk_id_campeonato, odd_casa, odd_fora, odd_empate))
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

def add_usuario(username: str, nome: str, email: str, data_Nascimento: str, saldo: float) -> int:
    with sqlite3.connect('Greenzord.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('PRAGMA foreign_keys = ON;')
            cursor.execute('''SELECT username FROM Usuario WHERE username = ?''', (username,))
            result = cursor.fetchone()
            if result is None:
                cursor.execute('''INSERT INTO Usuario (username , nome , email , data_Nascimento , saldo)
                VALUES(?,?,?,?,?)''', (username, nome, email, data_Nascimento, saldo))
                conn.commit()
            else:
                return id
                conn.commit()


def consultar_bots(nome:str) -> int:
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


def consultar_aposta(id_aposta) -> int:
    with sqlite3.connect('Greenzord.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('PRAGMA foreign_keys = ON;')
            cursor.execute('''SELECT id_aposta FROM Aposta WHERE id_aposta = ?''', (id_aposta,))
            result = cursor.fetchone()
            if result is None:
                print("Não existe essa aposta na base de dados")
                conn.commit()
            else:
                conn.commit()


def add_apostas(mercado: str, valor_apostado: float, odd_aposta: float, id_bot: str, id_jogo: str) -> int:
    with sqlite3.connect('Greenzord.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('PRAGMA foreign_keys = ON;')
            fk_id_bot = consultar_bots(id_bot)
            fk_id_jogos = consultar_jogos(id_jogo)
            cursor.execute('''INSERT INTO Apostas (mercado, valor_apostado, odd_aposta, fk_id_bot,fk_id_jogo)
            VALUES(?,?,?,?,?)''', (mercado, valor_apostado, odd_aposta, fk_id_bot, fk_id_jogos))
            conn.commit()


def add_relatorio(greens: int, reds: int, lucro: float, total_apostas: int, fk_id_bot: str) -> int:
    with sqlite3.connect('Greenzord.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('PRAGMA foreign_keys = ON;')
            cursor.execute('''INSERT INTO Relatorio (greens , reds, lucro,total_apostas,fk_id_bot) VALUES(?,?,?,?,?)''',
                           (greens, reds, lucro, total_apostas, fk_id_bot))
            conn.commit()


def consultas(acao):
    with sqlite3.connect('Greenzord.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('PRAGMA foreign_keys = ON;')
            cursor.execute(acao)
            tudo = cursor.fetchall()
            return tudo
            conn.commit()


def deletar(acao):
    with sqlite3.connect('Greenzord.db') as conn:
        with closing(conn.cursor()) as cursor:
            try:
                cursor.execute('PRAGMA foreign_keys = ON;')
                cursor.execute(acao)
                conn.commit()
            except:
                print("erro")
            finally:
                print("Registro excluido")