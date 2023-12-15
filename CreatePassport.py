import cv2
import sys
import cutpaste


n = cutpaste.cut(sys.argv[1])

m = cutpaste.paste(n)

cv2.imwrite('PassportResult.jpg', m)
cv2.imshow('img', m)
cv2.waitKey()
