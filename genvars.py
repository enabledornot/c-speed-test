import random
import sys
def makeRandomIntAry(length):
    intary = []
    for i in range(length):
        intary.append(random.randint(0,4294967295))
    return intary

numberOfVars = 2**int(sys.argv[1])
with open("c-vars.c","w") as f:
    f.write("#define varCount {}\nunsigned int data[{}] = {};".format(numberOfVars,numberOfVars,str(makeRandomIntAry(numberOfVars)).replace("[","{").replace("]","}")))