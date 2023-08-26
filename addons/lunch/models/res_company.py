# -*- coding: utf-8 -*-
# Part of etwork. See LICENSE file for full copyright and licensing details.

from etwork import models, fields


class Company(models.Model):
    _inherit = 'res.company'

    lunch_minimum_threshold = fields.Float()
