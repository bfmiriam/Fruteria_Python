import gi
from sqlite3 import dbapi2

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class ModificarProducto(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Modificar Producto")

        bbdd = dbapi2.connect("bbdd.dat")
        self.cursor = bbdd.cursor()

        self.productos = []
        cursorProductos = self.cursor.execute("select producto from Productos")

        for row in cursorProductos:
            self.productos.append(row[0])

        builder = Gtk.Builder()
        builder.add_from_file("ModificarProducto.glade")
        fiestra = builder.get_object("window")

        self.cmbProductos = builder.get_object("cmbProductos")
        self.btnBuscar = builder.get_object("btnBuscar")
        self.txtProducto = builder.get_object("txtProducto")
        self.txtCantidade = builder.get_object("txtCantidade")
        self.txtPrecioCompra = builder.get_object("txtPrecioCompra")
        self.txtPrecioVenta = builder.get_object("txtPrecioVenta")
        self.txtProvedor = builder.get_object("txtProvedor")
        self.txtContacto = builder.get_object("txtContacto")
        self.btnModificar = builder.get_object("btnModificar")
        self.btnEliminar = builder.get_object("btnEliminar")


        for producto in self.productos:
            self.cmbProductos.append_text(producto)

        sinais = {
            "on_btnBuscar_clicked": self.on_btnBuscar_clicked,
            "on_btnEliminar_clicked": self.on_btnEliminar_clicked,
            "on_btnModificar_clicked": self.on_btnModificar_clicked,
        }
        builder.connect_signals(sinais)

        fiestra.show_all()

    def on_btnBuscar_clicked(self,cmbEmpresas):

        nombre =self.cmbProductos.get_active_text()

        cursorProducto = self.cursor.execute("select producto, cantidade, precioCompra, precioVenta , provedor ,contacto from Productos where producto=?",(nombre,))

        for row in cursorProducto:
            self.txtProducto.set_text(row[0])
            self.txtCantidade.set_text(str(row[1]))
            self.txtPrecioCompra.set_text(str(row[2]))
            self.txtPrecioVenta.set_text(str(row[3]))
            self.txtProvedor.set_text(row[4])
            self.txtContacto.set_text(row[5])

    def on_btnEliminar_clicked(self, cmbProductos):

        nombre = self.cmbProductos.get_active_text()

        self.cursor.execute( "delete from Productos where producto=?",(nombre,))
        try:
            self.cursor.execute("commit")
            print('borrado')

        except (dbapi2.DatabaseError):
            print("Eliminado de la base de datos")

        self.txtProducto.set_text('')
        self.txtCantidade.set_text('')
        self.txtPrecioCompra.set_text('')
        self.txtPrecioVenta.set_text('')
        self.txtProvedor.set_text('')
        self.txtContacto.set_text('')
        self.cmbProductos.set_active(-1)

    def on_btnModificar_clicked(self, cmbProductos):

        nombre = self.cmbProductos.get_active_text()

        nombreProducto= self.txtProducto.get_text()
        cantidade = float(self.txtCantidade.get_text())
        precioCompra = float(self.txtPrecioCompra.get_text())
        precioVenta = float(self.txtPrecioVenta.get_text())
        provedor = self.txtProvedor.get_text()
        contacto = self.txtContacto.get_text()

        self.cursor.execute("update Productos set producto=?, cantidade=?, precioCompra=?, precioVenta=?, provedor=?, contacto=? where producto=?",
                            (nombreProducto,cantidade,precioCompra,precioVenta,provedor,contacto,nombre))
        try:
            self.cursor.execute("commit")
            print('modificado')

        except (dbapi2.DatabaseError):
            print("Modificado")

        self.txtProducto.set_text('')
        self.txtCantidade.set_text('')
        self.txtPrecioCompra.set_text('')
        self.txtPrecioVenta.set_text('')
        self.txtProvedor.set_text('')
        self.txtContacto.set_text('')
        self.cmbProductos.set_active(-1)


if __name__ == "__main__":
    ModificarProducto()
    Gtk.main()