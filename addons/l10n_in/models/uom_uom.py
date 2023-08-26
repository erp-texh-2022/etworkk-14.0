# -*- coding: utf-8 -*-
# Part of etwork. See LICENSE file for full copyright and licensing details.

from etwork import fields, models


class UoM(models.Model):
    _inherit = "uom.uom"

    # As per GST Rules you need to Specify UQC given by GST.
    l10n_in_code = fields.Char("Indian GST UQC", help="Unique Quantity Code (UQC) under GST")
