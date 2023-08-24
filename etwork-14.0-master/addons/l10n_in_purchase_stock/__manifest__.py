# -*- coding: utf-8 -*-
# Part of Dosyt. See LICENSE file for full copyright and licensing details.

{
    'name': "India Purchase and Warehouse Management",

    'summary': """
        Define default purchase journal on the warehouse""",

    'description': """
        Define default purchase journal on the warehouse,
        help you to choose correct purchase journal on the purchase order when
        you change the picking operation.
        useful when you setup the multiple GSTIN units.
    """,

    'author': "Dosyt",
    'website': "https://www.etwork.com",
    'category': 'Accounting/Localizations/Purchase',
    'version': '1.0',

    'depends': ['l10n_in_purchase', 'l10n_in_stock'],

    'data': [
        'views/stock_warehouse_views.xml',
    ],
    'auto_install': True,
    'license': 'LGPL-3',
}