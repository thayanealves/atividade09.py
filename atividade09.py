# Um motorista deseja calcular o consumo médio de combustível do seu carro. Crie um programa que receba a quantidade de quilômetros percorridos e a quantidade de litros de combustível consumidos, e calcule o consumo médio (km por litro).

km_percorrido = float(input("digite o valor do km percorrido"))
l_combus = float(input("digite a quantidade de litros"))

cons_medio = km_percorrido/l_combus
print (cons_medio)