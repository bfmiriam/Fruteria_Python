import gi

gi.require_version("Gtk", '3.0')
from gi.repository import Gtk
from XestionClientes import *
from XestionProductos import *
from XestionVentas import *



class FiestraPrincipal(Gtk.Window):

    """Ventana FiestraPrincipal que divide o programa de xestion en tres apartados, dependendo de se queremos tratar con ventas, clientes ou productos

        Metodos:

        __init__ --Constructor
        on_btnClientes_clicked -- cambia de interfaz e permitenos traballar coa taboa de clientes
        on_btnProductos_clicked -- cambia de interfaz e permitenos traballar coa taboa de productos
        on_btnVentas_clicked -- cambia de interfaz e permitenos traballar coa taboa de pedidos
        on_btnPechar_clicked -- pecha o programa

        """

    def __init__(self):
        """Constructor  da clase FiestraPrincipal (Window)
            Dispomos de tres botons que nos redirixen a distintas interfaces para poder traballar coas distintas taboas e outro que permite pechar o programa

            :param None

             Excepcions:
             -Non ten

             """
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
        """Abre unha nova ventana que nos permite crear, mostrar,modificar ou eliminar clientes

          :param guardar: guardar
          :return: None

           """
        XestionClientes()

    def on_btnProductos_clicked(self,guardar):
        """Abre unha nova ventana que nos permite crear, mostrar,modificar ou eliminar productos

          :param guardar: guardar
          :return: None

           """
        XestionProductos()

    def on_btnVentas_clicked(self, guardar):
        """Abre unha nova ventana que nos permite facer pedidos e xerar informes

          :param guardar: guardar
          :return: None

           """
        XestionVentas()

    def on_btnPechar_clicked(self,guardar):
        """Pecha o programa

          :param guardar: guardar
          :return: None

           """
        Gtk.main_quit()


if __name__ == "__main__":
    FiestraPrincipal()
    Gtk.main()