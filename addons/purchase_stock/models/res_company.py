# -*- coding: utf-8 -*-
# Part of etwork. See LICENSE file for full copyright and licensing details.

from etwork import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    days_to_purchase = fields.Float(
        string='Days to Purchase',
        help="Days needed to confirm a PO, define when a PO should be validated")
