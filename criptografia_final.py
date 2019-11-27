

import random
from cryptography.fernet import Fernet

	#iniciando o valor primo de p

xp = False
divp = 0

while(bool(xp == False)):	#algoritmo que verifica a primalidade do número
	p = random.randint(100,300)
	divp = 0
	for x in range (1, p+1):
		resto = p % x
		if resto == 0:
			divp = divp + 1
	if divp == 2:
		print("Número {} para o p é válido" .format(p))
		xp = True
	else:
		xp = False
		
	#iniciando o valor primo de q


xq = False
divp = 0

while(bool(xq == False)):	#algoritmo que verifica a primalidade do número
	q = random.randint(100,300)
	divq = 0
	for x in range (1, q+1):
		resto = q % x
		if resto == 0:
			divq = divq + 1
	if divq == 2:
		print("Número {} para o q é válido" .format(q))
		xq = True
	else:
		xq = False
		

	#calculando o valor de n
	
n = p*q
print("N =",n)

	#calculando o phi de n

phin = (p-1)*(q-1)
print("fi de n =",phin)

	#gerando a chave e

e = random.randint(2,phin-1)


	#gerando mdc de phin,e para verificar se o mdc entre os 2 números é = 1, pois só assim o (e) é aceitável.
n1 = phin
n2 = e


def mdc(n1,n2):	#Definindo uma função para achar o mdc
	rest = 1
	
	while(n2 != 0):
		rest = n1%n2
		n1 = n2
		n2 = rest
	return n1


if(mdc(n1,n2)>1):
	ver = 0
else:
	ver = 1
	
	
while(ver==0):	#looping para calcular o mdc até que a chave (e) seja aceita para a encriptação.
	e = random.randint(2,phin-1)
	ver=1
	mdc(n1,n2)
	if(mdc(n1,n2)!=1):
		ver=0
		n1 = phin
		n2 = e
	else:
		e = e
		ver=1
print("Chave (e)= ",e)
chapub1 = e 
#Aqui achamos a primeira parte da chave (e)


	#Calculando (D) para geração da chave privada.
	
d = random.randint(2,phin-1)
a = d*e
b = phin

def chaved(a,b):	#Criei uma função para achar o módulo de d*e com phi(n)
	rest = a%b
	return rest
verific = chaved(a,b)

if(verific ==1):
	d = d
	print("Chave d()= ",d)
else:
	while(verific!=1):
		d = random.randint(2,phin-1)
		a = d*e
		b = phin
		chaved(a,b)
		verific = chaved(a,b)
		"""print("Verificação=",verific)"""
		if(verific==1):
			d = d
			print("Chave (d)= ",d)

	

chapri1 = d



	#aqui começaremos a encriptar a mensagem
	


class Cryptography(object):

    def criptografia(self, m, chapub1, n): #criando função de criptografia
        c = (m**chapub1) % n
        return c

    def descriptografia(self, c, chapri1, n): #criando a função de decriptografia
        m = c**chapri1 % n
        return m

    def encripta_mensagem(self):	#função de criptografia de caracters(aqui a função percorre cada x(caractere) na mensagem e converte em seu valor ascii)
        m = input("Digite a mensagem: \t")
        enc = ''.join(chr(self.criptografia(ord(x), chapub1, n)) for x in m)
        print()
        print()
        print('Texto Cifrado: ', enc, '\n')
        print()
        return enc
        text.encode("utf-8")
        
    def decripta_mensagem(self, m):	#função de decriptografia de caracters(aqui a função percorre cada x(caractere) na mensagem que está em ascii criptografada e converte em texto simples)
        self.m = m
        dec = ''.join(chr(self.descriptografia(ord(x), chapri1, n)) for x in m)
        print()
        return print('Texto Simples: ', dec, '\n')
       
 
 
valide = str(input("Deseja encriptar uma mensagem? (s/n)\n"))
if(valide =="s" or valide=="S"):
	valid2 = int(input("Insira a chave publica (e): "))
	while(valid2 !=e):
		print("Chave pública inválida, forneca a chave correta:")
		valid2 = int(input("Insira a chave publica (e): "))
	if(valid2==e):
		mensagem = Cryptography()
		mensagem_cifrada = mensagem.encripta_mensagem()
else:
	print()
	print()
	print("-----------------------FIM!--------------------------------------")
	exit("O usuário não escolheu encriptar nenhuma mensagem.")
		
validec = str(input("Deseja decriptar a mensagem? (s/n)\n"))

if(validec=="s" or validec=="S"):
	validec2 = int(input("Insira a chave privada (d): "))
	while(validec2 !=d):
		print("Chave privada inválida, forneca a chave correta: ")
		validec2 = int(input("Insira a chave privada (d): "))
		print()
		print()
	if(validec2==d):
		mensagem.decripta_mensagem(mensagem_cifrada)

else:
	print()
	print()
	print("-----------------------FIM!--------------------------------------")
	exit("O usuário não escolheu decriptar a mensagem.")
	
		
			