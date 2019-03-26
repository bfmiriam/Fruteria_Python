import gi

gi.require_version("Gtk", '3.0')
from gi.repository import Gtk
from Inventario import *
from ModificarProducto import *


class XestionProductos(Gtk.Window):

    def __init__(self):
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
        Inventario()

    def on_btnEngadir_clicked(self,guardar):
        Inventario()

    def on_btnModificar_clicked(self,guardar):
        ModificarProducto()


if __name__ == "__main__":
    XestionProductos()
    Gtk.main()