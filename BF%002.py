import os
from time import sleep

#BF% = [64 - (20 × altura ÷ (Circ. abdominal ) + (12 × sexo)]
errorMensage = "Erro!!!"
continuar = "s"

#Função que usa as medidas coletadas para calcular o percentual de gordura
def gorduraCalc(alt, abd, sexo):
    resultado = 0

    #Define o valor referente ao sexo M = 0; F = 1;
    if sexo in "Mm":
        sexo = 0
    elif sexo in "Ff":
        sexo = 1
    else:
        print(errorMensage)

    #Fórmula transcrita para código
    resultado = 64 - (20 * alt + abd  + (int(sexo) * 12))

    return resultado


def menu():
    print("="*60)
    print(f"""\033[1;33m{"Calculo de percentual de gordura corporal:":^60}
    \033[30m{"Fórmula de Wollcot\033[m":^60}""")
    print("="*60)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


while continuar in "s":
    clear()

    #Pequena representação visual de menu
    menu()

    #Coleta de dados do usuário
    userAltura = float(input("Digite sua altura: "))
    clear()
    menu()
    userAbd = float(input("Digite a circunferência do seu abdomen: "))
    clear()
    menu()
    userSex = input("Digite seu sexo [M/F]: ")
    clear()
    
    #Condição de entrada definida para sexo M = Masculino; F = Feminino;
    while userSex not in "MmFf":
        print("Valor inválido, digite novamente!")
        userSex = input("Digite seu sexo [M/F]: ")

    #Mostra o resultado final
    print("O seu percentual de gordura corporal é de:")
    print(f"\033[1;33m{gorduraCalc(userAltura, userAbd, userSex):.1f}%\033[m")
    continuar = input("Deseja inserir novos dados [S/N]: ")

    while continuar not in "SsNn":
        print("Valor inválido, digite novamente!")
        continuar = input("Deseja inserir novos dados [S/N]: ")

