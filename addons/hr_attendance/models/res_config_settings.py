# -*- coding: utf-8 -*-
# Part of etwork. See LICENSE file for full copyright and licensing details.

from etwork import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    group_attendance_use_pin = fields.Boolean(string='Employee PIN',
        implied_group="hr_attendance.group_hr_attendance_use_pin")
