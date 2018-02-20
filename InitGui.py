import a
import FreeCAD
import FreeCADGui


class PartsLinkedWorkbench (Workbench):

    import a
    myname="InitGui.PartsLinkedWorkbench"
    a.log(myname,"started")
    a.log("InitGui->PartsLinked", "name = " + a.name + ", label = " + a.label)
    a.log("InitGui->PartsLinked", "path = " + a.path)
    a.log("InitGui->PartsLinked", "os sep= " + a.sep)
    MenuText = a.name

    def Initialize(self):
        import a
        myname="InitGui.PartsLinkedWorkbench.Initialize()"
        a.log(myname,"started")
        import cmd_PL_add
        import cmd_PL_move
        import cmd_PL_constrain
        commandslist = [
                'PL_add',
                'PL_move',
                'PL_constrain'
                ]
        self.appendToolbar(a.label, commandslist)

    def Activated(self):
        import a
        myname="InitGui.PartsLinkedWorkbench.Activated()"
        a.log(myname,"started")

    def ContextMenu(self, recipient):
        import a
        myname="InitGui.PartsLinkedWorkbench.ContextMenu()"
        a.log(myname,"started")

    Icon = a.iconsPath + a.sep + 'wb_PL.svg'

Gui.addWorkbench(PartsLinkedWorkbench())