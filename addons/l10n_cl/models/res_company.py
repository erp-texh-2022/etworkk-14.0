# -*- coding: utf-8 -*-
# Part of etwork. See LICENSE file for full copyright and licensing details.
from etwork import models, fields


class ResCompany(models.Model):
    _inherit = "res.company"

    def _localization_use_documents(self):
        """ Chilean localization use documents """
        self.ensure_one()
        return self.country_id.code == "CL" or super()._localization_use_documents()
