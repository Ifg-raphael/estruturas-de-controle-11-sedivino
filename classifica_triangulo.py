'''
## Lista 03 - Exercício 11

Elaborar um programa que lê 3 valores a,b,c e verifica se eles formam ou não um triângulo. Supor que os valores lidos são inteiros e positivos. Caso os valores formem um triângulo, calcular e escrever o tipo de triângulo (escaleno, isósceles ou eqüilátero). Se não formam triângulo escrever os valores lidos. Propriedade – O comprimento de cada lado de um triângulo é menor do que a soma dos comprimentos dos outros dois lados.

**Definição 1 –** Triângulo equilátero é o triângulo que tem os comprimentos dos três lados iguais.

**Definição 2 –** Triângulo isósceles é o triângulo que tem os comprimentos de dois lados iguais.

**Definição 3 –** Triângulo escaleno é o triângulo que tem os comprimentos dos três lados diferentes.

O programa deve assumir que a entrada e saída seja exatamente no formato dado nos exemplos a seguir. **Não adicione outras mensagens ou mude a capitalização das letras pois se fizer isso o teste não passará!**

---

**Exemplo 01:**

Entrada:
```
3 3 3
```
Saída:
```
equilátero
```
**Exemplo 03:**

Entrada:
```
2 2 4
```
Saída:
```
Não forma triângulo
```

'''

# Leitura dos valores
a, b, c = map(int, input().split())

# Verificação se formam um triângulo
if a < b + c and b < a + c and c < a + b:
    # Verificação do tipo de triângulo
    if a == b == c:
        print("equilátero")
    elif a == b or b == c or a == c:
        print("isósceles")
    else:
        print("escaleno")
else:
    print("Não forma triângulo")
    