import a
import alib

class cl_cmd_PL_move:

    def Activated(self):

        import a
        myname="cl_cmd_PL_move.Activated()"
        a.log(myname,"started")
        import alib
        if alib.objUsable(a.destDoc) is False:
        #if a.destDoc is None: #deleted object is not None
            a.log(myname, "a.destDoc is not usable, regging active doc as a.destdoc")
            a.destDoc = alib.getActiveDoc()
        alib.PartMover()

    def GetResources(self):
        import alib
        a.log("cl_cmd_PL_move.GetResources()", "started")
        return {
            'Pixmap': a.iconsPath + a.sep + 'cmd_PL_move.svg',
            'MenuText': 'Move part',
            'ToolTip': 'Move selected part'
            }
import FreeCADGui
FreeCADGui.addCommand('PL_move', cl_cmd_PL_move())