import gi
from sqlite3 import dbapi2

gi.require_version("Gtk", '3.0')
from gi.repository import Gtk


class EngadirClientes(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Engadir Clientes")

        bbdd = dbapi2.connect("bbdd.dat")
        self.cursor = bbdd.cursor()
        #self.cursor.execute("create table Clientes(NombreEmpresa text,CIF text, telefono text, email text, direccion text, codPostal text,provincia text)")
        #self.cursor.execute("commit")

        builder = Gtk.Builder()
        builder.add_from_file("NovoCliente.glade")
        fiestra = builder.get_object("window")

        self.txtNombre = builder.get_object("txtEmpresa")
        self.txtCif = builder.get_object("txtCif")
        self.txtTelefono = builder.get_object("txtTelefono")
        self.txtCorreo = builder.get_object("txtCorreo")
        self.txtDireccion = builder.get_object("txtDireccion")
        self.txtCp = builder.get_object("txtCp")
        self.cbProvincia = builder.get_object("cbProvincia")
        self.btnAceptar = builder.get_object("btnAceptar")

        sinais = {
            "on_btnAceptar_clicked": self.on_btnAceptar_clicked,
        }
        builder.connect_signals(sinais)


        fiestra.show_all()

    def on_btnAceptar_clicked(self,guardar):

        nombre =self.txtNombre.get_text()
        cif =self.txtCif.get_text()
        telefono = self.txtTelefono.get_text()
        mail =  self.txtCorreo.get_text()
        direccion = self.txtDireccion.get_text()
        codPostal = self.txtCp.get_text()
        provincia = self.cbProvincia.get_active_text()


        self.cursor.execute("insert into Clientes (NombreEmpresa,CIF,telefono,email,direccion,codPostal,provincia) values(?,?,?,?,?,?,?)",(nombre,cif,telefono,mail,direccion,codPostal,provincia))
        try:
            self.cursor.execute("commit")

        except (dbapi2.DatabaseError):
            print("Guardado en la base de datos")

        self.txtNombre.set_text('')
        self.txtCif.set_text('')
        self.txtTelefono.set_text('')
        self.txtCorreo.set_text('')
        self.txtDireccion.set_text('')
        self.txtCp.set_text('')
        self.cbProvincia.set_active(-1)


if __name__ == "__main__":
    EngadirClientes()
    Gtk.main()