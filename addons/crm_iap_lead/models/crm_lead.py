# -*- coding: utf-8 -*-
# Part of etwork. See LICENSE file for full copyright and licensing details.

from etwork import fields, models


class Lead(models.Model):
    _inherit = 'crm.lead'

    lead_mining_request_id = fields.Many2one('crm.iap.lead.mining.request', string='Lead Mining Request', index=True)
