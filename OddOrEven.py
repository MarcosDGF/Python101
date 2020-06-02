def numbercheck (num):
    if (float(num) % 2 == 0):
        print("O número: " +str(num)+" é par")
    else:
        print("O número: " +str(num)+" é ímpar")


nume = input("Digite o número desejado:")
numbercheck (nume)
