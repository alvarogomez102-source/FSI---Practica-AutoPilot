import cv2
import numpy as np

VIDEO = "imgs/PracticaAutoPilot.mp4"
ROI = np.array([[(520, 540), (1180, 540), (800, 285), (560, 285)]], dtype=np.int32)
VENTANA = "Canny ROI"


def nada(valor):
    pass


def preprocesar(frame, bajo, alto):
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    suave = cv2.GaussianBlur(gris, (5, 5), 0)
    return cv2.Canny(suave, bajo, alto)


def aplicar_roi(bordes):
    mascara = np.zeros_like(bordes)
    cv2.fillPoly(mascara, ROI, 255)
    return cv2.bitwise_and(bordes, mascara)


cap = cv2.VideoCapture(VIDEO)
cv2.namedWindow(VENTANA)
cv2.createTrackbar("Umbral bajo", VENTANA, 50, 255, nada)
cv2.createTrackbar("Umbral alto", VENTANA, 150, 255, nada)

while True:
    ok, frame = cap.read()
    if not ok:
        break

    bajo = cv2.getTrackbarPos("Umbral bajo", VENTANA)
    alto = cv2.getTrackbarPos("Umbral alto", VENTANA)
    bordes = aplicar_roi(preprocesar(frame, bajo, alto))

    vista = frame.copy()
    cv2.polylines(vista, ROI, True, (0, 0, 255), 2)

    cv2.imshow("Original", cv2.resize(vista, (640, 360)))
    cv2.imshow(VENTANA, cv2.resize(bordes, (640, 360)))

    tecla = cv2.waitKey(1) & 0xFF
    if tecla == 27:
        break
    if tecla == ord(" "):
        cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()
