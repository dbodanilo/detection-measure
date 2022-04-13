import json
from sklearn.utils import shuffle
from numpy import loadtxt
import keras
from keras.models import Sequential
from keras.layers import Dense

model = keras.models.load_model("detectionModel2")

agachamento=(0,0,1)
extensaoquadril=(0,1,0)
flexaojoelho=(1,0,0)

f = open("output_detection_x.json")
X = json.load(f)
f.close()

f = open("output_detection_y.json")
y = json.load(f)
f.close()

print("Quantidade de dados")
print(len(X))
print("Limiar")
print("0.5")




for i in range(11):
    limiar=i/10
    predictions = (model.predict(X) > limiar).astype(int)

    vp=0
    fn=0
    fp=0
    vn=0

    tp=flexaojoelho

    for i in range(len(X)):
        if tuple(predictions[i]) == tp and tuple(y[i]) == tp:
            vp+=1
        if (not tuple(predictions[i]) == tp) and tuple(y[i]) == tp:
            fn+=1
        if tuple(predictions[i]) == tp and (not tuple(y[i]) == tp):
            fp+=1
        if (not tuple(predictions[i]) == tp) and (not tuple(y[i]) == tp):
            vn+=1    
                
    print("Flexão joelho")
    print("limiar: ",limiar)
    print("vp: ",vp)
    print("fn: ",fn)
    print("fp: ",fp)
    print("vn: ",vn)



"""
aga=0
ext=0
fle=0

tp=agachamento

for i in range(len(X)):
    if tuple(predictions[i]) == tuple(y[i]) and tuple(y[i]) == tp:
        aga+=1
    if not (tuple(predictions[i]) == tuple(y[i])): 
        if tuple(y[i]) == tp:
            if tuple(predictions[i]) == extensaoquadril:
                ext+=1
            if tuple(predictions[i]) == flexaojoelho:
                fle+=1
print("Agachamento")
print(aga)
print(ext)
print(fle)
                
aga=0
ext=0
fle=0

tp=extensaoquadril

for i in range(len(X)):
    if tuple(predictions[i]) == tuple(y[i]) and tuple(y[i]) == tp:
        ext+=1
    if not (tuple(predictions[i]) == tuple(y[i])): 
        if tuple(y[i]) == tp:
            if tuple(predictions[i]) == agachamento:
                aga+=1
            if tuple(predictions[i]) == flexaojoelho:
                fle+=1
print("Extensao quadril")
print(aga)
print(ext)
print(fle)
aga=0
ext=0
fle=0

tp=flexaojoelho

for i in range(len(X)):
    if tuple(predictions[i]) == tuple(y[i]) and tuple(y[i]) == tp:
        fle+=1
    if not (tuple(predictions[i]) == tuple(y[i])): 
        if tuple(y[i]) == tp:
            if tuple(predictions[i]) == agachamento:
                aga+=1
            if tuple(predictions[i]) == extensaoquadril:
                ext+=1
print("Flexão joelho")
print(aga)
print(ext)
print(fle)
"""
