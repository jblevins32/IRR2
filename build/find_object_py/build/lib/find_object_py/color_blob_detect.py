import numpy as np
import cv2


def hsv_contour_detect(
    frame, hueLow, hueHigh, satLow, satHigh, valLow, valHigh, hueLow2, hueHigh2
):

    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerBound = np.array([hueLow, satLow, valLow])
    upperBound = np.array([hueHigh, satHigh, valHigh])

    lowerBound2 = np.array([hueLow2, satLow, valLow])
    upperBound2 = np.array([hueHigh2, satHigh, valHigh])

    myMask = cv2.inRange(frameHSV, lowerBound, upperBound)
    myMask2 = cv2.inRange(frameHSV, lowerBound2, upperBound2)

    myMask = myMask | myMask2
    contours, junk = cv2.findContours(
        myMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    for contour in contours:
        area = cv2.contourArea(contour)
        if area >= 100:
            x, y, w, h = cv2.boundingRect(contour)
            print(f"Bounding Box {x},{y} geometry: {w},{h}; target:{target}")
            target=x+w/2
            return target
        else:
            print(f"Area:{area}")
            return 1000.0
            # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
            # text = "x: " + str(x) + ", y: " + str(y)
            # cv2.putText(
            #     frame,
            #     text,
            #     (x,y),
            #     cv2.FONT_HERSHEY_SIMPLEX,
            #     0.5,
            #     (0, 255, 0),
            #     2,
            # )
        # else:
        #     x, y, w, h = cv2.boundingRect(np.vstack(contours))
        #     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
        #     text = "x: " + str(x) + ", y: " + str(y)
        #     cv2.putText(
        #         frame,
        #         text,
        #         (x,y),
        #         cv2.FONT_HERSHEY_SIMPLEX,
        #         0.5,
        #         (0, 255, 0),
        #         2,
        #     )
