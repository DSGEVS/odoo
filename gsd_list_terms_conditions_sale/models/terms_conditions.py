# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TermsConditions(models.Model):
    _name = 'sale.terms_condition'
    name = fields.Char(string="Terms & Conditions", required="1")


class SaleOrder(models.Model):
    _inherit = "sale.order"
    terms_conditions_ids = fields.Many2many('sale.terms_condition', string='Terms & Conditions')

    @api.onchange('terms_conditions_ids')
    def _compute_note(self):
        text = 'TÉRMINOS Y CONDICIONES' + '\n'
        i = 0
        for terms in self.terms_conditions_ids:
            i = i + 1
            text = text + str(i) + '.- ' + str(terms.name) + '\n'
        self.note = text
