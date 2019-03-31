import gi

gi.require_version("Gtk", '3.0')
from gi.repository import Gtk
from XerarPedido import *
from XenerarInformes import *

class XestionVentas(Gtk.Window):

    """Ventana XestionVentas para facer un novo pedido ou para xenerar informes

        Metodos:

        __init__ --Constructor
        on_btnPedido_clicked -- cambia de interfaz para facer novos pedidos
        on_btnLista_clicked -- cambia de interfaz para xerar informes


        """

    def __init__(self):
        """Constructor  da clase XestionVentas (Window)
            Dispomos de dous botons que nos redirixen a distintas interfaces para poder traballar coa taboa de Pedidos

            :param None

             Excepcions:
             -Non ten

             """
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
        """Abre unha nova ventana que mostra un comboBox para escoller cliente e producto e xerar pedidos

          :param guardar: guardar
          :return: None

           """
        XerarPedido()

    def on_btnLista_clicked(self,guardar):
        """Abre unha nova ventana que que nos permite xerar diferentes informes

          :param guardar: guardar
          :return: None

           """
        XerarInformes()



if __name__ == "__main__":
    XestionVentas()
    Gtk.main()