import gi
from sqlite3 import dbapi2

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class ListaClientes(Gtk.Window):


    def __init__(self):
        Gtk.Window.__init__(self, title="Lista de Clientes")

        bbdd = dbapi2.connect("bbdd.dat")
        self.cursor = bbdd.cursor()
        #self.cursor.execute("create table Productos(producto text,tipo text, cantidade numeric, precioCompra numeric, precioVenta numeric, provedor text)")
        #self.cursor.execute("insert into Productos values('naranja','clementina',3,1,2,'Pepe')")
        #self.cursor.execute("insert into Productos values('manzana','golden',2,3,4,'Sara')")
        #self.cursor.execute("insert into Productos values('platano','canarias',5,1.5,3.2,'Gabriel')")
        #self.cursor.execute("delete * from Productos where producto='producto'")
        #self.cursor.execute("commit")

        boxV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(boxV)

        modelo = Gtk.ListStore(str, str, str,str,str,str,str)
        cursorCliente = self.cursor.execute("select NombreEmpresa,CIF,telefono,email,direccion,codPostal,provincia from Clientes")
        for row in cursorCliente:
            modelo.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6]])


        vista = Gtk.TreeView(model=modelo)
        boxV.pack_start(vista,True,True,0)

        celdaText = Gtk.CellRendererText()
        columnaEmpresa = Gtk.TreeViewColumn('Empresa', celdaText, text=0)
        columnaEmpresa.set_min_width(160)
        columnaEmpresa.set_sort_column_id(0)
        vista.append_column(columnaEmpresa)

        celdaText2 = Gtk.CellRendererText()
        columnaCif = Gtk.TreeViewColumn('CIF', celdaText2, text=1)
        columnaCif.set_min_width(160)
        columnaCif.set_sort_column_id(0)
        vista.append_column(columnaCif)

        celdaNum = Gtk.CellRendererText()
        columnaTelefono = Gtk.TreeViewColumn('Telefono', celdaNum, text=2)
        columnaTelefono.set_min_width(160)
        columnaTelefono.set_sort_column_id(2)
        vista.append_column(columnaTelefono)

        celdaCompra = Gtk.CellRendererText()
        columnaMail = Gtk.TreeViewColumn('Mail', celdaCompra, text=3)
        columnaMail.set_min_width(160)
        columnaMail.set_sort_column_id(0)
        vista.append_column(columnaMail)

        celdaVenta = Gtk.CellRendererText()
        columnaDireccion = Gtk.TreeViewColumn('Direccion', celdaVenta, text=4)
        columnaDireccion.set_min_width(160)
        columnaDireccion.set_sort_column_id(0)
        vista.append_column(columnaDireccion)

        celdaProvedor = Gtk.CellRendererText()
        columnaCodPost = Gtk.TreeViewColumn('Codigo Postal', celdaProvedor, text=5)
        columnaCodPost.set_min_width(160)
        columnaCodPost.set_sort_column_id(0)
        vista.append_column(columnaCodPost)

        celdaProvincia = Gtk.CellRendererText()
        columnaProvincia = Gtk.TreeViewColumn('Provincia', celdaProvincia, text=6)
        columnaProvincia.set_min_width(160)
        columnaProvincia.set_sort_column_id(0)
        vista.append_column(columnaProvincia)

        self.show_all()

if __name__ == "__main__":
    ListaClientes()
    Gtk.main()
