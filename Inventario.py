import gi
from sqlite3 import dbapi2

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Inventario(Gtk.Window):

    """Ventana Inventario para engadir e mostrar todos os productos da fruteria coas suas caracteristicas

        Metodos:

        __init__ --Constructor
        on_btnEngadir_clicked -- Gardamos un novo producto

        """


    def __init__(self):

        """Constructor  da clase Inventario (Window)
            TreeView que mostra todos os productos da base de datos e permite engadir novos productos

                :param None

                Excepcions:
                -Non ten

                """
        Gtk.Window.__init__(self, title="Inventario")
        bbdd = dbapi2.connect("bbdd.dat")
        self.cursor = bbdd.cursor()
        '''self.cursor.execute("create table Productos(producto text, cantidade float, precioCompra float, precioVenta float, provedor text,contacto text)")
        self.cursor.execute("insert into Productos values('naranja',3,1,2,'Pepe','676432212')")
        self.cursor.execute("insert into Productos values('manzana',2,3,4,'Sara','65633423312')")
        self.cursor.execute("insert into Productos values('platano',5,1.5,3.2,'Gabriel','5544332322')")
        #self.cursor.execute("drop table Productos")
        self.cursor.execute("commit")'''


        boxV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(boxV)

        modelo = Gtk.ListStore(str, float, float,float, str,str)
        cursorProducto = self.cursor.execute("select producto,cantidade,precioCompra,precioVenta,provedor,contacto from Productos")
        for row in cursorProducto:
            modelo.append([row[0],row[1],row[2],row[3],row[4],row[5]])

        vista = Gtk.TreeView(model=modelo)
        boxV.pack_start(vista,True,True,0)

        celdaText = Gtk.CellRendererText()
        columnaProducto = Gtk.TreeViewColumn('Producto', celdaText, text=0)
        columnaProducto.set_min_width(160)
        columnaProducto.set_sort_column_id(0)
        vista.append_column(columnaProducto)

        celdaNum = Gtk.CellRendererText()
        columnaCantidade = Gtk.TreeViewColumn('Cantidade/Kgs', celdaNum, text=1)
        columnaCantidade.set_min_width(160)
        columnaCantidade.set_sort_column_id(2)
        vista.append_column(columnaCantidade)

        celdaCompra = Gtk.CellRendererText()
        columnaCompra = Gtk.TreeViewColumn('Precio Compra', celdaCompra, text=2)
        columnaCompra.set_min_width(160)
        columnaCompra.set_sort_column_id(0)
        vista.append_column(columnaCompra)

        celdaVenta = Gtk.CellRendererText()
        columnaVentas = Gtk.TreeViewColumn('Precio Venta', celdaVenta, text=3)
        columnaVentas.set_min_width(160)
        columnaVentas.set_sort_column_id(0)
        vista.append_column(columnaVentas)

        celdaProvedor = Gtk.CellRendererText()
        columnaProvedor = Gtk.TreeViewColumn('Provedor', celdaProvedor, text=4)
        columnaProvedor.set_min_width(160)
        columnaProvedor.set_sort_column_id(0)
        vista.append_column(columnaProvedor)

        celdaContacto = Gtk.CellRendererText()
        columnaContacto = Gtk.TreeViewColumn('Contacto', celdaContacto, text=5)
        columnaContacto.set_min_width(160)
        columnaContacto.set_sort_column_id(0)
        vista.append_column(columnaContacto)



        boxH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.txtProducto = Gtk.Entry()
        self.txtCantidade = Gtk.Entry()
        self.txtCompra = Gtk.Entry()
        self.txtVenta = Gtk.Entry()
        self.txtProvedor = Gtk.Entry()
        self.txtContacto = Gtk.Entry()


        boxH.pack_start(self.txtProducto, True, True, 0)
        boxH.pack_start(self.txtCantidade, True, True, 0)
        boxH.pack_start(self.txtCompra, True, True, 0)
        boxH.pack_start(self.txtVenta, True, True, 0)
        boxH.pack_start(self.txtProvedor, True, True, 0)
        boxH.pack_start(self.txtContacto, True, True, 0)



        btnEngadir = Gtk.Button(label="Engadir")
        btnEngadir.connect("clicked", self.on_btnEngadir_clicked,modelo)
        boxH.pack_start( btnEngadir, True, True, 0)
        boxV.pack_start(boxH, True, True, 0)

        self.show_all()


    def on_btnEngadir_clicked(self,cursor,modelo):

        """Recolle a informacion obtida nos Gtk.Entry e engade os seus valores a taboa Productos da base de datos
           Finalmente vacia todos os cadros de texto  para poder gardar outro producto

           :param cursor: consultas na bbdd
           :param modelo: ListStore do TreeView
           :return: None
           :raises: dbapi2.DatabaseError

           """

        producto =self.txtProducto.get_text()
        cantidade = float(self.txtCantidade.get_text())
        precioCompra =  float(self.txtCompra.get_text())
        precioVenta = float(self.txtVenta.get_text())
        provedor = self.txtProvedor.get_text()
        contacto = self.txtContacto.get_text()

        datos=[producto,cantidade,precioCompra,precioVenta,provedor,contacto]
        modelo.append(datos)

        self.cursor.execute("insert into Productos (producto,cantidade,precioCompra,precioVenta,provedor,contacto) values(?,?,?,?,?,?)",(producto,cantidade,precioCompra,precioVenta,provedor,contacto))
        try:
            self.cursor.execute("commit")

        except (dbapi2.DatabaseError):
         print("Guardado en la base de datos")

        self.txtProducto.set_text("")
        self.txtCantidade.set_text("")
        self.txtCompra.set_text("")
        self.txtVenta.set_text("")
        self.txtProvedor.set_text("")
        self.txtContacto.set_text("")


if __name__ == "__main__":
    Inventario()
    Gtk.main()
