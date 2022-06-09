import cv2
import os
from gtts import gTTS
from playsound import playsound




dataPath = 'C:/Users/Maria/Desktop/openCvPy/data' #Cambia a la ruta donde hayas almacenado Data
imagePaths = os.listdir(dataPath)
print('imagePaths=',imagePaths)

# face_recognizer = cv2.face.EigenFaceRecognizer_create()
# face_recognizer = cv2.face.FisherFaceRecognizer_create()
face_recognizer = cv2.face.LBPHFaceRecognizer_create()

# Leyendo el modelo
# face_recognizer.read('modeloEigenFace.xml')
# face_recognizer.read('modeloFisherFace.xml')
face_recognizer.read('modeloLBPHFace.xml')

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
# cap = cv2.VideoCapture('C:/Users/Maria/Desktop/openCvPy/ImaYvid/data/hombres_CST/Alejandro_Widmer_ANI_DIG.mp4')

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

while True:
    ret,frame = cap.read()
    if ret == False: break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = gray.copy()

    faces = faceClassif.detectMultiScale(gray,1.3,5)
# 
    for (x,y,w,h) in faces:
        rostro = auxFrame[y:y+h,x:x+w]
        rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
        result = face_recognizer.predict(rostro)
        print(result)
        cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)

                # EigenFaces
        # if result[1] < 5700:
        #     cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
        #     cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
        # else:
        #     cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
        #     cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)



                # FisherFace
        # if result[1] < 500:
        #     cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
        #     cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
        # else:
        #     cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
        #     cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)

                # LBPHFace
        if result[1] < 70:
            cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
            # print(imagePaths[result[0]])
            
            name = (imagePaths[result[0]])

# ***********************************************************************************************

            def nombre (name):

                    if name == 'Gabriel Rodriguez' or name == 'Javiera Tuki':

                        tts = gTTS('Aqui esta' + name, lang='es-us')
                        tts.save("persona.mp3")
                        playsound('persona.mp3')
                        os.remove('persona.mp3')
                        return nombre   

            while name != name:
                nombre(name)

# ***********************************************************************************************




                # return nombre
            
            # while name == name:

            #     tts = gTTS('Aqui esta' + name, lang='es-us')
            #     with open ("persona.mp3", "wb") as archivo:
            #         tts.save(archivo)
            # else:

            #     playsound ('persona.mp3')

            

        else:
            cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
            
            # playsound('Desconocido.mp3')

        
    cv2.imshow('frame',frame)
    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()