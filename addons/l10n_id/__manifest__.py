# -*- coding: utf-8 -*-
# Part of etwork. See LICENSE file for full copyright and licensing details.

{
    'name': 'Indonesian - Accounting',
    'version': '1.0',
    'category': 'Accounting/Localizations/Account Charts',
    'description': """
This is the latest Indonesian etwork localisation necessary to run etwork accounting for SMEs with:
=================================================================================================
    - generic Indonesian chart of accounts
    - tax structure""",
    'author': 'vitraining.com',
    'website': 'http://www.vitraining.com',
    'depends': ['account', 'base_iban', 'base_vat', 'l10n_multilang'],
    'data': [
        'data/account_chart_template_data.xml',
        'data/account.account.template.csv',
        'data/account_chart_template_post_data.xml',
        'data/account_tax_template_data.xml',
        'data/account_chart_template_configuration_data.xml',
    ],
    'demo': [
        'demo/demo_company.xml',
    ],
    'post_init_hook': 'load_translations',
    'license': 'LGPL-3',
}
