# -*- coding: utf-8 -*-
# Part of etwork. See LICENSE file for full copyright and licensing details.

from etwork import fields, models


class MailMail(models.Model):
    _inherit = 'mail.mail'

    fetchmail_server_id = fields.Many2one('fetchmail.server', "Inbound Mail Server", readonly=True, index=True)
