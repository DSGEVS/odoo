# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
import logging

class SaleOrder(models.Model):
    _inherit = "sale.order"
    line_bom_description = fields.Boolean(string='Activate Bom description')
    mo_count = fields.Integer(compute='_compute_mp_count')

    def create_mo(self):
            for order_line in self.order_line:
                if (order_line.bom_id and order_line.mo_created == 0):
                    mo = {
                        'product_id': order_line.product_id.id,
                        'product_qty': order_line.product_uom_qty,
                        'product_uom_id': order_line.product_id.uom_id.id,
                        'bom_id': order_line.bom_id.id,
                        'origin': self.name,
                        'company_id': self.company_id.id,
                        'sale_order_id': self.id
                    }
                    self.env['mrp.production'].create(mo)
                    order_line.write({'mo_created': 1})
                    self.message_post(body="Manufacturing orders was created")

    def _compute_mp_count(self):
        self.mo_count = len(self.env['mrp.production'].search([('sale_order_id', '=', self.id)]))

class SaleOrderLine(models.Model):
    _name = 'sale.order.line'
    _inherit = 'sale.order.line'
    bom_id = fields.Many2one('mrp.bom', string='LdM')
    mo_created = fields.Boolean(default=0)
    #domain = [('product_tmpl_id', '=', product_id.product_tmpl_id_id)]
    @api.onchange('bom_id')
    def _computed_cost_line(self):
        sum_cost_prices = 0
        sum_sale_price = 0
        if(self.bom_id and self.product_id):
            description = self.product_id.display_name + '\n'
            for bom_line in self.bom_id.bom_line_ids:
                description = description + '\t' + str(bom_line.product_qty) + '\t' + str(bom_line.product_id.name) + '\n'
            self.name = str(description)


    @api.onchange('product_id')
    def _onchange_product_id_customize(self):
        if self.product_id:
            return {'domain': {'bom_id': [('product_tmpl_id', '=', self.product_id.product_tmpl_id.id)]}}
        else:
            self.bom_id = {'domain': {'bom_id': [('product_tmpl_id', '=', 0)]}}


class MrpProduction(models.Model):
    _inherit = 'mrp.production'
    sale_order_id = fields.Many2one('sale.order',string='Sale Order')


