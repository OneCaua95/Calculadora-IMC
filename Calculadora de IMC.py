print("Qual o seu peso em kg?")
Peso = int(input())

print("Qual sua altura em metros?")
Altura = float(input())

def IMC(Peso, Altura):
    Valor_IMC = (Peso / (Altura * Altura))
    return Valor_IMC  

Valor_IMC = IMC(Peso, Altura)

condicoes = {
    (0, 18.5): "abaixo do peso",
    (18.5, 25): "peso ideal",
    (25, 30): "levemente acima do peso",
    (30, 35): "obesidade grau 1",
    (35, 40): "obesidade grau 2 (severa)",
    (40, float('inf')): "obesidade grau 3 (mórbida)"
}

condicao = next((v for k, v in condicoes.items() if k[0] < Valor_IMC <= k[1]), None)

print(f"O seu IMC é {Valor_IMC}, logo sua condição é {condicao}")
input()