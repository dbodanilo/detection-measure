import json
from sklearn.utils import shuffle
from numpy import loadtxt
import keras
from keras.models import Sequential
from keras.layers import Dense

model = keras.models.load_model("measureModel2")

braco_posicao=(0,1,0,0,0,0)
quadril_posicao=(0,0,1,0,0,0)
braco_quadril_posicao=(0,0,0,0,0,1)
perna_posicao=(0,0,0,0,1,0)
correto=(1,0,0,0,0,0)
    
f = open("output_measure_x.json")
X = json.load(f)
f.close()

f = open("output_measure_y.json")
y = json.load(f)
f.close()

print("Quantidade de dados")
print(len(X))
print("Limiar")
print("0.7")


for i in range(11):
    limiar=i/10
    predictions = (model.predict(X) > limiar).astype(int)

    vp=0
    fn=0
    fp=0
    vn=0

    tp=correto

    for i in range(len(X)):
        if tuple(predictions[i]) == tp and tuple(y[i]) == tp:
            vp+=1
        if (not tuple(predictions[i]) == tp) and tuple(y[i]) == tp:
            fn+=1
        if tuple(predictions[i]) == tp and (not tuple(y[i]) == tp):
            fp+=1
        if (not tuple(predictions[i]) == tp) and (not tuple(y[i]) == tp):
            vn+=1    
                
    print("Posição correta")
    print("limiar: ",limiar)
    print("vp: ",vp)
    print("fn: ",fn)
    print("fp: ",fp)
    print("vn: ",vn)


"""

predictions = (model.predict(X) > 0.7).astype(int)

bp=0
qp=0
bqp=0
pp=0
cor=0

tp=braco_posicao

for i in range(len(X)):
    if tuple(predictions[i]) == tuple(y[i]) and tuple(y[i]) == tp:
        bp+=1
    if not (tuple(predictions[i]) == tuple(y[i])): 
        if tuple(y[i]) == tp:
            if tuple(predictions[i]) == quadril_posicao:
                qp+=1
            if tuple(predictions[i]) == braco_quadril_posicao:
                bqp+=1
            if tuple(predictions[i]) == perna_posicao:
                pp+=1
            if tuple(predictions[i]) == correto:
                cor+=1    
print("Braco posicao")
print(bp)
print(qp)
print(bqp)
print(pp)
print(cor)
                
bp=0
qp=0
bqp=0
pp=0
cor=0

tp=quadril_posicao

for i in range(len(X)):
    if tuple(predictions[i]) == tuple(y[i]) and tuple(y[i]) == tp:
        qp+=1
    if not (tuple(predictions[i]) == tuple(y[i])): 
        if tuple(y[i]) == tp:
            if tuple(predictions[i]) == braco_posicao:
                bp+=1
            if tuple(predictions[i]) == braco_quadril_posicao:
                bqp+=1
            if tuple(predictions[i]) == perna_posicao:
                pp+=1
            if tuple(predictions[i]) == correto:
                cor+=1    
print("Quadril posicao")
print(bp)
print(qp)
print(bqp)
print(pp)
print(cor)

bp=0
qp=0
bqp=0
pp=0
cor=0

tp=braco_quadril_posicao

for i in range(len(X)):
    if tuple(predictions[i]) == tuple(y[i]) and tuple(y[i]) == tp:
        bqp+=1
    if not (tuple(predictions[i]) == tuple(y[i])): 
        if tuple(y[i]) == tp:
            if tuple(predictions[i]) == quadril_posicao:
                qp+=1
            if tuple(predictions[i]) == braco_posicao:
                bp+=1
            if tuple(predictions[i]) == perna_posicao:
                pp+=1
            if tuple(predictions[i]) == correto:
                cor+=1    
print("Braco quadril posicao")
print(bp)
print(qp)
print(bqp)
print(pp)
print(cor)

bp=0
qp=0
bqp=0
pp=0
cor=0

tp=perna_posicao

for i in range(len(X)):
    if tuple(predictions[i]) == tuple(y[i]) and tuple(y[i]) == tp:
        pp+=1
    if not (tuple(predictions[i]) == tuple(y[i])): 
        if tuple(y[i]) == tp:
            if tuple(predictions[i]) == quadril_posicao:
                qp+=1
            if tuple(predictions[i]) == braco_quadril_posicao:
                bqp+=1
            if tuple(predictions[i]) == braco_posicao:
                bp+=1
            if tuple(predictions[i]) == correto:
                cor+=1    
print("Perna posicao")
print(bp)
print(qp)
print(bqp)
print(pp)
print(cor)

bp=0
qp=0
bqp=0
pp=0
cor=0

tp=correto

for i in range(len(X)):
    if tuple(predictions[i]) == tuple(y[i]) and tuple(y[i]) == tp:
        cor+=1
    if not (tuple(predictions[i]) == tuple(y[i])): 
        if tuple(y[i]) == tp:
            if tuple(predictions[i]) == quadril_posicao:
                qp+=1
            if tuple(predictions[i]) == braco_quadril_posicao:
                bqp+=1
            if tuple(predictions[i]) == perna_posicao:
                pp+=1
            if tuple(predictions[i]) == braco_posicao:
                bp+=1    
print("Correto")
print(bp)
print(qp)
print(bqp)
print(pp)
print(cor)
"""

