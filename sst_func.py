import speech_recognition as sr
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.neighbors import NearestNeighbors


def getSoluciones(params ,sst_audio):
    
    allsentences = params['sentences']
    problems = params['problems']
    n_neighbors = params['n_neighbors']

    #sst_audio = "mi telefono se apaga solo"
    allsentences.append(sst_audio)

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



def applySSTassistant(params):
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Di algo")
        audio = r.listen(source)
        print("Gracias")
        
    try: 
        recognize_audio = r.recognize_google(audio, language='es-ES')
        #sst_word = recognize_audio.split()
        #print(sst_word)
        print("texto: " + recognize_audio)
        getSoluciones(params,recognize_audio)
    except:
        print("No audio registrado")
        pass