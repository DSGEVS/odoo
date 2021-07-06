# -*- coding: utf-8 -*-
# Copyright (C) 2018-present  Technaureus Info Solutions Pvt. Ltd.(<http://www.technaureus.com/>).

import xlsxwriter
from odoo import api, fields, models
import pytz
from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT

class StockCardReportXlsx(models.AbstractModel):
    _name = 'report.stock_card.card_report_xls.xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def get_lines(self, obj):
        lines = []
        domain = [
            ('state', '=', 'done'),
            ('product_id', '=', obj.product_id.id),
            '|',
            ('location_id', '=', obj.location_id.id),
            ('location_dest_id', '=', obj.location_id.id),
            ('date', '>=', obj.start_date),
            ('date', '<=', obj.end_date),
        ]
        sale_order = self.env['stock.move'].search(domain, order='date desc')

        user_tz = pytz.timezone(self.env.context.get('tz') or self.env.user.tz or 'UTC')
        lang = self._context.get("lang")
        record_lang = self.env["res.lang"].search([("code", "=", lang)], limit=1)

        for value in sale_order:
            qty_in = 0
            qty_out = 0
            reference = ""
            ot = ""
            if obj.location_id.id == value.location_dest_id.id:
                qty_in = value.product_qty
            else:
                qty_out = value.product_qty
            if not value.picking_id:
                reference = "Ajuste de inventario"
            else:
                reference = value.picking_id.name

            vals = {
                'ref': reference,
                'product_id': value.product_id.id,
                'product': value.product_id.display_name,
                'location_id': value.location_dest_id.id,
                'origen': value.location_id.display_name,
                'destino': value.location_dest_id.display_name,
                'date': value.date, #pytz.UTC.localize(datetime.strptime(value.date, DEFAULT_SERVER_DATETIME_FORMAT)).astimezone(user_tz),
                'qty_in': qty_in,
                'qty_out': qty_out,
                'saldo': value.product_id.with_context({'to_date': value.date,'location' : obj.location_id.id}).qty_available
            }
            lines.append(vals)
        return lines

    def generate_xlsx_report(self, workbook, data, wizard_obj):
        for obj in wizard_obj:
            lines = self.get_lines(obj)
            worksheet = workbook.add_worksheet('Report')
            
            bold = workbook.add_format({'bold': True, 'align': 'center'})
            bold1 = workbook.add_format({'bold': True})
            text = workbook.add_format({'font_size': 12, 'align': 'center'})
            text1 = workbook.add_format({'font_size': 12})
            date_format = workbook.add_format({'num_format': 'yyyy-mm-dd', 'align': 'center'})
            worksheet.set_column(0, 0, 15)
            worksheet.set_column(1, 1, 15)
            worksheet.set_column(2, 2, 15)
            worksheet.set_column(3, 3, 15)
            worksheet.set_column(4, 4, 30)
            worksheet.set_column(5, 5, 30)
            worksheet.merge_range('A1:G1', 'STOCK CARD REPORT', bold)             
            worksheet.write('A2', 'Product:', bold1)
            worksheet.merge_range('B2:G2', lines[0]['product'], text1)
            worksheet.write('A3', 'Start date:', bold1)
            worksheet.write('B3', obj.start_date, date_format)
            worksheet.write('C3', 'End date:', bold1)
            worksheet.write('D3', obj.end_date, date_format)
            worksheet.write('A4', 'Location:', bold1)
            worksheet.write('B4', obj.location_id.display_name, text1)
            worksheet.write('A6', 'Reference', bold)
            worksheet.write('B6', 'Date', bold)
            worksheet.write('C6', 'In', bold)
            worksheet.write('D6', 'Out', bold)
            worksheet.write('E6', 'Source', bold)
            worksheet.write('F6', 'Send to', bold)
            worksheet.write('G6', 'Balance', bold)
            row = 6
            col = 0

            for res in lines:
                #date_time = datetime.strptime(res['date'],'%Y-%m-%d %H:%M:%S')
                worksheet.write(row, col, res['ref'], text)
                worksheet.write(row, col + 1, res['date'], date_format)
                worksheet.write(row, col + 2, res['qty_in'], text)
                worksheet.write(row, col + 3, res['qty_out'], text)
                worksheet.write(row, col + 4, res['origen'], text)
                worksheet.write(row, col + 5, res['destino'], text)
                worksheet.write(row, col + 6, res['saldo'], text)
                row = row + 1
            worksheet.add_table('A7:G' + str(row), {'autofilter': False,'header_row': False})
