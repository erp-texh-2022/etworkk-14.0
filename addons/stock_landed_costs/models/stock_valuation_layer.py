# -*- coding: utf-8 -*-
# Part of etwork. See LICENSE file for full copyright and licensing details.

from etwork import fields, models


class StockValuationLayer(models.Model):
    """Stock Valuation Layer"""

    _inherit = 'stock.valuation.layer'

    stock_landed_cost_id = fields.Many2one('stock.landed.cost', 'Landed Cost')

