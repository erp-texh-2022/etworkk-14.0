# -*- coding: utf-8 -*-
# Part of etwork. See LICENSE file for full copyright and licensing details.
{
    'name': "etwork referral program",
    'summary': """Allow you to refer your friends to etwork and get rewards""",
    'category': 'Hidden',
    'version': '1.0',
    'depends': ['base', 'web'],
    'data': [
        'views/templates.xml',
    ],
    'qweb': [
        "static/src/xml/systray.xml",
    ],
    'auto_install': False,
    'license': 'LGPL-3',
}
