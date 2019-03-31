import gi
from sqlite3 import dbapi2

gi.require_version("Gtk", '3.0')
from gi.repository import Gtk


class XerarPedido(Gtk.Window):

    """Ventana XerarPedido para  realizar novos pedidos e gardalos na base de datos

        Metodos:

        __init__ --Constructor
         on_btnFacerPedido_clicked -- recolle a informacion do formulario e realiza o pedido
         on_btnNovo_clicked -- vacia o formulario para realizar novos pedidos
        """

    def __init__(self):

        """Constructor  da clase XerarPedido (Window)
            Dispomos de dous ComboBox  para seleccionar a empresa e o producto, indicando a cantidade e a fecha para realizar o pedido

           :param None

           Excepcions:
           -Non ten

           """
        Gtk.Window.__init__(self, title="Xerar Pedido")

        bbdd = dbapi2.connect("bbdd.dat")
        self.cursor = bbdd.cursor()
        #self.cursor.execute("create table Pedidos(NombreEmpresa text,producto text, cantidad float,precioVenta float, fechaEntrega text, total float)")
        #self.cursor.execute("drop table Pedidos")
        #self.cursor.execute("commit")

        self.empresas = []
        cursorEmpresas = self.cursor.execute("select NombreEmpresa from Clientes")

        for row in cursorEmpresas:
            self.empresas.append(row[0])

        self.productos = []
        cursorProductos = self.cursor.execute("select producto from Productos")

        for row in cursorProductos:
            self.productos.append(row[0])


        builder = Gtk.Builder()
        builder.add_from_file("NovoPedido.glade")
        fiestra = builder.get_object("window")

        self.cmbEmpresas = builder.get_object("cmbEmpresas")
        self.cmbProductos = builder.get_object("cmbProductos")
        self.txtCantidade = builder.get_object("txtCantidade")
        self.txtFecha = builder.get_object("txtFecha")
        self.btnFacerPedido = builder.get_object("btnFacerPedido")
        self.txtTotal = builder.get_object("txtTotal")

        for empresa in self.empresas:
            self.cmbEmpresas.append_text(empresa)

        for producto in self.productos:
            self.cmbProductos.append_text(producto)


        sinais = {
            "on_btnFacerPedido_clicked": self.on_btnFacerPedido_clicked,
            "on_btnNovo_clicked": self.on_btnNovo_clicked
        }
        builder.connect_signals(sinais)

        fiestra.show_all()

    def on_btnFacerPedido_clicked(self,guardar):
        """Rexistra na base de datos o pedido recollendo a informacion do formulario

             :param guardar: guardar
             :return: None
             :raises: dbapi2.DatabaseError

             """

        empresa = self.cmbEmpresas.get_active_text()
        producto =self.cmbProductos.get_active_text()
        cantidade =float(self.txtCantidade.get_text())
        fecha = self.txtFecha.get_text()

        cursorPrecio = self.cursor.execute("select precioVenta from Productos where producto=?",(producto,))

        for row in cursorPrecio:
            precioVenta= row[0]

        total = cantidade * float(precioVenta)
        self.txtTotal.set_text(str(total))

        self.cursor.execute("insert into Pedidos (NombreEmpresa,producto, cantidad,precioVenta, fechaEntrega, total) values(?,?,?,?,?,?)",(empresa,producto,cantidade,precioVenta,fecha,total))

        try:
            self.cursor.execute("commit")

        except (dbapi2.DatabaseError):
            print("Guardado en la base de datos")

    def on_btnNovo_clicked(self, guardar):
        """Vacia o contido do formulario para poder realizar un novo pedido

             :param guardar: guardar
             :return: None

             """


        self.txtCantidade.set_text('')
        self.txtFecha.set_text('')
        self.txtTotal.set_text('')
        self.cmbEmpresas.set_active(-1)
        self.cmbProductos.set_active(-1)

if __name__ == "__main__":
    XerarPedido()
    Gtk.main()