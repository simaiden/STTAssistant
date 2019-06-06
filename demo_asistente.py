import stt_func
import numpy as np

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
          



input('Bienvenido a SSTAssitant, presione una tecla para continuar...')
stt_func.applySTTassistant(params)






