import a
import alib

class cl_cmd_PL_constrain:

    def Activated(self):
        import alib
        import a
        myname="cl_cmd_PL_constrain.Activated()"
        a.log(myname,"started")
        parts = alib.getParts()
        if parts is None:
            a.log(myname,"doc contains no valid parts, return")
            alib.guiMsg("No valid parts", "Document contains no valid parts")
            return
        a.log(myname,"doc contains valid parts " + repr(parts))

        selEx = alib.getSelectionExtended()
        if selEx is None:
            a.log(myname,"selEx is None, return")
            return
        a.log(myname,"doc contains extended selection " + repr(selEx))


    def GetResources(self):
        import a
        myname="cl_cmd_PL_constrain.GetResources()"
        a.log(myname,"started")
        return {
        'Pixmap': a.iconsPath + a.sep + 'cmd_PL_constrain.svg',
        'MenuText': 'cmd_PL_constrain',
        'ToolTip': 'cmd_PL_constrain'
        }

import FreeCADGui
FreeCADGui.addCommand('PL_constrain', cl_cmd_PL_constrain())