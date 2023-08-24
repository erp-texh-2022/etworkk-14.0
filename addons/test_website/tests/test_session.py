import etwork.tests
from etwork.tools import mute_logger


@etwork.tests.common.tagged('post_install', '-at_install')
class TestWebsiteSession(etwork.tests.HttpCase):

    def test_01_run_test(self):
        self.start_tour('/', 'test_json_auth')
