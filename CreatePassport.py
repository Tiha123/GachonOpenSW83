import cv2
import sys
import cutpaste.cutprof
import cutpaste.pasteprof


n = cutpaste.cutprof.cutf(sys.argv[1])

m = cutpaste.pasteprof.pastef(n)

cv2.imwrite('./PassportResult.jpg', m)
cv2.imshow('img', m)
cv2.waitKey()
