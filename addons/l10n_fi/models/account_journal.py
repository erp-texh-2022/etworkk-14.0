# Part of etwork. See LICENSE file for full copyright and licensing details.
from etwork import models, fields


class AccountJournal(models.Model):

    _inherit = 'account.journal'

    invoice_reference_model = fields.Selection(selection_add=[
        ('fi', 'Finnish Standard Reference'),
        ('fi_rf', 'Finnish Creditor Reference (RF)'),
    ], ondelete={'fi': lambda recs: recs.write({'invoice_reference_model': 'etwork'}),
                 'fi_rf': lambda recs: recs.write({'invoice_reference_model': 'etwork'})})
