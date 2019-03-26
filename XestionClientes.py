import gi

gi.require_version("Gtk", '3.0')
from gi.repository import Gtk
from ListaClientes import *
from EngadirClientes import *
from ModificarClientes import *


class XestionClientes(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Xestion de Clientes")

        builder = Gtk.Builder()
        builder.add_from_file("XestionClientes.glade")
        fiestra = builder.get_object("window")

        self.btnMostrar = builder.get_object("btnMostrar")
        self.btnEngadir = builder.get_object("btnEngadir")
        self.btnModificar = builder.get_object("btnModificar")
        self.btnSalir = builder.get_object("btnSalir")

        sinais = {
            "on_btnMostrar_clicked": self.on_btnMostrar_clicked,
             "on_btnEngadir_clicked": self.on_btnEngadir_clicked,
            "on_btnModificar_clicked": self.on_btnModificar_clicked
        }
        builder.connect_signals(sinais)

        fiestra.show_all()

    def on_btnMostrar_clicked(self,guardar):
        ListaClientes()

    def on_btnEngadir_clicked(self,guardar):
        EngadirClientes()

    def on_btnModificar_clicked(self,guardar):
        ModificarClientes()


if __name__ == "__main__":
    XestionClientes()
    Gtk.main()