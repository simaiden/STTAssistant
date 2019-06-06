import speech_recognition as sr
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import webbrowser



def searchWebSolution(problem,phone='samsung'):
    to_search = problem
    # words = problem.split()
    # to_search = ''
    # for word in words:
    #     to_search = word + '%20'
    
    if(phone == 'samsung'):
        search_url = 'https://www.samsung.com/cl/support/search/?keyword={}'.format(to_search)
    if(phone == 'iphone'):
        search_url = 'https://support.apple.com/kb/index?page=search&q={}&product=&doctype=&currentPage=1&includeArchived=false&locale=es_CL&src=support_searchbox_main&type=organic'.format(to_search)
    webbrowser.open(search_url)

def getSoluciones(params ,stt_audio):
    
    allsentences = params['sentences']
    problems = params['problems']
    n_neighbors = params['n_neighbors']

    allsentences = np.append(allsentences,stt_audio)
    #allsentences.append(stt_audio)

    #Bag of Words + transformacion Tf-Idf 
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(allsentences)

    #Knn con n=2
    neigh = NearestNeighbors(n_neighbors=n_neighbors)
    #Se entrena sin el audio dado por la persona 
    neigh.fit(X.toarray()[:-1]) 

    #Entrega indice y distancia de vecinos mas cercanos para audio sst
    knn = neigh.kneighbors([X.toarray()[-1]])
    knn_index = knn[1][0]
    knn_distance = knn[0][0]

    print("Posibles problemas:\n")
    for i in range(n_neighbors):
        print("{}°. {}".format(i+1, problems[knn_index[i]]))

    for i in range(n_neighbors):
        searchWebSolution(problems[knn_index[i]])

def applySTTassistant(params):
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando problema...")
        audio = r.listen(source)
        print("Gracias\n")
        
    try: 
        recognize_audio = r.recognize_google(audio, language='es-ES')
        #sst_word = recognize_audio.split()
        #print(sst_word)
        print("Texto: " + recognize_audio)
        getSoluciones(params,recognize_audio)
    except:
        print("No audio registrado")
        pass