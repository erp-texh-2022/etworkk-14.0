import etwork.tests
from etwork.tools import mute_logger


@etwork.tests.common.tagged('post_install', '-at_install')
class TestWebsiteError(etwork.tests.HttpCase):

    @mute_logger('etwork.addons.http_routing.models.ir_http', 'etwork.http')
    def test_01_run_test(self):
        self.start_tour("/test_error_view", 'test_error_website')
