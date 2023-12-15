import cv2


def pastef(n):
    img = cv2.imread('./passport.png')

    height, width, channel = img.shape
    height2 = int(height*0.4)
    width2 = int(width*0.3)

    m = cv2.resize(n, dsize=(width2, height2), interpolation=cv2.INTER_AREA)

    x_end, y_end, c = m.shape
    img[0:x_end, 0:y_end] = m

    return img
