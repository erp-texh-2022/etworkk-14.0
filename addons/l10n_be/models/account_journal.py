# -*- coding: utf-8 -*-
# Part of etwork. See LICENSE file for full copyright and licensing details.
from etwork import fields, models


class AccountJournal(models.Model):
    _inherit = 'account.journal'

    invoice_reference_model = fields.Selection(selection_add=[
        ('be', 'Belgium')
        ], ondelete={'be': lambda recs: recs.write({'invoice_reference_model': 'etwork'})})

