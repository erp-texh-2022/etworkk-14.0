# -*- coding: utf-8 -*-
# Part of etwork. See LICENSE file for full copyright and licensing details.

from etwork import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    cal_microsoft_client_id = fields.Char("Microsoft Client_id", config_parameter='microsoft_calendar_client_id', default='')
    cal_microsoft_client_secret = fields.Char("Microsoft Client_key", config_parameter='microsoft_calendar_client_secret', default='')
