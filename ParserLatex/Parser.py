nome_arquivo = str(input("insira o nome do arquivo:"))

partes = nome_arquivo.split(".")

nome_arquivo = partes[0] + ".txt"

with open(nome_arquivo, "r") as arquivo:

    expressoes = arquivo.readlines()

    cont1 = 0
    for x in expressoes:
        item = x.split("\n")
        expressoes[cont1] = item[0]

        cont1+=1
def verifica_unario(ini, fim):
    global estado
    if not exprec[ini] == " ":
        estado = "invalido"
        return False
    else:
        j = ini
        cont_signo = 0
        while j <= fim:
            if exprec[j] == " ":
                if cont_signo > 0:
                    estado = "invalido"
                    return False
            else:
                cont_signo += 1
            j += 1

        if cont_signo > 0:
            estado = "valido"
            return True


def verifica_binario(ini, fim):
    global estado
    if not exprec[ini] == " ":
        estado = "invalido"
        return False
    else:
        cont_signo = 0
        cont = 0
        j = ini
        while j < fim:
            if exprec[j] == " ":
                if cont_signo > 0:
                    cont += 1
            else:
                cont_signo += 1
            j += 1

        if cont == 1:
            estado = "valido"
            return True
        else:
            estado = "invalido"
            return False

def arruma_string():
    j = 0
    string_nova = ""
    while j < len(exprec):
        if j == AbreParen:
            string_nova += "V"
        elif j > AbreParen and FechaParen >= j:
            string_nova = string_nova
        else:
            string_nova += exprec[j]
        j += 1
    return string_nova

def verifica_contra_barra(ini, fim):
    global estado
    if exprec[ini] == "/":
        if exprec[ini + 1] == "n":
            if exprec[ini + 2] == "e" and exprec[ini + 3] == "g":
                estado = "unario"
                return 3
        elif exprec[ini + 1] == "w":
            if exprec[ini + 2] == "e" and exprec[ini + 3] == "d" and exprec[ini + 4] == "g" and exprec[ini + 5] == "e":
                estado = "binario"
                return 5
        elif exprec[ini + 1] == "v":
            if exprec[ini + 2] == "e" and exprec[ini + 3] == "e":
                estado = "binario"
                return 3
        elif exprec[ini + 1] == "r":
            if exprec[ini + 2] + exprec[ini + 3] + exprec[ini + 4] + exprec[ini + 5] + exprec[ini + 6] + exprec[ini + 7]\
                    + exprec[ini + 8] + exprec[ini + 9] + exprec[ini + 10] == "ightarrow":
                estado = "binario"
                return 10
        elif exprec[ini + 1] == "l":
            if exprec[ini + 2] + exprec[ini + 3] + exprec[ini + 4] + exprec[ini + 5] + exprec[ini + 6] + exprec[ini + 7]\
                    + exprec[ini + 8] + exprec[ini + 9] + exprec[ini + 10] + exprec[ini + 11] \
                    + exprec[ini + 12] + exprec[ini + 13] + exprec[ini + 14] == "eftrightarrow":
                estado = "binario"
                return 14
    else:
        j = ini + 1
        while j < fim:
            if exprec[j] == " ":
                estado = "invalido"
                return 0
            j+=1
        estado = "valido"
        return 0

final = expressoes[0]

if int(final) == len(expressoes) - 1:
    x = 1

    while x <= int(final):
        estado = "valido"

        exprec = expressoes[x]

        AbreParen = 0
        FechaParen = 0

        i = 0
        n = len(exprec)

        print("Expressão: " + exprec, end="")

        while i < n:
            if exprec[i] == "(":
                AbreParen = i
            elif exprec[i] == ")":
                FechaParen = i
                aumentar = verifica_contra_barra(AbreParen + 1, FechaParen - 1)
                if estado == "invalido":
                    i = n
                elif estado == "valido":
                    exprec = arruma_string()
                    i = 0
                    n = len(exprec)
                    continue
                elif estado == "unario":
                    if verifica_unario(AbreParen + aumentar + 2, FechaParen - 1):
                        exprec = arruma_string()
                        i = 0
                        n = len(exprec)
                        continue
                    else:
                        i = n
                else:
                    if verifica_binario(AbreParen + aumentar + 2, FechaParen - 1):
                        exprec = arruma_string()
                        i = 0
                        n = len(exprec)
                        continue
                    else:
                        i = n
            i += 1

        if estado == "valido":
            print("; Condição: Válida")
        else:
            print("; Condição: Inválida")

        x += 1
else:
    print("O número de expressões não condiz com o informado")