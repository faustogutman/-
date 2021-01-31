import pandas as pd
pd.set_option('display.max_colwidth', -1)
import random

sheelot=pd.read_excel('sheelotsherut.xlsx') #לשים פה את הפס אל הקובץ הרלבנתי שלכם
sheelot.replace('  ',' ').replace('  ',' ').replace('   ',' ').replace('    ',' ')
sheelot['אפשרות']=sheelot['אפשרות'].apply(lambda x: x+ '.         ')

preguntas=list(sheelot['קוד שאלה'].drop_duplicates())
# preguntas

for i in preguntas:
    hola=sheelot[sheelot['קוד שאלה']==i]
    opciones=hola.shape[0]
    opciones
    Q_opciones = list(range(opciones))
    buenas=random.sample(range(opciones), 1)
    buenas[0]
    #Generate 5 random numbers between 10 and 30
    goodoptions = random.sample(range(opciones), buenas[0])
    goodoptions
    # print(goodoptions)
    chau = list(range(opciones))
    # print(chau)
    notgoodoption = list(set(chau) - set(goodoptions))
    # print(notgoodoption)
    optiontoshow=hola.iloc[goodoptions,[3,6]]
    optiontoshow=optiontoshow.append(hola.iloc[notgoodoption,[3,7]].copy())
    optiontoshow['אופציות']=optiontoshow['תיאור נכון'].fillna(optiontoshow['תיאור לא נכון'])
    # optiontoshow[['אפשרות','אופציות']].sort_values(by='אפשרות')
    final=list(hola['אפשרות'].iloc[goodoptions])
    final.sort()
    finalrespuesta=' שאלה: ' +str(hola.iloc[0,2]) +'  אופציות נכונות:  ' + ', '.join([str(elem) for elem in final])


    print( 'שאלה:' , hola.iloc[0,2] , file=open("pruebas.txt", "a"))
    print(hola.iloc[0,4] , file=open("pruebas.txt", "a"))
    print(hola.iloc[0,5], file=open("pruebas.txt", "a"))
    print(optiontoshow[['אפשרות','אופציות']].sort_values(by='אפשרות').to_string(index=False), file=open("pruebas.txt", "a"))
    print('\n\n\n' + finalrespuesta, file=open("pruebas.txt", "a"))
    #     print('%let trik=0;', file=open("output.sas", "a"))

    print('\n\n\n\n\n'  , end='\n', file=open("pruebas.txt", "a"))
    
    print( 'שאלה:' , hola.iloc[0,2])
