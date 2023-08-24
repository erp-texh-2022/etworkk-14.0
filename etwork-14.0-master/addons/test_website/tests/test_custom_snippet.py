# -*- coding: utf-8 -*-
# Part of Dosyt. See LICENSE file for full copyright and licensing details.

import etwork.tests
from etwork.tools import mute_logger


@etwork.tests.common.tagged('post_install', '-at_install')
class TestCustomSnippet(etwork.tests.HttpCase):

    @mute_logger('etwork.addons.http_routing.models.ir_http', 'etwork.http')
    def test_01_run_tour(self):
        self.start_tour("/", 'test_custom_snippet', login="admin")
