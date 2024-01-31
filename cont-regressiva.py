import time
tempo = int(input("Entre com o valor: "))
i = 0
while tempo >= i:
  print(tempo)
  time.sleep(1)
  tempo -= 1
print("O tempo acabou!!!")
