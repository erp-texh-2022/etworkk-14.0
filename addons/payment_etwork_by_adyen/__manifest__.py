# -*- coding: utf-8 -*-
# Part of etwork. See LICENSE file for full copyright and licensing details.

{
    'name': 'etwork Payments by Adyen Payment Acquirer',
    'category': 'Accounting/Payment Acquirers',
    'sequence': 330,
    'summary': 'Payment Acquirer: etwork Payments by Adyen',
    'version': '1.0',
    'description': """etwork Payments by Adyen""",
    'depends': ['payment', 'adyen_platforms'],
    'data': [
        'views/payment_views.xml',
        'views/payment_etwork_by_adyen_templates.xml',
        'data/payment_acquirer_data.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
