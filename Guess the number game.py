import random
import sys
##Isso é pra gerar compatibilidade com Python 2.##
if sys.version_info[0] < 3:
    input = raw_input


def start_guess():
    i = 0
    j = 0
    random_number = random.randrange(0, 101) ##Vai gerar um número entre 0 e 100, pois é (0,101] (aberto no 0 fechado no
                                             ##101)
    print("A random number between 0 and 100 has been generated!")

    while True: ##loop infinito, vai ficar rodando pra sempre, até tomar um BREAK
        try:
            user_input = int(input("Now, try to guess what's the value of that number:")) ##Se for um número quebrado, irá converter para um integer
        except ValueError: ##Ativa se o usuário colocar algo que não é um número
            print("That's not a number. Enter an actual number.")
            i = i + 1
            if i == 5:
                print("Homie, you ain't know no numbers. Get the fuck outta here and go read some books!")
                break
            continue
        if user_input == random_number:
            print("Look at you! You guessed it right")
            break ##O BREAK quebra o WHILE
        elif not 0 <= user_input <= 100:    # Só caso o usuário coloque um número que não é entre o intervalo
                                            # predeterminado.
            print("The guess range is between 0 to 100, please try a bit {}." .format("higher" if user_input < 0 else "lower"))
            j = j + 1
            if j == 5:
                print("You clearly don't know how to follow rules so I'm shutting this whole thing down right now!")
                break
                 #Caso o número seja maior que 100 ele vai dizer "please try a
                 #bit LOWER"
                 #Caso seja menor que 0, i.e., um número negativo, ele vai
                 #dizer "please try a bit HIGHER"
                 #Como só tem duas possibilidades (ou o número é maior que o
                 #intervalo ou menor), basta especificar um dos casos e
                 #utilizar
                 #o ELSE para o outro caso.
        else:
            print("Please try a {} number this time." .format("higher" if user_input < random_number else "lower"))
                #Aqui o usuário colocou o número no intervalo correto, e
                #novamente, só há duas possibilidades: ou o NUMERO INPUT é
                #MAIOR
                #ou MENOR do que o NÚMERO GERADO.  Então basta especificar 1
                #dos casos e para o outro usar ELSE

if __name__ == "__main__":
    start_guess()
    print('''Thank you for playing!
See you next time.''')
