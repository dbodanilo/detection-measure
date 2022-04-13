import json
from sklearn.utils import shuffle
from numpy import loadtxt
import keras
from keras.models import Sequential
from keras.layers import Dense

model = keras.models.load_model("detectionModel3")

name_of_file="features_agachamento7.json"

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
    
