import numpy as np
import stt_func
#sacadas de https://www.cronoshare.com/blog/10-averias-comunes-en-un-movil/


allsentences = np.load('allsentences.npy',allow_pickle=True)
problems = {0:"Un rendimiento extremadamente lento",
1:"Batería defectuosa con el tiempo",
2:"La falta de memoria interna",
3:"El ataque de los virus",
4:"Conector de carga estropeado",
5:"El móvil está muy caliente",
6:"El móvil se apaga o reinicia solo",
7:"Problemas de audio"}





params = {"sentences": allsentences,
          "problems": problems,
          "n_neighbors":2}




#print(X.toarray().shape)

stt_audio = "telefono se apaga solo"
stt_func.getSoluciones(params,stt_audio)


'''import webbrowser

webbrowser.open('http://example.com')'''

