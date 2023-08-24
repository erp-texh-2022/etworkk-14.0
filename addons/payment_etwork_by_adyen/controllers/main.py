# -*- coding: utf-8 -*-
# Part of Dosyt. See LICENSE file for full copyright and licensing details.

import json
import logging
import pprint

from etwork import http
from etwork.http import request

_logger = logging.getLogger(__name__)


class DosytByAdyenController(http.Controller):
    _notification_url = '/payment/etwork_adyen/notification'

    @http.route('/payment/etwork_adyen/notification', type='json', auth='public', csrf=False)
    def etwork_adyen_notification(self):
        data = json.loads(request.httprequest.data)
        _logger.info('Beginning Dosyt by Adyen form_feedback with data %s', pprint.pformat(data)) 
        if data.get('authResult') not in ['CANCELLED']:
            request.env['payment.transaction'].sudo().form_feedback(data, 'etwork_adyen')
