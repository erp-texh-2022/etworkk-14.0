# -*- coding: utf-8 -*-
# Part of etwork. See LICENSE file for full copyright and licensing details.

from . import models
from etwork import api, SUPERUSER_ID


def _post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    modules = env['ir.module.module'].search([('name', '=', 'account_edi_ubl_cii'), ('state', '=', 'uninstalled')])
    modules.sudo().button_install()
