import cv2
import numpy as np

VIDEO = "imgs/PracticaAutoPilot.mp4"
ROI = np.array([[(520, 540), (1180, 540), (800, 285), (560, 285)]], dtype=np.int32)
Y_ABAJO = 540
Y_ARRIBA = 300
ANGULO_MIN = 20
ANGULO_MAX = 75
DISTANCIA_MAX = 60
SUAVIZADO = 0.7
MAX_PERDIDOS = 15
MARGEN_CARRIL = 40


def preprocesar(frame):
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    suave = cv2.GaussianBlur(gris, (5, 5), 0)
    return cv2.Canny(suave, 50, 150)


def aplicar_roi(bordes):
    mascara = np.zeros_like(bordes)
    cv2.fillPoly(mascara, ROI, 255)
    return cv2.bitwise_and(bordes, mascara)


def detectar_segmentos(bordes):
    lineas = cv2.HoughLinesP(bordes, 1, np.pi / 180, 30, minLineLength=40, maxLineGap=60)
    if lineas is None:
        return []
    return lineas.reshape(-1, 4).tolist()


def filtrar_derecha(segmentos):
    validos = []
    for x1, y1, x2, y2 in segmentos:
        if x1 == x2:
            continue
        pendiente = (y2 - y1) / (x2 - x1)
        angulo = np.rad2deg(np.arctan(pendiente))
        if ANGULO_MIN < angulo < ANGULO_MAX:
            validos.append((x1, y1, x2, y2))
    return validos


def x_en_altura(x1, y1, x2, y2, y):
    return x1 + (y - y1) * (x2 - x1) / (y2 - y1)


def ajustar_linea(segmentos):
    if not segmentos:
        return None
    xs_abajo = []
    xs_arriba = []
    for x1, y1, x2, y2 in segmentos:
        xs_abajo.append(x_en_altura(x1, y1, x2, y2, Y_ABAJO))
        xs_arriba.append(x_en_altura(x1, y1, x2, y2, Y_ARRIBA))
    return np.mean(xs_abajo), np.mean(xs_arriba)


def filtrar_cercanos(segmentos, anterior):
    if anterior is None:
        return segmentos
    x_abajo_ant, x_arriba_ant = anterior
    cercanos = []
    for x1, y1, x2, y2 in segmentos:
        x_abajo = x_en_altura(x1, y1, x2, y2, Y_ABAJO)
        x_arriba = x_en_altura(x1, y1, x2, y2, Y_ARRIBA)
        if abs(x_abajo - x_abajo_ant) < DISTANCIA_MAX and abs(x_arriba - x_arriba_ant) < DISTANCIA_MAX:
            cercanos.append((x1, y1, x2, y2))
    return cercanos


def suavizar(anterior, actual):
    if anterior is None:
        return actual
    x_abajo = SUAVIZADO * anterior[0] + (1 - SUAVIZADO) * actual[0]
    x_arriba = SUAVIZADO * anterior[1] + (1 - SUAVIZADO) * actual[1]
    return x_abajo, x_arriba


def dibujar(frame, segmentos, linea, detectada):
    capa = frame.copy()

    for x1, y1, x2, y2 in segmentos:
        cv2.line(capa, (x1, y1), (x2, y2), (255, 0, 0), 2)

    cambio_carril = False

    if linea is not None:
        x_abajo, x_arriba = linea

        # Límites izquierdo y derecho del ROI
        limite_izq_abajo = 520
        limite_der_abajo = 1180

        limite_izq_arriba = 560
        limite_der_arriba = 800

        # Comprobar proximidad a los límites
        if (
            x_abajo - limite_izq_abajo < MARGEN_CARRIL or
            limite_der_abajo - x_abajo < MARGEN_CARRIL or
            x_arriba - limite_izq_arriba < MARGEN_CARRIL or
            limite_der_arriba - x_arriba < MARGEN_CARRIL
        ):
            cambio_carril = True

        p1 = (int(x_abajo), Y_ABAJO)
        p2 = (int(x_arriba), Y_ARRIBA)

        color = (0, 0, 255) if cambio_carril else (
            (0, 255, 0) if detectada else (0, 200, 255)
        )

        cv2.line(capa, p1, p2, color, 6)

    cv2.polylines(capa, ROI, True, (0, 0, 255), 2)

    texto = "DETECTADA" if detectada else "ESTIMADA"

    cv2.putText(
        capa, texto, (900, 80),
        cv2.FONT_HERSHEY_SIMPLEX, 1.5,
        (255, 255, 255), 3
    )

    # Mostrar alerta de cambio de carril
    if cambio_carril:
        cv2.putText(
            capa,
            "Cambio de Carril",
            (250, 150),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.5,
            (0, 0, 255),
            4
        )

    return cv2.addWeighted(frame, 0.4, capa, 0.6, 0)


cap = cv2.VideoCapture(VIDEO)
anterior = None
perdidos = 0

while True:
    ok, frame = cap.read()
    if not ok:
        break

    bordes = aplicar_roi(preprocesar(frame))
    segmentos = filtrar_cercanos(filtrar_derecha(detectar_segmentos(bordes)), anterior)
    actual = ajustar_linea(segmentos)

    if actual is not None:
        anterior = suavizar(anterior, actual)
        perdidos = 0
    else:
        perdidos += 1
        if perdidos > MAX_PERDIDOS:
            anterior = None

    resultado = dibujar(frame, segmentos, anterior, actual is not None)

    cv2.imshow("Autopilot", cv2.resize(resultado, (960, 540)))
    cv2.imshow("Canny ROI", cv2.resize(bordes, (480, 270)))

    tecla = cv2.waitKey(1) & 0xFF
    if tecla == 27:
        break
    if tecla == ord(" "):
        cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()
