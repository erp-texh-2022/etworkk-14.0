# -*- coding: utf-8 -*-
# Part of etwork. See LICENSE file for full copyright and licensing details.

# Copyright (C) 2014 Tech Receptives (<http://techreceptives.com>).
from . import models

def _preserve_tag_on_taxes(cr, registry):
    from etwork.addons.account.models.chart_template import preserve_existing_tags_on_taxes
    preserve_existing_tags_on_taxes(cr, registry, 'l10n_sg')
