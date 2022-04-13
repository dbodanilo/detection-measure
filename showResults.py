import numpy as np
import cv2
import json
name='agachamento7'
cap = cv2.VideoCapture('videos/agachamento/'+name+'.mp4')
f = open("output_features_"+name+".json")
data_test = json.load(f)
f.close()

font_size=0.5

l_dist=0
r_dist=5
color=(0, 255, 255)

f = open("output_noisy_features_"+name+".json")
data_test_noisy = json.load(f)
f.close()

map_wrong_position={(0,1,0,0,0,0): ['posicao errada dos bracos', 'angulo acima de 123 graus', 'angulo entre 2 e 5 graus, levante um pouco os bracos'],#agachamento
  (0,0,1,0,0,0): ['posicao errada do quadril','angulo acima de 170 graus','angulo entre 2 e 5 graus'],#agachamento
  (0,0,0,0,0,1): ['posicao errada dos bracos e quadril','braco > 123 quadril >140 ' ],#agachamento
  (0,0,0,1,0,0): ['posicao errada do quadril','angulo menor que 140 graus'],#extensaoquadril
  (0,0,0,0,1,0): ['posicao errada das pernas','angulo maior que 27 graus'],#joelho
  (1,0,0,0,0,0): ['exercicio feito corretamente'],
  (1,1,1,1,1,1): ['nada identificado']                  }
                    

total_frame=0
while(cap.isOpened()):
  ret, frame = cap.read()
  tupla=tuple(data_test_noisy[total_frame][8])
  index=0
  font = cv2.FONT_HERSHEY_SIMPLEX
  if not tupla in map_wrong_position:
    tupla=(1,1,1,1,1,1)
    text_1="exercicio: " + data_test[total_frame][1]
    text_2="status: " + map_wrong_position[tupla][0]
    cv2.putText(frame,text_1, (l_dist, r_dist+20), font, font_size, color, 2, cv2.LINE_4)
    cv2.putText(frame,text_2, (l_dist, r_dist+40), font, font_size, color, 2, cv2.LINE_4)
  else:
    if tupla == (0,1,0,0,0,0):
      index=1
      if not data_test_noisy[total_frame][4] >=123:
        index=2
    if tupla == (0,0,0,0,0,1):
      index=1
    if tupla == (0,0,1,0,0,0):
      index=1
      if not data_test_noisy[total_frame][5] >=170:
        index=2
    if tupla == (0,0,0,1,0,0) or  tupla ==(0,0,0,0,1,0):
      index=1

    if index ==0:
      aux=map_wrong_position[tupla]
      text_1="exercicio: " + data_test[total_frame][1]
      text_2="status: " + aux[index]
      cv2.putText(frame,text_1, (l_dist, r_dist+20), font, font_size, color, 2, cv2.LINE_4)
      cv2.putText(frame,text_2, (l_dist, r_dist+40), font, font_size, color, 2, cv2.LINE_4)
    
    if not index ==0:
      
      if tupla == (0,0,0,1,0,0) and data_test[total_frame][1] == 'agachamento':
        tupla=(0,0,1,0,0,0)

      aux=map_wrong_position[tupla]
      text_1="exercicio: " + data_test[total_frame][1]
      text_2="status: " + aux[0]
      text_3="recomendacao: " + aux[index]
      cv2.putText(frame,text_1, (l_dist, r_dist+20), font, font_size, color, 2, cv2.LINE_4)
      cv2.putText(frame,text_2, (l_dist, r_dist+40), font, font_size, color, 2, cv2.LINE_4)
      cv2.putText(frame,text_3, (l_dist, r_dist+60), font, font_size, (0, 255, 0), 2, cv2.LINE_4)
      

  total_frame=total_frame+1
  cv2.imshow('frame',frame)
  if cv2.waitKey(3000) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()

