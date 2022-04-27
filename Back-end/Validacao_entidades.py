import re


def validar_username(username):
    validar = re.compile(r'\W')
    validar2 = re.compile(r'\s')
    check = validar.findall(username)
    check2 = validar2.findall(username)
    tamanho = len(check)
    tamanho2 = len(check2)
    if tamanho > 0 and tamanho2 > 0:
        return False
    else:
        return True


def validar_nome(nome):
    validar = '^[ a-zA-Z á]*$'
    if (re.search(validar, nome)):
        return True
    else:
        return False


def validar_email(email):
    validar = '[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]'
    if (re.search(validar, email)):
        return True
    else:
        return False


def validar_inteiros(numero):
    validar = '^[0-9]*$'
    if (re.search(validar, numero)):
        return True
    else:
        return False


def validar_float(numero):
    validar = '^[0-9]+\.[0-9]'
    if (re.search(validar, numero)):
        return True
    else:
        return False
