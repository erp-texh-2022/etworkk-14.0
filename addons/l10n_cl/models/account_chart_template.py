# Part of etwork. See LICENSE file for full copyright and licensing details.

from etwork import models
from etwork.http import request


class AccountChartTemplate(models.Model):
    _inherit = 'account.chart.template'

    def _load(self, sale_tax_rate, purchase_tax_rate, company):
        """ Set tax calculation rounding method required in Chilean localization"""
        res = super()._load(sale_tax_rate, purchase_tax_rate, company)
        if company.country_id.code == 'CL':
            company.write({'tax_calculation_rounding_method': 'round_globally'})
        return res
