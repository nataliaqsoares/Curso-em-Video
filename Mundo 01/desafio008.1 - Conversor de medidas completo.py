""" Desafio 008.1
Escreva um programa que leia um valor em metros e o exiba convertido de km a milimetros """

m = float(input('Digite um valor: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('{} metro(s) é(são) equivalente(s) a: \n{} km \n{} hm \n{} dam \n{} dm \n{} cm \n{} mm'
      .format(m, km, hm, dam, dm, cm, mm))
