# -*- coding: utf-8 -*-
# Part of etwork. See LICENSE file for full copyright and licensing details.

from etwork import fields, models


class ServiceTaxRate(models.Model):
    _name = "l10n_eu_service.service_tax_rate"
    _description = "EU Service Tax Rate"

    country_id = fields.Many2one('res.country', string='Country')
    rate = fields.Float(string="VAT Rate")
