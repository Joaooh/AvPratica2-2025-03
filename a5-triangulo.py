def linhas():
    print("-" * 52)

linhas()
print("Verificador de Triângulos".center(52))
linhas()

def forma_triangulo(lado_a: float, lado_b: float, lado_c: float) -> bool:
    return (
        lado_a > 0 and lado_b > 0 and lado_c > 0
        and (lado_a + lado_b > lado_c and lado_a + lado_c > lado_b and lado_b + lado_c > lado_a)
    )

def tipo_triangulo(lado_a: float, lado_b: float, lado_c: float) -> str:
    if lado_a == lado_b == lado_c:
        return "É um triângulo equilátero (todos os lados iguais)"
    if lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
        return "É um triângulo isósceles (dois lados iguais)"
    return "É um triângulo escaleno (todos os lados diferentes)"

def obter_lado(mensagem: str) -> float:
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Erro. Tente novamente com um número válido.")

def lados():
    while True:
        lado_a = obter_lado("Digite o primeiro lado: ")
        lado_b = obter_lado("Digite o segundo lado: ")
        lado_c = obter_lado("Digite o terceiro lado: ")

        linhas()
        if forma_triangulo(lado_a, lado_b, lado_c):
            print("Os valores inseridos formam um triângulo válido!")
            print(tipo_triangulo(lado_a, lado_b, lado_c))
        else:
            print("Os valores inseridos não formam um triângulo válido.")
        linhas()

        continuar = input("Deseja verificar outro triângulo? (s/n): ").strip().lower()
        if continuar == "n":
            print("\nFinalizando o programa.")
            break

lados()