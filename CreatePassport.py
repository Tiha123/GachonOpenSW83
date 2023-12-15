import cv2
import os
from cutpaste.pasteprof import pastef
from cutpaste.cutprof import cutf


cutf("asian.jpg","profile.jpg")

pastef("./profile.jpg", "passport.png","./result.png")
