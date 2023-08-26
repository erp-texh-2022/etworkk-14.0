# Part of etwork. See LICENSE file for full copyright and licensing details.

from etwork.addons.account.models.chart_template import update_taxes_from_templates


def migrate(cr, version):
    update_taxes_from_templates(cr, 'l10n_es.account_chart_template_common')
