
#subface.Placement.Base = FreeCAD.Vector(-65, 15, 658)

#planeBase.BoundBox
#BoundBox (-125, -125, 0, 125, -125, 4)

doc = App.ActiveDocument
selEx = FreeCADGui.Selection.getSelectionEx(doc.Name)
base = selEx[0].Object
baseBoundBox = base.Shape.BoundBox
baseFace = selEx[0].SubObjects[0]
baseFaceBoundBox = baseFace.BoundBox
baseFaceBoundBox.XMin
baseFaceBoundBox.YMin
baseFaceBoundBox.ZMin
baseFaceBoundBox.XMax
baseFaceBoundBox.YMax
baseFaceBoundBox.ZMax

client = selEx[1].Object
clientBoundBox = client.Shape.BoundBox
clientFace = selEx[1].SubObjects[0]
clientFaceBoundBox = clientFace.BoundBox






>>> client.Placement.Base
Vector (4.0, -200.0, 100.0)
>>> clientFace.Placement.Base
Vector (4.0, -200.0, 100.0)
>>> clientBoundBox
BoundBox (-121, -325, 100, 129, -75, 160)
>>> clientFaceBoundBox
BoundBox (129, -325, 100, 129, -75, 104)
BoundBox (129, -325, 100, 129, -75, 104)


>>> base.Placement.Base
Vector (0.0, 0.0, 0.0)
>>> baseBoundBox
BoundBox (-125, -125, 0, 125, 125, 60)
>>> baseFaceBoundBox
BoundBox (-125, -125, 0, 125, -125, 4)
>>>

client.Placement.Base = FreeCAD.Vector(-125, -125, 0)
