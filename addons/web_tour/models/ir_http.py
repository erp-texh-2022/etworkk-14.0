# -*- coding: utf-8 -*-
# Part of etwork. See LICENSE file for full copyright and licensing details.

from etwork import models
from etwork.http import request


class Http(models.AbstractModel):
    _inherit = 'ir.http'

    def session_info(self):
        result = super(Http, self).session_info()
        if result['is_admin']:
            result['web_tours'] = request.env['web_tour.tour'].get_consumed_tours()
        return result
