#FUNCIONES PARA ANÁLISIS DE PLAGIO DE TEXTOS 
#Librerias que necesitarían descargar 
import docx2txt, fitz, nltk
import pandas as pd
import numpy as np
#Ya viene incorporado en python 3 
from os import remove

#Métrica de Kullback-Leibler para decir si dos textos contienen potencialmente los mismos conceptos
#los argumentos deben ser elementos txt 
def K_L(sospechoso,original):

#Convertimos los vectores en variables nltk.probability.freqdist 
    freqs=nltk.FreqDist(sospechoso.split())
    freqd=nltk.FreqDist(original.split())

    vocabularys=set(sospechoso.split())
    vocabularyd=set(original.split())
    inter=sorted(vocabularys & vocabularyd)
    P=[]
    Q=[]
#Calculamos las imágenes de las distribuciones 
    for word in inter:
        P=np.append(P,freqd.freq(word))
        Q=np.append(Q,freqs.freq(word))

#Calculamos el valor de la función Kullback-Leibler
    KL=sum(P*np.log(P/Q))
    return(KL)
    
#Conversión de archivos pdf a txt, path=Ruta del archivo pdf
def pdf_to_txt(path):

    documentpdf=fitz.open(path)
    salida=open("extraible.txt","wb")
    for page in documentpdf:
        text=page.getText().encode("utf8")
        salida.write(text)
        salida.write(b'\n-----\n')
    salida.close()
    new=open("extraible.txt",encoding="utf8")
    document=new.read()
    new.close() 
    remove("extraible.txt")
    return(document)
    
#path = ruta del archivo docx
def docx_to_txt(path):

    documentdocx=docx2txt.process("sospechoso.docx")
    return(documentdocx)

#Funciòn de anàlisis de n-grammas, suspect y original son argumentos de tipo txt 
def n_gramma_test(sospechoso,original):

#Deconstruimos el texto en un conjunto de palabras (sin repeticiones) y obtenemos el vocabulario
    vocabularys=set(sospechoso.split())
    vocabularyd=set(original.split())
    
#identificamos las palabras que comparten y las separamos por n-grammas para calcular la medida de contención para cada n=1,2,...,máxima longitud
    g1=set()
    g2=set()
    g3=set()
    g4=set()
    g5=set()
    g6=set()
    g7=set()
    G1=set()
    G2=set()
    G3=set()
    G4=set()
    G5=set()
    G6=set()
    G7=set()
#Calculamos los conjuntos de n-grammas en la intersección
    intersec=sorted(vocabularyd & vocabularys)
    
    for i in intersec:
        if len(i)==1:
            g1= g1 | set([i])
        if len(i)==2:
            g2= g2 | set([i])
        if len(i)==3:
            g3= g3 | set([i])
        if len(i)==4:
            g4= g4 | set([i])
        if len(i)==5:
            g5= g5 | set([i])
        if len(i)==6:
            g6= g6 | set([i])
        if len(i)==7:
            g7= g7 | set([i])
        
#Calculamos los n-gramas en el documento sospechoso
    for i in sorted(vocabularys):
        if len(i)==1:
            G1= G1 | set([i])
        if len(i)==2:
            G2= G2 | set([i])
        if len(i)==3:
            G3= G3 | set([i])
        if len(i)==4:
            G4= G4 | set([i])
        if len(i)==5:
            G5= G5 | set([i])
        if len(i)==6:
            G6= G6 | set([i])
        if len(i)==7:
            G7= G7 | set([i])
            
#Mostramos el análisis de n-grammas mediante un Data Frame (si la medida de conteción de un n-gramma es alto cuando n es mayor a 3 es muy probable que sea plagio) 
    tablen=pd.DataFrame({"n-gramma":["1-gramma","2-gramma","3-gramma","4-gramma","5-gramma","6-gramma","7-gramma"],
                    "medida de contención":[len(g1)/len(G1),len(g2)/len(G2),len(g3)/len(G3),len(g4)/len(G4),len(g5)/len(G5),len(g6)/len(G6),len(g7)/len(G7)]})     
    return(tablen)


    

