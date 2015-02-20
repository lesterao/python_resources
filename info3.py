import os
from datetime import datetime, date, time, timedelta
import calendar

formato1 = "%H:%M:%S"
rootDir = '.'
ACTAnotados=0
nAction = 0
tAction = 0
nFrames = 0 #numero de frames anotados en cada video
tFrames = 0 #numero total de frames
TvideoAnotado = time(0,0,0) # Total de video anotado
TvideoAnotadoFile = time(0,0,0) # Total de video anotado en fichero
suma = time(0,0,0)
sumaf = time(0,0,0)

def writteACTFILE(dirName,fname,nFrames,sumaf,nAction):
    print(dirName,fname)
    index = fname.find('Mx')
    replace = fname[index:len(fname)-4]
    #print(replace)
    
    if os.access(dirName + "/" +"CITEDI_"+ str(nAction)+"ACT"+replace+".txt", os.X_OK):
        os.remove(dirName + "/" +"CITEDI_"+ str(nAction)+"ACT"+replace+".txt")
    else:
        f = open(dirName + "/" +"CITEDI_"+ str(nAction)+"ACT"+replace+".txt",'w')
        f.writelines("Frames Anotados Fichero: "+str(nFrames)+'\n')
        f.writelines("Total Video Anotado Fichero: "+str(sumaf)+'\n')
        f.writelines("Total Acciones Anotadas Fichero: "+str(nAction)+'\n')
        f.close()

def add_secs_to_time(timeval, secs_to_add):
    secs = timeval.hour * 3600 + timeval.minute * 60 + timeval.second
    secs += secs_to_add
    return time(secs // 3600, (secs % 3600) // 60, secs % 60)

for dirName, subdirList, fileList in os.walk(rootDir):
    #print('Directorio: %s'% dirName)
    for fname in fileList:
        #print('\t%s' % fname)
        dirname1 = dirName.replace('.\\','')
        #print(dirname1)
        if '&'+dirname1+'&' in fname and '.txt' in fname and '_ANN_' in fname:
            print('\t%s' % fname)
            try:
                f = open(dirName+"/"+fname)
                for line in f:
                    line = line.replace('\t','/')
                    line = line.replace(' ','-')
                    line = line.split('/')
                    tFrame = line[3].split(':')
                    
                    try:
                        #objeto_datetime = datetime.strptime(cadena1, formato1)
                        tFrame1 = tFrame[2].split('.')
                        H = time(int(tFrame[0]),int(tFrame[1]),int(tFrame1[0]))
                        suma = add_secs_to_time(TvideoAnotado,H.hour*3600+H.minute*60+H.second)    
                        sumaf = add_secs_to_time(TvideoAnotadoFile,H.hour*3600+H.minute*60+H.second)    
                        #cadena1 = H.strftime(formato1)
                        #TvideoAnotado=H
                        #suma = TvideoAnotado + datetime.timedelta(H) 
                        #print(suma)
                        
                    except ValueError as e:
                        print("")
                        #print("Es un Literal no se puede convertir")
                    except IndexError as i:
                        print("")
                        #print("Fuera de Indice no se puede acceder")
                    nFrames=nFrames+1
                    #print(line)
            except IOError as e:
                print("Uh oh! Esto no existe")
            #Acciones ACT anotadas
        if '&'+dirname1+'&' in fname and '.txt' in fname and 'ACTANN' in fname:
            ACTAnotados= ACTAnotados+1
            #print('\t%s' % fname)
            try:
                f = open(dirName+"/"+fname)
                for line in f:
                    line = line.replace('\t','/')
                    line = line.replace(' ','-')
                    nAction=nAction+1
                    #print(nAction)
            except IOError as e:
                print("Uh oh! Esto no existe")

            if f:
                if nAction > 0:
                    nAction=nAction-1
                #print(nAction)
                #f.close()
        
        #Frames anotados

            if f:
                nFrames=nFrames-1
                TvideoAnotado = suma
                tFrames+=nFrames
                tAction+=nAction
                print("Fichero: "+dirName+"/"+fname)
                print("Frames Anotados Fichero: "+str(nFrames))
                print("Total Video Anotado Fichero: "+str(sumaf))
                print("Total Acciones Anotadas Fichero: "+str(nAction))
                print("-------------------------------------------")
                writteACTFILE(dirName,fname,nFrames,sumaf,nAction)
                
                sumaf = time(0,0,0)
                nFrames=0
                nAction=0
                f.close()
print("**************Totales***************")
print("Total Video Anotado = "+ str(TvideoAnotado))
print("Total Frames Anotados= "+str(tFrames))
print("Total De Acciones Anotadas= "+str(tAction))    
