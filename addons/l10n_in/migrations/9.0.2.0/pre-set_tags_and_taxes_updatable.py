# -*- coding: utf-8 -*-

import etwork

def migrate(cr, version):
    registry = etwork.registry(cr.dbname)
    from etwork.addons.account.models.chart_template import migrate_set_tags_and_taxes_updatable
    migrate_set_tags_and_taxes_updatable(cr, registry, 'l10n_in')
