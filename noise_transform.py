import sys
import json
import math
import os
import glob
import random
from random import seed
from sklearn.utils import shuffle

file_name='all_features.json'
exercices=['agachamento', 'extensaoquadril', 'flexaojoelho']
exercices_data={'agachamento': [0,0,1], 'extensaoquadril': [0,1,0], 'flexaojoelho': [1,0,0]}

low_noise=300

f = open(file_name)
data = json.load(f)
f.close()

output={'agachamento': [], 'extensaoquadril': [], 'flexaojoelho': []}

braco_angles=[]
braco2_angles=[]
quadril_angles=[]
pernas_angles=[]
quadril_angles_2=[]

seed(1)
for _ in range(700):
    braco_angles.append(random.uniform(123.0, 160.0))
seed(2)
for _ in range(700):
    braco_angles.append(random.uniform(2.0, 5.0))

seed(3)
for _ in range(700):
    quadril_angles.append(random.uniform(150.0, 170.0))#170;180	

seed(4)
for _ in range(700):
    quadril_angles.append(random.uniform(10.0, 30.0))

seed(5)
for _ in range(len(data['flexaojoelho'])):
    pernas_angles.append(random.uniform(27.0, 35.0))    

seed(6)
for _ in range(1400):
    quadril_angles_2.append(random.uniform(105, 170)) 

seed(7)
for _ in range(1400):
     braco2_angles.append(random.uniform(40.0, 105.0)) 

braco_angles=shuffle(braco_angles, random_state=0)
braco2_angles=shuffle(braco2_angles, random_state=0)
quadril_angles=shuffle(quadril_angles, random_state=0)

service=[]

#aqui len do agachamento dentro do segundo for

for p in exercices:
    for k in range(len(data[p])):
        data_array=[]
        data_array.append(exercices_data[p])
        for aux in data[p][k]:
          data_array.append(aux)
        data_array.append([1,0,0,0,0,0])
        service.append(data_array)


for k in range(low_noise):
    data_array=[]
    data_array.append([0,0,1])
    for aux in data['agachamento'][k]:
      data_array.append(aux)
    data_array[1] = braco_angles[k]
    data_array.append([0,1,0,0,0,0])
    service.append(data_array)


for k in range(low_noise*2):
    data_array=[]
    data_array.append([0,0,1])
    for aux in data['agachamento'][k]:
      data_array.append(aux)
    data_array[2] = quadril_angles[k]
    data_array.append([0,0,1,0,0,0])
    service.append(data_array)
"""
for k in range(low_noise):
    data_array=[]
    data_array.append([0,0,1])
    for aux in data['agachamento'][k]:
      data_array.append(aux)
    data_array[1] = braco_angles[k]
    data_array[2] = quadril_angles[k]
    data_array.append([0,0,0,0,0,1])
    service.append(data_array)            
"""

for k in range(low_noise):
    data_array=[]
    data_array.append([0,1,0])
    for aux in data['extensaoquadril'][k]:
      data_array.append(aux)
    data_array[3] = quadril_angles_2[k]
    data_array.append([0,0,0,1,0,0])
    service.append(data_array)

for k in range(low_noise):
    data_array=[]
    data_array.append([0,1,0])
    for aux in data['extensaoquadril'][k]:
      data_array.append(aux)
    data_array[1] = braco2_angles[k]
    data_array.append([0,0,0,1,0,0])
    service.append(data_array)
  
for k in range(low_noise*2):
    data_array=[]
    data_array.append([1,0,0])
    for aux in data['flexaojoelho'][k]:
      data_array.append(aux)
    data_array[4] = pernas_angles[k]
    data_array.append([0,0,0,0,1,0])
    service.append(data_array)

service = shuffle(service, random_state=0)

array_to_save=service

array_to_save = shuffle(array_to_save, random_state=0)

with open('all_features_low_noisy_5.json', 'w') as f:
    json.dump(array_to_save, f)

