import os
import gi

gi.require_version("Gtk", '3.0')
from gi.repository import Gtk
from reportlab.platypus import (SimpleDocTemplate, PageBreak, Image, Spacer, Paragraph, TableStyle, Table)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from sqlite3 import dbapi2

class InformePedidos(Gtk.Window):

    def __init__(self):


        bbdd = dbapi2.connect("bbdd.dat")

        cursor = bbdd.cursor()

        detallePedido = []
        facturas = []

        cursorConsultaPedidos = cursor.execute("select NombreEmpresa,producto, cantidad, precioVenta, fechaEntrega, total from Pedidos")

        detallePedido.append(['Cliente','Producto','Cantidade', 'Precio/Kg', 'Fecha Entrega','Total'])

        for row in cursorConsultaPedidos:
            detallePedido.append([row[0],row[1],row[2],row[3],row[4],row[5]])


        facturas.append(list(detallePedido))

        doc = SimpleDocTemplate("ListadoPedidos.pdf", pagesize=A4)
        guion = []

        for factura in facturas:
            taboa = Table(factura, colWidths=[6*20,4*20,4*20,4*20,4*20,4*20], rowHeights=30)

            taboa.setStyle(TableStyle([

                ('TEXTCOLOR', (0, 1), (-1, -1), colors.darkblue),

                ('BACKGROUND', (0, 0), (5, 1), colors.darkcyan),

                ('BACKGROUND', (0, 1), (-1, -1), colors.aliceblue),

                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),


                ('BOX', (0, 0), (-1, -1), 1, colors.black),

                ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.grey),

            ]))
            guion.append(taboa)
            guion.append(Spacer(0, 20))
            guion.append(PageBreak())

        doc.build(guion)


if __name__ == "__main__":
    InformePedidos()
    Gtk.main()