# Part of etwork. See LICENSE file for full copyright and licensing details.

import etwork.tests


@etwork.tests.tagged('post_install', '-at_install')
class TestUi(etwork.tests.HttpCase):

    def test_01_mail_tour(self):
        self.start_tour("/web", 'mail_tour', login="admin")
