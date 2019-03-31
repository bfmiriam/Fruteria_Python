import gi
from sqlite3 import dbapi2

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class ModificarClientes(Gtk.Window):

    """Formulario para modificar ou eliminar clientes da base de datos do programa de xestion da fruteria.

        Metodos:

        __init__ --Constructor
        on_btnBuscar_clicked -- recolle o cliente a modificar/eliminar
        on_btnEliminar_clicked -- elimina o cliente seleccionado
        on_btnModificar_clicked -- modifica o cliente seleccionado

        """

    def __init__(self):
        """Constructor  da clase ModificarClientes (Window)
           Formulario que recolle o cliente desexado mediante un ComboBox e mostra todos os seus datos para
           poder visualizalos e modificalos/eliminalos se e o que desexamos

            :param None

             Excepcions:
             -Non ten

             """
        Gtk.Window.__init__(self, title="Modificar Clientes")

        bbdd = dbapi2.connect("bbdd.dat")
        self.cursor = bbdd.cursor()

        self.empresas = []
        cursorEmpresa = self.cursor.execute("select nombreEmpresa from Clientes")

        for row in cursorEmpresa:
            self.empresas.append(row[0])

        builder = Gtk.Builder()
        builder.add_from_file("ModificarEliminar.glade")
        fiestra = builder.get_object("window")

        self.cmbEmpresas = builder.get_object("cmbEmpresas")
        self.txtNombre = builder.get_object("txtEmpresa")
        self.txtCif = builder.get_object("txtCif")
        self.txtTelefono = builder.get_object("txtTelefono")
        self.txtCorreo = builder.get_object("txtCorreo")
        self.txtDireccion = builder.get_object("txtDireccion")
        self.txtCodpost = builder.get_object("txtCodPost")
        self.txtProvincia = builder.get_object("txtProvincia")
        self.btnModificar = builder.get_object("btnModificar")
        self.btnEliminar = builder.get_object("btnEliminar")
        self.btnBuscar = builder.get_object("btnBuscar")


        for empresa in self.empresas:
            self.cmbEmpresas.append_text(empresa)

        sinais = {
            "on_btnBuscar_clicked": self.on_btnBuscar_clicked,
            "on_btnEliminar_clicked": self.on_btnEliminar_clicked,
            "on_btnModificar_clicked": self.on_btnModificar_clicked
        }
        builder.connect_signals(sinais)

        fiestra.show_all()

    def on_btnBuscar_clicked(self,cmbEmpresas):

        """Recolle o nome do  cliente seleccionado no ComboBox e busca os seus datos na base de datos, mostrandoos no formulario

           :param cmbEmpresas: comboBox
           :return: None

           """

        nombre =self.cmbEmpresas.get_active_text()

        cursorCliente = self.cursor.execute("select NombreEmpresa,CIF,telefono,email,direccion,codPostal,provincia from Clientes where NombreEmpresa=?",(nombre,))

        for row in cursorCliente:
            self.txtNombre.set_text(row[0])
            self.txtCif.set_text(row[1])
            self.txtTelefono.set_text(row[2])
            self.txtCorreo.set_text(row[3])
            self.txtDireccion.set_text(row[4])
            self.txtCodpost.set_text(row[5])
            self.txtProvincia.set_text(row[6])

    def on_btnEliminar_clicked(self, cmbEmpresas):

        """Elimina da base de datos o cliente seleccionado no ComboBox e vacia o formulario

             :param cmbEmpresas: comboBox
             :return: None
             :raises: dbapi2.DatabaseError

             """

        nombre = self.cmbEmpresas.get_active_text()

        self.cursor.execute( "delete from Clientes where NombreEmpresa=?",(nombre,))
        try:
            self.cursor.execute("commit")
            print('borrado')

        except (dbapi2.DatabaseError):
            print("Eliminado de la base de datos")

        self.txtNombre.set_text('')
        self.txtCif.set_text('')
        self.txtTelefono.set_text('')
        self.txtCorreo.set_text('')
        self.txtDireccion.set_text('')
        self.txtCodpost.set_text('')
        self.txtProvincia.set_text('')
        self.cmbEmpresas.set_active(-1)

    def on_btnModificar_clicked(self, cmbEmpresas):
        """Recolle os datos mostrados no formulario e actualiza na base de datos o cliente mostrado nel, para rexistrar as modificacions
           e vacia o formulario

             :param cmbEmpresas: comboBox
             :return: None
             :raises: dbapi2.DatabaseError

             """

        nombre = self.cmbEmpresas.get_active_text()

        nombreEmpresa= self.txtNombre.get_text()
        cif = self.txtCif.get_text()
        tlfn = self.txtTelefono.get_text()
        correo = self.txtCorreo.get_text()
        direccion = self.txtDireccion.get_text()
        codPost = self.txtCodpost.get_text()
        provincia = self.txtProvincia.get_text()
        self.cmbEmpresas.set_active(-1)

        self.cursor.execute("update Clientes set NombreEmpresa=?, CIF=?, telefono=?, email=?, direccion=?, codPostal=?, provincia=? where NombreEmpresa=?",
                            (nombreEmpresa,cif,tlfn,correo,direccion,codPost,provincia,nombre))
        try:
            self.cursor.execute("commit")
            print('modificado')

        except (dbapi2.DatabaseError):
            print("Modificado")

        self.txtNombre.set_text('')
        self.txtCif.set_text('')
        self.txtTelefono.set_text('')
        self.txtCorreo.set_text('')
        self.txtDireccion.set_text('')
        self.txtCodpost.set_text('')
        self.txtProvincia.set_text('')

if __name__ == "__main__":
    ModificarClientes()
    Gtk.main()