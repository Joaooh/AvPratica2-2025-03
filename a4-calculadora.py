def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    return "Erro: divisão por zero não é permitida." if y == 0 else x / y

def formatar(valor):
    return int(valor) if valor == int(valor) else f"{valor:.2f}"

def linhas():
    print("-" * 44)

linhas()
print("Calculadora de quatro operações".center(44))
linhas()

print("+ → Adição\n- → Subtração\n* → Multiplicação\n/ → Divisão")

operacoes = {
    '+': ("Adição", adicao),
    '-': ("Subtração", subtracao),
    '*': ("Multiplicação", multiplicacao),
    '/': ("Divisão", divisao)
}

while True:
    operacao = input("Escolha uma operação (+, -, *, /): ").strip()
    if operacao in operacoes:
        linhas()
        print(f"Operação escolhida: {operacoes[operacao][0]}")
        while True:
            try:
                num1 = float(input("Digite o primeiro número: "))
                break
            except ValueError:
                print("Erro: Verifique se digitou um número válido.")

        while True:
            try:
                num2 = float(input("Digite o segundo número: "))
                break
            except ValueError:
                print("Erro: Verifique se digitou um número válido.")

        resultado = operacoes[operacao][1](num1, num2)
        linhas()
        print(f"{formatar(num1)} {operacao} {formatar(num2)} = {formatar(resultado)}")
        linhas()

        while True:
            continuar = input("Quer fazer outro cálculo? (s/n): ").strip().lower()
            if continuar in ("s", "sim"):
                break
            elif continuar in ("n", "não", "nao"):
                print("\nFinalizando a calculadora.")
                exit()
            else:
                print("Erro: Responda com s/n ou sim/não.")