# -*- coding: utf-8 -*-
# Part of etwork. See LICENSE file for full copyright and licensing details.

from etwork import models


class StockMove(models.Model):
    _inherit = 'stock.move'

    def _should_force_price_unit(self):
        self.ensure_one()
        return self.is_subcontract or super()._should_force_price_unit()
