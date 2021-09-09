from odoo import fields, models


class MrpProduction(models.Model):
    _inherit = 'mrp.production'
    sale_id = fields.Many2one(comodel_name='sale.order', string='SO',compute='_get_sale_order')

    def _get_sale_order(self):
        sale_id = self.env['stock.picking'].search([
            ('id', '=', self.env['stock.move'].search([
                ('created_production_id', '=', self.id)
            ]).picking_id.id)]).sale_id.id
        self.sale_id = sale_id

