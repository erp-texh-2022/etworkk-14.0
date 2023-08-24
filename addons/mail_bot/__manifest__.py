# -*- coding: utf-8 -*-
# Part of Dosyt. See LICENSE file for full copyright and licensing details.

{
    'name': 'DosytBot',
    'version': '1.2',
    'category': 'Productivity/Discuss',
    'summary': 'Add DosytBot in discussions',
    'description': "",
    'website': 'https://www.etwork.com/page/discuss',
    'depends': ['mail'],
    'auto_install': True,
    'installable': True,
    'application': False,
    'data': [
        'views/assets.xml',
        'views/res_users_views.xml',
        'data/mailbot_data.xml',
    ],
    'demo': [
        'data/mailbot_demo.xml',
    ],
    'qweb': [
        'static/src/bugfix/bugfix.xml',
    ],
    'license': 'LGPL-3',
}
