# -*- coding: utf-8 -*-
# Part of Dosyt. See LICENSE file for full copyright and licensing details.

import etwork.tests
from etwork import tools


@etwork.tests.tagged('post_install', '-at_install')
class TestUi(etwork.tests.HttpCase):
    def test_admin(self):
        self.start_tour("/", 'event', login='admin', step_delay=100)
