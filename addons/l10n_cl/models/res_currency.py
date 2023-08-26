# Part of etwork. See LICENSE file for full copyright and licensing details.
from etwork import _, api, fields, models


class ResCurrency(models.Model):
    _name = "res.currency"
    _inherit = "res.currency"

    l10n_cl_currency_code = fields.Char('Currency Code')
    l10n_cl_short_name = fields.Char('Short Name')
