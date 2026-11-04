import cv2
import numpy as np

VIDEO = "autopilot/autopilot.mp4"
ROI = np.array([[(520, 540), (1180, 540), (800, 285), (560, 285)]], dtype=np.int32)
Y_ABAJO = 540
Y_ARRIBA = 300
ANGULO_MIN = 20
ANGULO_MAX = 75


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


def ajustar_linea(segmentos):
    if not segmentos:
        return None
    xs = []
    ys = []
    for x1, y1, x2, y2 in segmentos:
        xs += [x1, x2]
        ys += [y1, y2]
    m, b = np.polyfit(ys, xs, 1)
    return m, b


def dibujar(frame, segmentos, linea):
    capa = frame.copy()
    for x1, y1, x2, y2 in segmentos:
        cv2.line(capa, (x1, y1), (x2, y2), (255, 0, 0), 2)
    if linea is not None:
        m, b = linea
        p1 = (int(m * Y_ABAJO + b), Y_ABAJO)
        p2 = (int(m * Y_ARRIBA + b), Y_ARRIBA)
        cv2.line(capa, p1, p2, (0, 255, 0), 12)
    cv2.polylines(capa, ROI, True, (0, 0, 255), 2)
    return cv2.addWeighted(frame, 0.4, capa, 0.6, 0)


cap = cv2.VideoCapture(VIDEO)

while True:
    ok, frame = cap.read()
    if not ok:
        break

    bordes = aplicar_roi(preprocesar(frame))
    segmentos = filtrar_derecha(detectar_segmentos(bordes))
    linea = ajustar_linea(segmentos)
    resultado = dibujar(frame, segmentos, linea)

    cv2.imshow("Autopilot", cv2.resize(resultado, (960, 540)))
    cv2.imshow("Canny ROI", cv2.resize(bordes, (480, 270)))

    tecla = cv2.waitKey(1) & 0xFF
    if tecla == 27:
        break
    if tecla == ord(" "):
        cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()
