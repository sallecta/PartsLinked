import a

def objUsable(obj):
    import a
    myname="alib.objUsable()"
    a.log(myname,"started")
    if obj != None:
        try: #check if obj allready deleted
            obj.__dict__
        except ReferenceError as e:
            a.log(a.myname(), "No, it is deleted")
            return False
        a.log(a.myname(), "Yes, it is real " + repr(obj))
        return True
    a.log(a.myname(), "No, it is None")
    return False

def checkInitialActiveDoc():
    import a
    myname="alib.checkInitialActiveDoc()"
    a.log(myname,"started")
    if objUsable(a.initialActiveDoc) is False:
        a.initialActiveDoc = getActiveDoc()
        a.log(myname, "initialActiveDoc registered " + repr(a.initialActiveDoc) + repr(a.initialActiveDoc.Name))
    a.log(myname, "end checking a.initialActiveDoc" + repr(a.initialActiveDoc))

def guiMsg(caption, message):
    import a
    myname="alib.guiMsg()"
    a.log(myname,"started")
    from PySide import QtGui
    QtGui.QMessageBox.information(QtGui. qApp.activeWindow(), caption, message)

#creating srcdoc
def selectFileGui():
    from PySide import QtGui
    import a
    myname="alib.selectFileGui()"
    a.log(myname,"started")
    dialog = QtGui.QFileDialog(
            QtGui.qApp.activeWindow(),
            "Select FreeCAD document to import part from"
            )
    dialog.setNameFilter("Supported Formats (*.FCStd);;All files (*.*)")
    if dialog.exec_():
        filename = dialog.selectedFiles()[0]
        import os.path
        if os.path.isfile(filename):
            return filename
    return None

def createSrcDoc(fileName):
    import a
    import FreeCAD
    myname="alib.createSrcDoc()"
    a.log(myname,"started")
    docList = FreeCAD.listDocuments()
    for doc in docList:
        if docList[doc].FileName == fileName:
            a.log(a.myname(), "doc allready open")
            return docList[doc]
    msg = "doc is not open. Opening the doc"
    a.log(a.myname(), msg)
    return FreeCAD.openDocument(fileName)
#end creating srcdoc

#creating srcPart

def createSrcPart(srcDoc):
    import a
    myname="alib.createSrcPart()"
    a.log(myname,"started")
    import FreeCAD
    objList = srcDoc.Objects
    for obj in objList:
        if (obj.TypeId == "Part::Feature") and obj.ViewObject.isVisible():
            return obj
    return None
#end creating srcPart

#creating destdoc
def createDestDoc(srcdoc=None):
    import FreeCAD
    import FreeCADGui
    import a
    myname="alib.createDestDoc()"
    a.log(myname,"started")
    if objUsable(a.destDoc):
        a.log(myname, "DestDoc allready exists")
        return a.destDoc
    docs = FreeCAD.listDocuments()
    a.log(myname, "DestDocList " + repr(len(docs)))
    if len(docs) == 0:
        a.log(myname, "DestDocList == 0, creating new destdoc ")
        a.destDoc = FreeCAD.newDocument()
        return a.destDoc
    if len(docs) == 1:
        if docs.values()[0] == srcdoc:
            a.log(myname, "the only opened doc is srcdoc, creating new destdoc ")
            a.destDoc = FreeCAD.newDocument()
            return a.destDoc
    for doc in docs: #find acceptable active doc to use as destdoc
        a.log(myname, "DestDocList iteration ")
        if docs[doc] != srcdoc:
            a.log(myname, "iter, docs[doc] != srcdoc ")
            if docs[doc] == a.initialActiveDoc:
                a.log(myname, "iter, docs[doc] is a.initialActiveDoc, setting as destdoc "
                + repr(docs[doc].Name) + " " + repr(docs[doc]))
                a.destDoc = a.initialActiveDoc
                return a.destDoc
            else:
                a.log(myname, "iter, docList[doc] is not active")
    if a.destDoc == srcdoc:
        a.log(myname, "function error: a.destDoc == srcdoc ")
        raise ValueError('a.destDoc == srcdoc')
    if a.destDoc == None:
        a.log(myname, "function error: a.destDoc == None")
        raise ValueError(a.myname() + ' error: a.destDoc == None')
#end creating destdoc

#creating destPart
def createDestPart(desDoc,sPart):
    import a
    myname="alib.createDestPart()"
    a.log(myname,"started")
    import FreeCAD
    destPart = desDoc.addObject("Part::FeaturePython")
    a.log(a.myname(), "destPart = " + repr(destPart))
    destPart.Label = sPart.Label
    destPart.addProperty("App::PropertyString", "objType",
        a.label).objType = a.name
    destPart.addProperty("App::PropertyFile", "sourceFile",
        a.label).sourceFile = sPart.Document.FileName
    destPart.addProperty("App::PropertyString", "srcName",
        a.label).srcName = sPart.Name
    destPart.addProperty("App::PropertyString", "srcLabel",
        a.label).srcLabel = sPart.Label
    destPart.Shape = sPart.Shape.copy()
    destPart.ViewObject.ShapeColor = sPart.ViewObject.ShapeColor
    destPart.ViewObject.DiffuseColor = sPart.ViewObject.DiffuseColor
    #destPart.ViewObject.DisplayMode = sPart.ViewObject.DisplayMode #crash in FreeCAD 0.16
    destPart.ViewObject.DrawStyle = sPart.ViewObject.DrawStyle
    #destPart.ViewObject.ShapeMaterial = sPart.ViewObject.ShapeMaterial #disables diffuse colors
    destPart.ViewObject.Lighting = sPart.ViewObject.Lighting
    destPart.ViewObject.LineColor = sPart.ViewObject.LineColor
    destPart.ViewObject.LineMaterial = sPart.ViewObject.LineMaterial
    destPart.ViewObject.LineWidth = sPart.ViewObject.LineWidth
    destPart.ViewObject.Transparency = sPart.ViewObject.Transparency
    destPart.ViewObject.PointColor = sPart.ViewObject.PointColor
    destPart.ViewObject.PointMaterial = sPart.ViewObject.PointMaterial
    destPart.ViewObject.PointSize = sPart.ViewObject.PointSize
    # just set ViewObject.Proxy to something different from None
    #(this assignment is needed to run an internal notification)
    destPart.ViewObject.Proxy=0
    #end creating destPart
    a.destPart = destPart
    return destPart
#end creating destPart

def newDoc():
    import a
    myname="alib.newDoc()"
    a.log(myname,"started")
    import FreeCAD
    return FreeCAD.newDocument()

def getActiveDoc():
    import a
    myname="alib.getActiveDoc()"
    a.log(myname,"started")
    import FreeCAD
    actDoc = FreeCAD.ActiveDocument
    if objUsable(actDoc):
        return FreeCAD.ActiveDocument
    else:
        a.log(myname,"actDoc is None, returning new doc")
        return newDoc()

def guiFitAll(doc = None):
    import a
    import FreeCAD
    import FreeCADGui
    myname="alib.guiFitAll()"
    a.log(myname,"started")
    if doc is None:
        guidoc = FreeCADGui.ActiveDocument
    else:
        guidoc = FreeCADGui.getDocument(doc.Name)
    view = guidoc.ActiveView   # get the active viewer
    view.fitAll()

def closeDocument(doc):
    import a
    myname="alib.closeDocument()"
    a.log(myname,"started")
    import FreeCAD
    FreeCAD.closeDocument(doc.Name)


#move part
def app2gui(doc):
    import FreeCAD
    import FreeCADGui
    import a
    myname="alib.app2gui()"
    a.log(myname,"started")
    return FreeCADGui.getDocument(doc.Name)

def gui2app(doc):
    myname="alib.gui2app()"
    a.log(myname,"started")
    import FreeCAD
    import FreeCADGui
    import a
    return FreeCAD.getDocument(doc.Name)

def getActiveView(doc):
    #import FreeCADGui
    import a
    myname="alib.getActiveView()"
    a.log(myname,"started")
    return app2gui(doc).activeView()

def getFirstSelectionFrom(doc):
    import FreeCADGui
    import a
    myname="alib.getFirstSelectionFrom()"
    a.log(myname,"started")
    obj = None
    a.log(a.myname(), "doc = " + repr(doc))
    sel = FreeCADGui.Selection.getSelection(doc.Name)
    a.log(a.myname(), "sel = " + repr(len(sel)))
    if len(sel) > 0:
        obj = sel[0]
        a.log(a.myname(), "selected item: " + repr(obj))
        return obj
    a.log(a.myname(), "function error: no object selected")
    raise ValueError('getFirstSelection error: obj = None')

def recreateSelection(obj):
    import FreeCADGui
    import a
    myname="alib.recreateSelection()"
    a.log(myname,"started")
    FreeCADGui.Selection.clearSelection(obj.Document.Name)
    FreeCADGui.Selection.addSelection(obj)


class PartMover:
    def __init__(self, obj=None):
        import a
        myname="alib.cl.PartMover.init()"
        a.log(myname,"started")
        if objUsable(obj):
            a.log(myname,"got destination object to move")
            recreateSelection(a.destPart)
        self.obj = getFirstSelectionFrom(a.destDoc)
        self.view = getActiveView(a.destDoc)
        self.initialPostion = self.obj.Placement.Base
        #self.copiedObject = False
        self.callbackMove = self.view.addEventCallback("SoLocation2Event",self.moveMouse)
        self.callbackClick = self.view.addEventCallback("SoMouseButtonEvent",self.clickMouse)
        self.callbackKey = self.view.addEventCallback("SoKeyboardEvent",self.KeyboardEvent)
    def moveMouse(self, info):
        import a
        myname="alib.cl.PartMover.moveMouse()"
        a.log(myname,"started")
        newPos = self.view.getPoint( *info['Position'] )
        a.log(myname,"new position " + repr(newPos))
        self.obj.Placement.Base = newPos
    def removeCallbacks(self):
        import a
        myname="alib.cl.PartMover.removeCallbacks()"
        a.log(myname,"started")
        self.view.removeEventCallback("SoLocation2Event",self.callbackMove)
        self.view.removeEventCallback("SoMouseButtonEvent",self.callbackClick)
        self.view.removeEventCallback("SoKeyboardEvent",self.callbackKey)
    def clickMouse(self, info):
        import a
        myname="alib.cl.PartMover.clickMouse()"
        a.log(myname,"started")
        a.log(myname,"clickMouse info " + repr(info))
        if info['Button'] == 'BUTTON1' and info['State'] == 'DOWN':
            if not info['ShiftDown'] and not info['CtrlDown']:
                self.removeCallbacks()
            elif info['ShiftDown']: #copy object
                self.obj = duplicateImportedPart( self.obj )
                self.copiedObject = True
            elif info['CtrlDown']:
                azi   =  ( numpy.random.rand() - 0.5 )*numpy.pi*2
                ela   =  ( numpy.random.rand() - 0.5 )*numpy.pi
                theta =  ( numpy.random.rand() - 0.5 )*numpy.pi
                axis = azimuth_and_elevation_angles_to_axis( azi, ela )
                self.obj.Placement.Rotation.Q = quaternion( theta, *axis )

    def KeyboardEvent(self, info):
        import a
        myname="alib.cl.PartMover.KeyboardEvent()"
        a.log(myname,"started")
        a.log(myname,"KeyboardEvent info " + repr(info))
        if info['State'] == 'UP' and info['Key'] == 'ESCAPE':
            if not self.copiedObject:
                self.obj.Placement.Base = self.initialPostion
            else:
                FreeCAD.ActiveDocument.removeObject(self.obj.Name)
            self.removeCallbacks()
#end move part

#start constrain part
def getParts():
    import a
    myname="alib.getParts()"
    a.log(myname,"started")
    import FreeCAD
    partsList = []
    objList = getActiveDoc().Objects
    a.log(myname,"objList " + repr(type(objList)) + " " + repr(objList))
    for obj in objList:
        if hasattr(obj,'objType'):
            a.log(myname,"detected object with objType attribute")
            if obj.objType == a.name:
                a.log(myname,"detected " + a.name + " object")
                partsList.append(obj)
    if len(partsList) == 0:
        a.log(myname,"no objects with objType attribute detected")
        return None
    else:
        return partsList

def getSelectionExtended():
    import a
    myname="alib.getSelectionExtended()"
    a.log(myname,"started")
    selEx = None
    import FreeCADGui
    selEx = FreeCADGui.Selection.getSelectionEx(getActiveDoc().Name)
    if (type(selEx) == None) or ((type(selEx) != list)):
        a.log(myname,"no selEx " + repr(selEx) + " " + repr(type(selEx)))
        return None
    if len(selEx) == 0:
        a.log(myname,"len(selEx) == 0, returning None " + repr(selEx))
        return None
    return selEx

    subface=selEx[0].SubObjects[1]
#end constrain part