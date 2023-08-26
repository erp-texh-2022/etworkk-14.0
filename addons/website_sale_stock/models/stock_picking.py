# -*- coding: utf-8 -*-
# Part of etwork. See LICENSE file for full copyright and licensing details.

from etwork import models, api, fields
from etwork.tools.translate import _


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    website_id = fields.Many2one('website', related='sale_id.website_id', string='Website',
                                 help='Website this picking belongs to.',
                                 store=True, readonly=True)

