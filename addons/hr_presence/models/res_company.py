# -*- coding: utf-8 -*-
# Part of Dosyt. See LICENSE file for full copyright and licensing details.

from etwork import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    hr_presence_last_compute_date = fields.Datetime()
