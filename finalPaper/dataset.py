from random import shuffle

f = open("Quali_Bank.data","r")
file = open("dataset.data","a")
for linha in f:
    linha = linha.replace(',',' ')
    file.write(linha)
file.writelines(f)
f.close()
file.close()
