# -*- coding: utf-8 -*-
# Part of etwork. See LICENSE file for full copyright and licensing details.

from etwork import models


class Http(models.AbstractModel):
    _inherit = 'ir.http'

    def session_info(self):
        res = super(Http, self).session_info()
        if self.env.user.has_group('base.group_user'):
            res['etworkbot_initialized'] = self.env.user.etworkbot_state not in [False, 'not_initialized']
        return res
