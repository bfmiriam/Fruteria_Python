import gi

gi.require_version("Gtk", '3.0')
from gi.repository import Gtk
from ListaClientes import *
from EngadirClientes import *
from ModificarClientes import *


class XestionClientes(Gtk.Window):

    """Ventana XestionClientes para  crear,modificar ou mostrar clientes

        Metodos:

        __init__ --Constructor
        on_btnMostrar_clicked -- cambia de interfaz e mostra nun treeView os clientes
        on_btnEngadir_clicked -- cambia de interfaz e permite engadir un cliente
        on_btnModificar_clicked -- cambia de interfaz e permite modificar ou borrar un cliente


        """

    def __init__(self):

        """Constructor  da clase XestionClientes (Window)
            Dispomos de tres botons que nos redirixen a distintas interfaces para poder traballar coa taboa de clientes

            :param None

             Excepcions:
             -Non ten

             """
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
        """Abre unha nova ventana que mostra un TreeView con todos os clientes da base de datos

          :param guardar: guardar
          :return: None

           """
        ListaClientes()

    def on_btnEngadir_clicked(self,guardar):
        """Abre unha nova ventana con un formulario que nos permite gardar novos clientes na base de datos

          :param guardar: guardar
          :return: None

           """
        EngadirClientes()

    def on_btnModificar_clicked(self,guardar):
        """Abre unha nova ventana con un comboBox para escoller un cliente da base de datos que queiramos borrar ou modificar

          :param guardar: guardar
          :return: None

           """
        ModificarClientes()


if __name__ == "__main__":
    XestionClientes()
    Gtk.main()