import gi

gi.require_version("Gtk", '3.0')
from gi.repository import Gtk
from XestionClientes import *
from XestionProductos import *
from XestionVentas import *



class FiestraPrincipal(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Xestion Fruteria")

        builder = Gtk.Builder()
        builder.add_from_file("VentanaPrincipal.glade")
        fiestra = builder.get_object("window")

        self.btnVentas = builder.get_object("btnVentas")
        self.btnClientes = builder.get_object("btnClientes")
        self.btnProductos = builder.get_object("btnProductos")
        self.btnPechar = builder.get_object("btnPechar")

        sinais = {
            "on_btnClientes_clicked": self.on_btnClientes_clicked,
            "on_btnProductos_clicked": self.on_btnProductos_clicked,
            "on_btnVentas_clicked": self.on_btnVentas_clicked,
            "on_btnPechar_clicked": self.on_btnPechar_clicked,
            "on_window_destroy": Gtk.main_quit
        }
        builder.connect_signals(sinais)

        fiestra.connect("destroy", Gtk.main_quit)
        fiestra.show_all()


    def on_btnClientes_clicked(self,guardar):
        XestionClientes()

    def on_btnProductos_clicked(self,guardar):
        XestionProductos()

    def on_btnVentas_clicked(self, guardar):
        XestionVentas()

    def on_btnPechar_clicked(self,guardar):
        Gtk.main_quit()


if __name__ == "__main__":
    FiestraPrincipal()
    Gtk.main()