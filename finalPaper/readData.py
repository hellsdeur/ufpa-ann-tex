from random import shuffle

f = open("Qualitative_Bankruptcy.data.txt","r")
file = open("Qua_Ban.data","a")
for linha in f:
    atributos = str(linha[0:12])
    classe = str(linha[12])
    atributos = atributos.replace('P','4')
    atributos = atributos.replace('A','3')
    atributos = atributos.replace('N','2')
    classe = classe.replace('N','0')
    classe = classe.replace('B','1')
    linha = atributos + classe + '\n'
    file.write(linha)
file.writelines(f)
f.close()
file.close()
with open("Qua_Ban.data") as f:
    lines = f.readlines()
shuffle(lines)
with open("Quali_Bank.csv", "w") as f:
    f.writelines(lines)
f.close()
