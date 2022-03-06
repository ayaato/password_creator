import random

chars = {
    'numbers' : {'0123456789'},
    'letters' : {'abcdefghijklmnoprstuvyz'},
    'special' : {'>£#$½{[]}\!^+%&/()=?_'},
    'upletters': {'ABCDEFGHIJKLMNOPRSTUVYZ'}
}
rndi = random.randint(0,16); output = ''; i = 0
while i <= 16:
    i+=1
    rndspeciesselection = random.randint(0,len(chars.keys()))
    selectedspeciesconverttostring = str(list(chars.values())[rndspeciesselection-1])
    selectedspeciesconverttostringsplitted = [selectedspeciesconverttostring[x:x+1] for x in range(0,len(selectedspeciesconverttostring),1)]
    rnd = random.randint(0,len(selectedspeciesconverttostringsplitted))
    output  += selectedspeciesconverttostringsplitted[rnd-1]
print(output)
