import stt_func

#sacadas de https://www.cronoshare.com/blog/10-averias-comunes-en-un-movil/
allsentences = ["Un uso continuado del móvil puede hacer que comience a ir lento. Si las aplicaciones tardan una eternidad en abrirse o acciones básicas como mirar la agenda o realizar una llamada tardan demasiado en efectuarse, significa que el terminal está sobrecargado de datos.Recuerda ir borrando la memoria caché de las aplicaciones de vez en cuando. También haz limpieza de archivos antiguos que ya no necesites: fotos, vídeos, audios, documentos… Aun así, la opción más efectiva es realizar una copia de seguridad de todos los archivos importantes y formatear el terminal entero. Al restaurarlo a su estado fábrica, su velocidad y rendimiento serán mucho mayores.",
"Los smartphone no se caracterizan por la amplia duración de su batería. Además, es muy común que, según vaya pasando el tiempo, esta funcione cada vez peor. Las baterías tienen una vida de entre dos y tres años, por lo que es recomendable cambiarlas cuando cumplen ese periodo. Si no se cambian pueden sobrecalentarse y/o deteriorarse y causar problemas internos graves, además de acortar en exceso su duración.",
"Este es uno de los problemas con más fácil solución, pero aún así puede ser todo un incordio. Cada vez hay más apps atrayentes que queremos tener en nuestro móvil, pero el espacio del terminal es limitado. Esto se suma a la gran cantidad de información que recibimos a diario en forma de vídeos e imágenes. Este problema generará molestos mensajes en los que se indicará que no tenemos espacio libre, y, además de que afectará al rendimiento de nuestro móvil, algunas funciones pueden quedar desactivadas.La solución más sencilla es adquirir una tarjeta microSD del tamaño deseado. Así podremos almacenar ahí toda nuestra música, fotos y demás archivos. Además, algunas aplicaciones pueden moverse a esta tarjeta para que dejen de ocupar espacio en la memoria interna.",
"Como hemos comentado, los smartphones son como ordenadores en miniatura. Esto quiere decir que, al igual que una computadora, pueden quedar infectados de virus. Muy pocos usuarios instalan antivirus en sus móviles, ocasionando que los virus se introduzcan en ellos a través de alguna descarga malintencionada.",
"El conector de carga del móvil es una de las partes que más toqueteamos. Tener que cargar el móvil a diario hace que estemos introduciendo una y otra vez el cable en el conector de carga. Si no somos cuidadosos y lo hacemos de forma brusca podemos torcer alguna clavija. El resultado será que ningún cargador hará contacto, no podremos cargar el móvil y tendremos que acudir a un servicio técnico para arreglarlo.",
"Muchas veces el móvil puede llegar a sobrecalentarse en exceso. A veces este problema viene derivado por una batería defectuosa o un mal rendimiento del software. Este calor puede ser fatal para el teléfono y su mecanismo interno, por lo que hay que intentar identificar rápidamente sus causas.Comprueba que no tengas muchas aplicaciones actuando en segundo plano y cierra todas las que no vayas a usar. Intenta además no utilizar el móvil muchas horas seguidas, dejándole descansar. Apagarlo de vez en cuanto también es una opción para que no sufra sobrecalentamientos, sobre todo en climas muy calurosos.",
"Si el móvil comienza a apagarse o reiniciarse solo, puede tener un grave problema interno. Este puede estar ocasionado por un virus o por defectos en el software o hardware. Si consigues llegar a las opciones, intenta formatearlo devolviéndolo a su estado de fábrica. Si no esto no funciona, el servicio técnico tendrá que hacerse cargo del problema.",
"Debido a golpes, humedad o problemas de hardware o software, el audio puede dejar de funcionar de repente en nuestro móvil. La solución pasa una vez más por devolverlo a su estado de fábrica, aunque en la mayoría de los casos se habrá soltado un chip interno que habrá que volver a soldar."]


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
          "n_neighbors":3}


stt_func.applySTTassistant(params)




