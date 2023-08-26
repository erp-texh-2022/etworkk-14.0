import etwork.tests
# Part of etwork. See LICENSE file for full copyright and licensing details.


@etwork.tests.tagged('post_install', '-at_install')
class TestUi(etwork.tests.HttpCase):

    def test_01_sale_tour(self):
        self.start_tour("/web", 'sale_tour', login="admin", step_delay=100)
