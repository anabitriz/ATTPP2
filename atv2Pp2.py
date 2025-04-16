"""# q.6)

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")



     

#  q.7)

nota1 = float(input("Digite a nota 1"))
nota2 = float(input("Digite a nota 2"))
nota3 = float(input("Digite a nota 3"))
media = (nota1 + nota2 + nota3) / 3

if media < 4:
    print("Reprovado")
elif 4 <= media <7:
 print("Em Prova Final")
else:
  print( "Aprovado")




     

# q.8)


idade = int(input("Digite a idade do nadador: "))

if 5 <= idade <= 7:
   print( "junior")
elif 8 <= idade <= 12:
   print( "infantil")
elif 13 <= idade <= 18:
   print( "pre")
elif idade > 18:
   print( "Avançada")
else:
  print("Idade inválida")



     
Digite a idade do nadador: 15
pre

# q.9)

n1 = float(input("Digite o primeiro número: "))
operador= input("Digite a operação (+, -, *, /): ")
n2 = float(input("Digite o segundo número: "))

if operador == "+":
    print(n1 + n2)
elif operador == "-":
    print(n1 - n2)
elif operador == "*":
    print(n1 * n2)
elif operador == "/":
    if n2 != 0:
        print(n1 / n2)
    else:
        print("Erro: Divisão por zero.")
else:
    print("Operador inválido.")#
     
Digite o primeiro número: 2
Digite a operação (+, -, *, /): +
Digite o segundo número: 6
8.0

#q.10)

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

if a <= b and b <= c:
    print(a, b, c)
elif a <= c and c <= b:
    print(a, c, b)
elif b <= a and a <= c:
    print(b, a, c)
elif b <= c and c <= a:
    print(b, c, a)
elif c <= a and a <= b:
    print(c, a, b)
else:
    print(c, b, a)
     

#q.11)
numero = int(input("Digite um número entre 20 e 39: "))

if 20 <= numero <= 29:
    unidade = numero - 20
    extenso = "Vinte" if unidade == 0 else f"Vinte e {['um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove'][unidade-1]}"
    print(extenso)
elif 30 <= numero <= 39:
    unidade = numero - 30
    extenso = "Trinta" if unidade == 0 else f"Trinta e {['um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove'][unidade-1]}"
    print(extenso)
else:
    print("Número fora do intervalo permitido.")
     

# q.12)

numero = int(input("Digite um número de 0 a 6: "))

if numero == 0:
    print("Fatorial: 1")
elif numero == 1:
    print("Fatorial: 1")
elif numero == 2:
    print("Fatorial: 2")
elif numero == 3:
    print("Fatorial: 6")
elif numero == 4:
    print("Fatorial: 24")
elif numero == 5:
    print("Fatorial: 120")
elif numero == 6:
    print("Fatorial: 720")
else:
    print("Número muito grande ou inválido para esta versão.")"""
     