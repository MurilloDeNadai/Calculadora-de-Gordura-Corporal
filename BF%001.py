#BF% = [64 - (20 × altura ÷ (Circ. abdominal ) + (12 × sexo)]
errorMensage = "Erro!!!"

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

#Pequena representação visual de menu
print("""\033[1;33mCalculo de percentual de gordura corporal:
\033[30mFórmula utilizada: Fórmula de Wollcot\033[m""")

#Coleta de dados do usuário
userAltura = float(input("Digite sua altura: "))
userAbd = float(input("Digite a circunferência do seu abdomen: "))
userSex = input("Digite seu sexo [M/F]: ")

#Condição de entrada definida para sexo M = Masculino; F = Feminino;
while userSex not in "MmFf":
    print("Valor inválido, digite novamente!")
    userSex = input("Digite seu sexo [M/F]: ")

#Mostra o resultado final
print(gorduraCalc(userAltura, userAbd, userSex))
