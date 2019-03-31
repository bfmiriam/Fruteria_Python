import gi

gi.require_version("Gtk", '3.0')
from gi.repository import Gtk
from Inventario import *
from ModificarProducto import *


class XestionProductos(Gtk.Window):
    """Ventana XestionProductos para  crear,modificar ou mostrar productos

        Metodos:

        __init__ --Constructor
        on_btnInventario_clicked -- cambia de interfaz e mostra nun treeView os productos,  tamen permite engadir
        on_btnEngadir_clicked -- cambia de interfaz e mostra nun treeView os productos, tamen permite engadir
        on_btnModificar_clicked -- cambia de interfaz e permite modificar ou borrar un producto

        """

    def __init__(self):

        """Constructor  da clase XestionProductos (Window)
            Dispomos de tres botons que nos redirixen a distintas interfaces para poder traballar coa taboa de productos

            :param None

             Excepcions:
             -Non ten

             """
        Gtk.Window.__init__(self, title="Xestion de Productos")

        builder = Gtk.Builder()
        builder.add_from_file("XestionProductos.glade")
        fiestra = builder.get_object("window")

        self.btnInventario = builder.get_object("btnInventario")
        self.btnEngadir = builder.get_object("btnEngadir")
        self.btnModificar = builder.get_object("btnModificar")


        sinais = {
            "on_btnInventario_clicked": self.on_btnInventario_clicked,
            "on_btnEngadir_clicked": self.on_btnEngadir_clicked,
            "on_btnModificar_clicked": self.on_btnModificar_clicked
        }
        builder.connect_signals(sinais)

        fiestra.show_all()

    def on_btnInventario_clicked(self,guardar):

        """Abre unha nova ventana que mostra un TreeView con todos os productos da base de datos e permite engadir outros novos

          :param guardar: guardar
          :return: None

           """
        Inventario()

    def on_btnEngadir_clicked(self,guardar):
        """Abre unha nova ventana que mostra un TreeView con todos os productos da base de datos e permite engadir outros novos

          :param guardar: guardar
          :return: None

           """
        Inventario()

    def on_btnModificar_clicked(self,guardar):
        """Abre unha nova ventana con un comboBox para escoller un producto da base de datos que queiramos borrar ou modificar

          :param guardar: guardar
          :return: None

           """
        ModificarProducto()


if __name__ == "__main__":
    XestionProductos()
    Gtk.main()