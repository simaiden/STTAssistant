# SSTAssistant
Proyecto para curso EL5003 Taller de Proyecto

Librerías:

- <code> pip install SpeechRecognition </code>
- <code>pip install PyAudio </code>
- <code>pip install -U scikit-learn</code> o <code>conda install scikit-learn</code>


Problemas sacados de <link> https://www.cronoshare.com/blog/10-averias-comunes-en-un-movil/ </code> 

Pasos que sigue programa:
- Genera vectores para cada uno de los documentos (problemas) utilizando algoritmo Bag of Words.
- Aplica transformación TF-IDF a los vectores (normaliza vectores restando importancia a palabras que se repiten mucho, como <i>'a' 'de' 'para' </i>, y le añade importancia a palabras relevantes (que se repiten menos).
- Con la frase transformada con SST se aplica knn (k-nearest neighbors) con los problemas y entrega el ranking.


Correr archivo principal <code> demo_asistente.py</code> y para pruebas <code> pruebas.py </code>

