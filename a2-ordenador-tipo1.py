def linhas():
    print("-" * 48)

def obter_numero(mensagem: str) -> int:
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Erro. Digite um número inteiro válido.")

linhas()
print("Maior número entre três valores (sem operadores)")
linhas()

valor1 = obter_numero("Primeiro valor: ")
valor2 = obter_numero("Segundo valor: ")
valor3 = obter_numero("Terceiro valor: ")
maior_valor = max(valor1, valor2, valor3)

linhas()
print(f"O maior valor entre {valor1}, {valor2} e {valor3} é: {maior_valor}.")