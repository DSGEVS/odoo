
from odoo import api, fields, models

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'
    stock_available = fields.Float(string='On hand', related='product_id.qty_available')