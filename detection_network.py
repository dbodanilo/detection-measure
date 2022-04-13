import json
from sklearn.utils import shuffle
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense

def convertNoiseToDetection(data):
    agachamento=[]
    extensaoquadril=[]
    flexaojoelho=[]
    for i in data:
        tp=i[0]
        if tp[0]==1 and tp[1] ==0 and tp[2] ==0:
            aux=[]
            aux.append(i[1])
            aux.append(i[2])
            aux.append(i[3])
            aux.append(i[4])
            flexaojoelho.append(aux)
            
        if tp[0]==0 and tp[1] ==1 and tp[2] ==0:
            aux=[]
            aux.append(i[1])
            aux.append(i[2])
            aux.append(i[3])
            aux.append(i[4])
            extensaoquadril.append(aux)
            
        if tp[0]==0 and tp[1] ==0 and tp[2] ==1:
            aux=[]
            aux.append(i[1])
            aux.append(i[2])
            aux.append(i[3])
            aux.append(i[4])
            agachamento.append(aux)
    data_array = {'agachamento':[], 'extensaoquadril': [], 'flexaojoelho': []}
    data_array['agachamento']=agachamento
    data_array['extensaoquadril']=extensaoquadril
    data_array['flexaojoelho']=flexaojoelho
    return data_array

all_datas=[]

classes = {'agachamento':[0,0,1], 'extensaoquadril': [0,1,0], 'flexaojoelho': [1,0,0]}

f = open('all_features_low_noisy_5.json')
data = json.load(f)

data=convertNoiseToDetection(data)


for label in data:
    for features in data[label]:
        specific_values=[]
        for vl in features:
            specific_values.append(vl)
        specific_values.append(label)
        all_datas.append(specific_values)
            


all_datas=shuffle(all_datas, random_state=0)


X=[]
y=[]

for i in all_datas:
    content_values=[]
    for j in range(5):
        if j!=4:
            content_values.append(i[j])
        else:
            y.append(classes[i[j]])
    X.append(content_values)





pr=int(len(X)*0.1)
Dx=[]
Dy=[]
Xt=[]
Yt=[]

for lk in range(0,pr,1):
    Xt.append(X[lk])
    Yt.append(y[lk])

for lk in range(pr,len(X),1):
    Dx.append(X[lk])
    Dy.append(y[lk])

with open("output_detection_x.json", 'w') as f:
    json.dump(Xt, f)
with open("output_detection_y.json", 'w') as f:
    json.dump(Yt, f)    


model = Sequential()
model.add(Dense(10, input_dim=4, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(3, activation='softmax'))



model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
#epochs=250 batch_size=8
#model.fit(X, y, epochs=250, batch_size=8)
model.fit(Dx, Dy, epochs=250, batch_size=8)

_, accuracy = model.evaluate(Dx, Dy)
print('Accuracy: %.2f' % (accuracy*100))

"""
name_of_file="features_flexaojoelho4.json"

f = open(name_of_file)
data_test = json.load(f)
f.close()


predictions = (model.predict(data_test) > 0.5).astype(int)

write_detection=[]

for i in range(len(data_test)):
    if(predictions[i][0] == 0 and predictions[i][1] == 0 and predictions[i][2] == 1):   
        write_detection.append([i,"agachamento"])
    elif(predictions[i][0] == 0 and predictions[i][1] == 1 and predictions[i][2] == 0):   
        write_detection.append([i,"extensaoquadril"])
    elif(predictions[i][0] == 1 and predictions[i][1] == 0 and predictions[i][2] == 0):   
        write_detection.append([i,"flexaojoelho"])    
    else:   
        write_detection.append([i,"no_detection"])

with open("output_"+name_of_file, 'w') as f:
    json.dump(write_detection, f)
"""    

model.save("detectionModel3")
