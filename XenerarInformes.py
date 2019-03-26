import gi
from sqlite3 import dbapi2

gi.require_version("Gtk", '3.0')
from gi.repository import Gtk
from XerarFactura import *
from InformePedidos import *


class XerarInformes(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Xerar Informes")

        bbdd = dbapi2.connect("bbdd.dat")
        self.cursor = bbdd.cursor()


        self.empresas = []
        cursorEmpresas = self.cursor.execute("select NombreEmpresa from Clientes")

        for row in cursorEmpresas:
            self.empresas.append(row[0])


        builder = Gtk.Builder()
        builder.add_from_file("GenerarInformes.glade")
        fiestra = builder.get_object("window")

        self.cmbClientes = builder.get_object("cmbClientes")
        self.btnClientes = builder.get_object("btnCliente")
        self.btnPedidos = builder.get_object("btnPedidos")

        for empresa in self.empresas:
            self.cmbClientes.append_text(empresa)

        sinais = {
            "on_btnClientes_clicked": self.on_btnClientes_clicked,
            "on_btnPedidos_clicked": self.on_btnPedidos_clicked
        }
        builder.connect_signals(sinais)

        fiestra.show_all()

    def on_btnClientes_clicked(self,guardar):

        cliente = self.cmbClientes.get_active_text()
        XerarFactura(cliente)
        self.cmbClientes.set_active(-1)

    def on_btnPedidos_clicked(self, guardar):
        InformePedidos()


if __name__ == "__main__":
    XerarInformes()
    Gtk.main()