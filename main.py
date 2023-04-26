#Programa vai pegar str(opções de alimentos) em uma determinada tupla é monta um "prato" para o cliente, exemplo: 0,3,0
# por sequencia esse itens são Maçã,Ovo,Suco de caju, porem o cliente não tem a noção, que para conseguir esses alimento ele precisar por essa numeração, entao o jeito e deixa que ele escolha de forma intuitiva e o programa retorne o valor é a lista do que ele ira comer!

# Correção de erros!

# Tkinter = Bom tentar introduzir o tkinter nas proximas linhas, a inteção e fazer uma janela funcional, com as opções pre-definidas para o usuario!

# usando o tkinter, adicionar umas janela que peça o email é o numero telefonico, como forma de validação para sua "POSSIVEL" compra na loja de conveniencia 

from mod import cole
from mod import sms as s

cole('Bem vindo a loja de conveniencia! :)')

Alimentos_Saude = ('Maçã' , 'Uva', 'Alface', 'Tomate')
# Alimentos_Gorduroso = ('Coxinha', 'Bacon', 'Ovo', 'Hamburg')
# Bebidas = ('Suco de uva', 'Suco de Caju', 'Guarana', 'Coca-Cola')

saude = Alimentos_Saude

# ERRO: Bom até então aconteceu um erro no index da tupla, tentar corrigir! ou tratar o erro, bem provavel que a correção ajude mais para não acontecer futuramente, e a correção de erro ser menor
cole('--Lista de Alimentos Saudaveis--')
for n in range(0,6):
    s("Chata pra caralho!")

# num = int(input('digite um numero: '))
# if num == num:
#     num1 = int(input('Deseja escolher mais um itens: '))
    
#     c = num + 2

# for t in range(num,c):
#     c = num + 1
#     sa = saude[t]
#     cole(f'{sa}')
    


    


    
