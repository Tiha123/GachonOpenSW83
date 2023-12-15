import cv2
import os
from cutpaste.pasteprof import pastef
from cutpaste.cut import cut


cut("asian.jpg","profile.jpg")

pastef("./profile.jpg", "passport.png","./result.png")

