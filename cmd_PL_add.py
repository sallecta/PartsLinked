import a


class cl_cmd_PL_add:
    def Activated(self):
        import alib
        import a
        myname="cl_cmd_PL_add.Activated()"
        a.log(myname,"started")

        alib.checkInitialActiveDoc()

        #creating srcdoc
        a.log(myname, "creating srcdoc")
        srcFile = alib.selectFileGui()
        if srcFile is None:
            a.log(myname, "srcFile is None. Function return")
            return
        srcDoc = alib.createSrcDoc(srcFile)
        a.log(myname, "end creating srcdoc" + repr(srcDoc))
        #end creating srcdoc

        #creating srcPart
        a.log(myname, "creating srcPart")
        srcPart = alib.createSrcPart(srcDoc)
        if alib.objUsable(srcPart) is False:
            alib.guiMsg("Invalid Part", "No valid Parts in selected Document")
            a.log(myname, "srcPart is not usable, return")
            alib.closeDocument(srcDoc)
            return
        a.log(myname, "end creating srcPart " + repr(srcPart))
        #return
        #end creating srcPart

        #creating destdoc
        a.log(myname, "creating destdoc")
        destDoc = alib.createDestDoc(srcDoc)
        a.log(myname, "end creating destdoc " + repr(destDoc))
        #end creating destdoc

        a.log(myname, "destDoc = " + repr(destDoc))
        a.log(myname, "srcDoc = " + repr(srcDoc))

        #creating destPart
        a.log(myname, "creating destPart")
        destPart = alib.createDestPart(destDoc,srcPart)
        a.log(myname, "end creating destPart")
        #end creating destPart

        a.log(myname, "recomputing destDoc")
        destDoc.recompute()
        a.log(myname, "fitting view")
        alib.guiFitAll(destDoc)

        #moving part
        a.log(myname, "moving part")
        alib.PartMover(destPart)
        a.log(myname, "end moving part")
        #end moving part

        a.log(myname, "closing srcDoc")
        alib.closeDocument(srcDoc)

    def GuiViewFit(self):
        import a
        myname="cl_cmd_PL_add.GuiViewFit()"
        a.log(myname,"started")

    def GetResources(self):
        import a
        myname="cl_cmd_PL_add.GetResources()"
        a.log(myname,"started")
        return {
            'Pixmap': a.iconsPath + a.sep + 'cmd_PL_add.svg',
            'MenuText': 'Import a part from another FreeCAD document',
            'ToolTip': 'Import a part from another FreeCAD document'
            }
import FreeCADGui
FreeCADGui.addCommand('PL_add', cl_cmd_PL_add())