def linhas():
    print("-" * 51)

def obter_numero(mensagem: str) -> int:
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Erro. Digite um número inteiro válido.")

linhas()
print("Maior número entre três valores (usando operadores)")
linhas()

valor1 = obter_numero("Primeiro valor: ")
valor2 = obter_numero("Segundo valor: ")
valor3 = obter_numero("Terceiro valor: ")
maior = valor1

if valor2 > maior:
    maior = valor2
if valor3 > maior:
    maior = valor3

linhas()
print(f"O maior valor entre {valor1}, {valor2} e {valor3} é: {maior}.")