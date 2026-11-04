# **Práctica: Sistema de conducción autónoma mediante visión artificial con OpenCV** 

**Asignatura:** Fundamentos de los Sistemas Inteligentes 

**Titulación:** Grado en Ciencia e Ingeniería de Datos 

**Universidad:** Universidad de Las Palmas de Gran Canaria (ULPGC) 

## **1. Introducción** 

Uno de los componentes fundamentales de los sistemas de conducción autónoma es la capacidad de interpretar el entorno a partir de las imágenes capturadas por cámaras instaladas en el vehículo. 

Entre las tareas más habituales de estos sistemas se encuentra la detección de las marcas viales que delimitan los carriles de circulación. Esta información permite conocer la posición aproximada del vehículo respecto a la carretera, identificar cambios en el trazado y reconocer situaciones como curvas, bifurcaciones o cambios de carril. 

En esta práctica se desarrollará un sistema simplificado de seguimiento de carril utilizando Python y la biblioteca OpenCV. 

El sistema analizará una grabación de vídeo realizada desde un vehículo en movimiento y deberá identificar y seguir las marcas viales que delimitan la parte derecha del carril. 

El objetivo no es implementar un sistema completo de conducción autónoma, sino desarrollar algunos de los mecanismos básicos de percepción visual utilizados en este tipo de aplicaciones. 

## **2. Objetivos** 

Los principales objetivos de la práctica son: 

- Familiarizarse con el procesamiento de secuencias de vídeo utilizando OpenCV. 

- Aplicar técnicas de preprocesamiento y filtrado de imágenes. 

- Utilizar algoritmos de detección de bordes, como Canny. 

- Aplicar técnicas de detección de líneas mediante la transformada de Hough. 

- Identificar y seleccionar regiones de interés dentro de una imagen. 

- Desarrollar estrategias para localizar y seguir marcas viales. 

- Analizar la evolución temporal de los elementos detectados. 

- Resolver situaciones progresivamente más complejas, como curvas, interrupciones de líneas, cambios de carril o paso por zonas de sombra. 

## **3. Material proporcionado** 

Se facilitará una grabación de vídeo obtenida desde una cámara situada en la parte delantera de un vehículo. 



Durante el recorrido aparecen diferentes situaciones: 

- Circulación por un tramo de carretera aproximadamente recto. 

- Aparición de curvas suaves. 

- Aparición de curvas más pronunciadas. 

- Paso bajo zona de sombra 

- Transición entre marcas viales continuas y discontinuas. 

- Aparición de líneas discontinuas de mayor grosor. 

- Cambio de carril hacia la derecha y circulación por una salida de la vía. 

Estas situaciones tendrán distintos grados de dificultad que se tendrán en cuenta durante la evaluación de la práctica. 

## **4. Descripción del problema** 

Se deberá implementar una aplicación que procese el vídeo proporcionado y sea capaz de identificar y seguir la marca vial que delimita la parte derecha del carril por el que circula el vehículo. 

Inicialmente, esta delimitación corresponde a una línea blanca continua fácilmente reconocible. Sin embargo, conforme avanza el vídeo, su posición y orientación cambian debido a las curvas de la carretera. Además, se producirán situaciones en las que la delimitación será discontinua o aparecerán nuevas marcas viales debido a la presencia de una salida. 

El sistema deberá intentar mantener correctamente la referencia de seguimiento durante todo el recorrido. 

Se valorará especialmente que las soluciones sean capaces de adaptarse a estos cambios sin perder la marca vial ni confundirla con otros elementos de la escena. 

## **5. Procesamiento del vídeo** 

La aplicación deberá emplear las técnicas de procesamiento de imágenes estudiadas en la asignatura. Cada estudiante o grupo deberá seleccionar y combinar aquellas que considere más adecuadas, justificando las decisiones adoptadas. Cuando no sea posible detectar con suficiente fiabilidad la marca vial, el sistema podrá utilizar información de los fotogramas anteriores para estimar temporalmente su posición. El programa deberá mostrar el vídeo original con los resultados del procesamiento superpuestos. La representación deberá permitir identificar claramente la marca vial que está siguiendo el sistema. 

Se valorarán los siguientes aspectos: 

- Correcta localización de la marca vial. 

- Continuidad temporal del seguimiento. 

- Adaptación a diferentes geometrías de la carretera. 

- Capacidad para recuperar el seguimiento después de una pérdida temporal. 

- Comportamiento ante líneas discontinuas. 

- Gestión de las transiciones entre distintas marcas viales. 

## **6. Defensa y entregables** 

La práctica deberá defenderse por ambos miembros de la pareja. Cada alumno/a debe demostrar un conocimiento profundo de cada parte del software por la que se le pregunte. El código no debe incorporar ningún tipo de comentario explicativo. Para cualquier parámetro de cada función utilizada debe conocerse su utilidad. Cualquier solución de código adoptada debe poder justificarse. 

En su momento se informará sobre la opción en el campus virtual para la entrega de la práctica. 

