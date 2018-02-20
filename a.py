label = "Parts Linked"
name = label.replace(" ", "")

import os
import sys
path = os.path.dirname(os.path.realpath(__file__))
sep = os.sep

resourcesPath = path + sep + "Recources"
iconsPath = resourcesPath + sep + "Icons"

destDoc = None
destPart = None
initialActiveDoc = None

def myname():
    import inspect
    return inspect.stack()[1][3]

def log(strLocation, strMsg=""):
    print(name + "->" + strLocation + ": " + strMsg)


