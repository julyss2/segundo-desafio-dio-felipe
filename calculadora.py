def calcular_rank(vitorias, derrotas):
    saldo_vitorias = vitorias - derrotas
    
    if vitorias < 10:
        nivel = "Ferro"
    elif vitorias <= 20:
        nivel = "Bronze"
    elif vitorias <= 50:
        nivel = "Prata"
    elif vitorias <= 80:
        nivel = "Ouro"
    elif vitorias <= 90:
        nivel = "Diamante"
    elif vitorias <= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal"
    
    mensagem = f"O Herói tem saldo de {saldo_vitorias} está no nível de {nivel}"

    return mensagem

vitorias = int(input("Digite a quantidade de vitórias do herói: "))
derrotas = int(input("Digite a quantidade de derrotas do herói: "))

resultado = calcular_rank(vitorias, derrotas)

print(resultado)
