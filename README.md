# FSI — Práctica AutoPilot

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)](https://opencv.org/)

Sistema educativo de detección y seguimiento de la marca vial derecha mediante visión artificial en Python y OpenCV.

El proyecto procesa un vídeo grabado desde el vehículo, aplica preprocesamiento y segmentación de región de interés, detecta líneas con la transformada de Hough, sigue la línea entre fotogramas y permite identificar posibles cambios de carril. Forma parte de la práctica de **Fundamentos de los Sistemas Inteligentes** del Grado en Ciencia e Ingeniería de Datos (ULPGC).

## Características

- Preprocesamiento con escala de grises, suavizado gaussiano y detección de bordes Canny.
- Región de interés configurable para limitar el análisis a la zona útil de la carretera.
- Detección probabilística de segmentos mediante `cv2.HoughLinesP`.
- Filtrado por pendiente y cercanía temporal.
- Suavizado del seguimiento entre fotogramas y recuperación ante pérdidas temporales.
- Visualización de segmentos detectados, línea estimada y estado del seguimiento.
- Alerta visual para posibles cambios de carril.
- Controles interactivos para pausar, navegar por fotogramas y salir.
- Exportación del vídeo procesado en `autopilot_paso6.py`.

## Requisitos

- Python 3.8 o posterior.
- OpenCV para Python (`opencv-python`).
- NumPy.
- Entorno gráfico compatible con ventanas OpenCV.
- Códec MP4/H.264 o MPEG-4 disponible para reproducir el vídeo de entrada y generado.

No existe un archivo de dependencias en el repositorio. Instala manualmente las principales bibliotecas:

```bash
python -m pip install --upgrade pip
python -m pip install opencv-python numpy
```

## Instalación

```bash
git clone https://github.com/alvarogomez102-source/FSI---Practica-AutoPilot.git
cd FSI---Practica-AutoPilot
python -m pip install opencv-python numpy
```

Conserva la estructura original, ya que los scripts esperan el vídeo en `imgs/PracticaAutoPilot.mp4`.

## Uso

Ejecuta el script correspondiente al nivel o versión que quieras probar:

```bash
python autopilot_paso1.py
python autopilot_paso2.py
python autopilot_paso3.py
python autopilot_paso4.py
python autopilot_paso5.py
python autopilot_paso6.py
```

Ejemplo básico:

```bash
python autopilot_paso6.py
```

El script final abre dos ventanas: la vista procesada y el resultado de Canny limitado por la región de interés. Al terminar, genera:

```text
imgs/PracticaAutoPilot_resultado.mp4
```

## Evolución por pasos

| Archivo | Funcionalidad principal |
|---|---|
| [`autopilot_paso1.py`](autopilot_paso1.py) | Canny con umbrales ajustables y visualización de la región de interés. |
| [`autopilot_paso2.py`](autopilot_paso2.py) | Detección de segmentos, filtro angular y ajuste inicial de la línea. |
| [`autopilot_paso3.py`](autopilot_paso3.py) | Seguimiento temporal, suavizado y estado detectado/estimado. |
| [`autopilot_paso4.py`](autopilot_paso4.py) | Alerta de cambio de carril y recuento de líneas detectadas. |
| [`autopilot_paso5.py`](autopilot_paso5.py) | Pausa, avance manual y navegación hacia atrás por fotogramas. |
| [`autopilot_paso6.py`](autopilot_paso6.py) | Versión final: exportación MP4 y presentación de información de seguimiento. |

## Controles

| Tecla | Acción |
|---|---|
| `Esc` | Finalizar la reproducción y cerrar las ventanas. |
| `Espacio` | Pausar o reanudar (paso 5 y posteriores). |
| `←` | Retroceder y procesar de nuevo un fotograma (paso 5 y posteriores). |
| `→` | Avanzar manualmente un fotograma (paso 5 y posteriores). |

En los primeros pasos, `Espacio` puede congelar la ejecución hasta pulsarlo de nuevo.

## Archivos del proyecto

- [`EnunciadoPracticaAutoPilot.md`](EnunciadoPracticaAutoPilot.md): enunciado, objetivos y requisitos de la práctica.
- [`imgs/`](imgs/): vídeos de entrada usados por los scripts.
- `.gitignore`: excluye los vídeos de salida generados por el paso 6.

## Personalización

Los parámetros principales están definidos como constantes al inicio de cada script:

- `VIDEO`: ruta del vídeo de entrada.
- `ROI`: coordenadas del polígono de análisis.
- `ANGULO_MIN` y `ANGULO_MAX`: margen angular de las líneas válidas.
- `DISTANCIA_MAX`: tolerancia para comparar segmentos entre fotogramas.
- `SUAVIZADO`: peso temporal aplicado al seguimiento.
- `MAX_PERDIDOS`: fotogramas consecutivos permitidos sin detección antes de reiniciar.
- `MARGEN_CARRIL`: proximidad a los límites que activa la alerta.

## Ayuda y soporte

- Consulta el [enunciado completo](EnunciadoPracticaAutoPilot.md) para los objetivos y criterios de la práctica.
- Abre una incidencia en la pestaña [Issues](../../issues) del repositorio si encuentras un problema reproducible.
- Incluye en el reporte la versión de Python, las versiones de OpenCV y NumPy, el sistema operativo y el script ejecutado.

## Mantenimiento y contribuciones

El proyecto está mantenido por [@alvarogomez102-source](https://github.com/alvarogomez102-source). Las contribuciones son bienvenidas mediante issues o pull requests.

Consulta [`CONTRIBUTING.md`](CONTRIBUTING.md) para las normas del proyecto y [`LICENSE`](LICENSE) para los términos de uso, una vez que esos archivos estén disponibles en el repositorio.
