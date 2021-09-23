from odoo import models, fields, api, _
from datetime import datetime


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    bom_id = fields.Many2one('mrp.bom', string='BOM',
               domain="[('product_tmpl_id.product_variant_ids', '=', product_id),"
               "'|', ('product_id', '=', product_id), "
               "('product_id', '=', False)]")


    @api.onchange('bom_id')
    def _computed_cost_line(self):
        if (self.bom_id and self.product_id):
            description = self.product_id.name + '\n'
            for bom_line in self.bom_id.bom_line_ids:
                description = description + '  •  ' + str(bom_line.product_qty) + '  ' + str(
                    bom_line.product_id.name) + '\n'
            self.name = str(description)
