
from odoo import api, fields, models


class StockPicking(models.Model):
    _inherit = 'stock.move'
    stock_available = fields.Float(string='On hand', related='product_id.qty_available')