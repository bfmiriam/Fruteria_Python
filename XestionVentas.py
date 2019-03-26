import gi

gi.require_version("Gtk", '3.0')
from gi.repository import Gtk
from XerarPedido import *
from XenerarInformes import *

class XestionVentas(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Xestion de Ventas")

        builder = Gtk.Builder()
        builder.add_from_file("XextionVentas.glade")
        fiestra = builder.get_object("window")

        self.btnPedido = builder.get_object("btnPedido")
        self.btnLista = builder.get_object("btnLista")



        sinais = {
            "on_btnPedido_clicked": self.on_btnPedido_clicked,
            "on_btnLista_clicked": self.on_btnLista_clicked
        }
        builder.connect_signals(sinais)

        fiestra.show_all()

    def on_btnPedido_clicked(self,guardar):
        XerarPedido()

    def on_btnLista_clicked(self,guardar):
        XerarInformes()



if __name__ == "__main__":
    XestionVentas()
    Gtk.main()