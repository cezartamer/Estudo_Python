CONSTANTE_BONUS = 1000
nome = input("Digite seu nome: ")
salario = float(input("Digite o valor do seu salário: "))
bonus = float(input("Digite % do seu bônus recebido: "))
KPI =  CONSTANTE_BONUS + salario * bonus 
print("O valor do bonus total é: " + str(KPI))
print("Nome: " + nome + ", Salário: "+ str(salario) + ", Bonus: " +str(bonus) + ", KPI: "+ str(KPI))
print(f"Nome: {nome}, Salário: {salario} , Bonus: {bonus} KPI: {KPI}")