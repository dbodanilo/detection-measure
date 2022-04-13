import sys
import json
import math
import os
import glob

def convertDegreeToRadian(degree):
    return ((degree*math.pi)/180)

def convertRadianToDegree(radian):
    return ((radian*180)/math.pi)

def anglesForArms(data):

    if (data[1][0]==0 and data[1][1]==0) or (data[8][0]==0 and data[8][1]==0) or (data[3][0]==0 and data[3][1] ==0):
        return 0;
    
    ax=data[1][0] - data[3][0]
    ay=data[1][1] - data[3][1]
    a = math.sqrt(pow(ax,2) + pow(ay,2))

    bx=data[1][0] - data[8][0]
    by=data[1][1] - data[8][1]
    b = math.sqrt(pow(bx,2) + pow(by,2))
    
    cx=data[3][0] - data[8][0]
    cy=data[3][1] - data[8][1]
    c = math.sqrt(pow(cx,2) + pow(cy,2))

    cos0 = pow(c,2) - pow(a,2) - pow(b,2)
    cos0 = cos0/(-2*a*b)

    inverse_cos0 = math.acos(cos0)
    
    return convertRadianToDegree(inverse_cos0)
    

def anglesForBackbone(data):

    if (data[1][0]==0 and data[1][1] ==0) or (data[8][0]==0 and data[8][1] ==0) or (data[10][0]==0 and data[10][1] ==0):
        return 0;
    
    ax=data[1][0] - data[8][0]
    ay=data[1][1] - data[8][1]
    a = math.sqrt(pow(ax,2) + pow(ay,2))

    bx=data[8][0] - data[10][0]
    by=data[8][1] - data[10][1]
    b = math.sqrt(pow(bx,2) + pow(by,2))
    
    cx=data[1][0] - data[10][0]
    cy=data[1][1] - data[10][1]
    c = math.sqrt(pow(cx,2) + pow(cy,2))

    cos0 = pow(c,2) - pow(a,2) - pow(b,2)
    cos0 = cos0/(-2*a*b)

    inverse_cos0 = math.acos(cos0)
    
    return convertRadianToDegree(inverse_cos0)


def anglesForKnees(data):

    if (data[9][0]==0 and data[9][1] ==0) or (data[10][0]==0 and data[10][1] ==0) or (data[11][0]==0 and data[11][1] ==0):
        return 0;
    
    ax=data[9][0] - data[10][0]
    ay=data[9][1] - data[10][1]
    a = math.sqrt(pow(ax,2) + pow(ay,2))

    bx=data[10][0] - data[11][0]
    by=data[10][1] - data[11][1]
    b = math.sqrt(pow(bx,2) + pow(by,2))
    
    cx=data[9][0] - data[11][0]
    cy=data[9][1] - data[11][1]
    c = math.sqrt(pow(cx,2) + pow(cy,2))

    cos0 = pow(c,2) - pow(a,2) - pow(b,2)
    cos0 = cos0/(-2*a*b)

    inverse_cos0 = math.acos(cos0)
    
    return convertRadianToDegree(inverse_cos0)


def anglesBetweenLegs(data):

    if (data[10][0]==0 and data[10][1] ==0) or (data[12][0]==0 and data[12][1] ==0) or (data[13][0]==0 and data[13][1] ==0):
        return 0;
    
    ax=data[12][0] - data[10][0]
    ay=data[12][1] - data[10][1]
    a = math.sqrt(pow(ax,2) + pow(ay,2))

    bx=data[12][0] - data[13][0]
    by=data[12][1] - data[13][1]
    b = math.sqrt(pow(bx,2) + pow(by,2))
    
    cx=data[10][0] - data[13][0]
    cy=data[10][1] - data[13][1]
    c = math.sqrt(pow(cx,2) + pow(cy,2))

    cos0 = pow(c,2) - pow(a,2) - pow(b,2)
    cos0 = cos0/(-2*a*b)

    inverse_cos0 = math.acos(cos0)
    
    return convertRadianToDegree(inverse_cos0)

exercices=['agachamento', 'extensaoquadril', 'flexaojoelho']
directory=["baseDeTeste\\testeAgachamento\\"+exercices[0], "baseDeTeste\\testeExtensaoQuadril\\"+exercices[1], "baseDeTeste\\testeFlexaoJoelho\\"+exercices[2]]

for index in range(3):
    for k in range(9):
        contents = []
        json_dir_name = directory[index]+str(k+1)
        json_pattern = os.path.join(json_dir_name, '*.json')
        file_list = glob.glob(json_pattern)
        set_angles=[]
        for file in file_list:
            contents.append(file)
   
        if len(contents) > 0:
            for file_name in contents:
                f = open(file_name)
                data = json.load(f)
                if not data['people']:
                  continue
    
                all_data = data['people'][0]
                points = []
                points_array = []
                angles_per_frame = []

                for i in range(len(all_data['pose_keypoints_2d'])):
                   points.append(all_data['pose_keypoints_2d'][i])  
                   if (i+1)%3 ==0:
                      points_array.append(points)
                      points=[]

                angles_per_frame.append(anglesForArms(points_array))
                angles_per_frame.append(anglesForBackbone(points_array))
                angles_per_frame.append(anglesForKnees(points_array))
                angles_per_frame.append(anglesBetweenLegs(points_array))
    
                set_angles.append(angles_per_frame)
                f.close()
        path_to_save="features_"+exercices[index]+str(k+1)+".json"           
        with open(path_to_save, 'w') as f:
           json.dump(set_angles, f)
    
