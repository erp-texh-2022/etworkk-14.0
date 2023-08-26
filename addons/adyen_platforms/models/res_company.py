# -*- coding: utf-8 -*-
# Part of etwork. See LICENSE file for full copyright and licensing details.

from etwork import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    adyen_account_id = fields.Many2one('adyen.account', string='Adyen Account', readonly=True)
