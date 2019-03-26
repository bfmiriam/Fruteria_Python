import os
import gi

gi.require_version("Gtk", '3.0')
from gi.repository import Gtk
from reportlab.platypus import (SimpleDocTemplate, PageBreak, Image, Spacer, Paragraph, TableStyle, Table)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from sqlite3 import dbapi2

class XerarFactura(Gtk.Window):

    def __init__(self,cliente):


        bbdd = dbapi2.connect("bbdd.dat")
        cursor = bbdd.cursor()

        detallePedido = []
        facturas = []

        cursorConsultaEmpresa = cursor.execute("select NombreEmpresa, telefono, direccion, codPostal,provincia from Clientes where NombreEmpresa=?",(cliente,))

        for row in cursorConsultaEmpresa:
            detallePedido.append(['Nome: ', row[0], '', '', ''])
            detallePedido.append(['Telefono: ', row[1], '', '', ''])
            detallePedido.append(['Direccion: ', row[2], '', '', ''])
            detallePedido.append(['Codigo Postal: ', row[3], '', 'Provincia: ', row[4]])

        cursorConsultaPedidos = cursor.execute("select producto, cantidad,precioVenta, fechaEntrega, total from Pedidos where NombreEmpresa=?",(cliente,))

        detallePedido.append(["", "", "", "", ""])
        detallePedido.append(["Producto", "Cantidade", "Precio/Kg", "Fecha Entrega", "Total"])

        prezoTotal = 0

        for row in cursorConsultaPedidos:
            detallePedido.append([row[0],row[1],row[2],row[3],row[4]])
            prezoTotal = prezoTotal + row[4]

        detallePedido.append(["", "", "", "Prezo total:", prezoTotal])
        facturas.append(list(detallePedido))

        doc = SimpleDocTemplate("FacturaCliente.pdf", pagesize=A4)
        guion = []

        for factura in facturas:
            taboa = Table(factura, colWidths=80, rowHeights=30)

            taboa.setStyle(TableStyle([
                ('TEXTCOLOR', (0, 0), (-1, 3), colors.blue),

                ('TEXTCOLOR', (0, 4), (-1, -1), colors.green),

                ('BACKGROUND', (0, 5), (-1, -1), colors.aliceblue),

                #('ALIGN', (2, 5), (-1, -1), 'RIGHT'),

                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),

                ('BOX', (0, 0), (-1, 3), 1, colors.black),

                ('BOX', (0, 5), (-1, -2), 1, colors.black),

                ('INNERGRID', (0, 5), (-1, -2), 0.5, colors.grey),

            ]))
            guion.append(taboa)
            guion.append(Spacer(0, 20))
            guion.append(PageBreak())

        doc.build(guion)


if __name__ == "__main__":
    XerarFactura()
    Gtk.main()