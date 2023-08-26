# -*- coding: utf-8 -*-
# Part of etwork. See LICENSE file for full copyright and licensing details.

from etwork import api, models, _


class Channel(models.Model):
    _inherit = 'mail.channel'

    def _execute_command_help(self, **kwargs):
        super(Channel, self)._execute_command_help(**kwargs)
        self.env['mail.bot']._apply_logic(self, kwargs, command="help")  # kwargs are not usefull but...

    @api.model
    def init_etworkbot(self):
        if self.env.user.etworkbot_state in [False, 'not_initialized']:
            etworkbot_id = self.env['ir.model.data'].xmlid_to_res_id("base.partner_root")
            channel_info = self.channel_get([etworkbot_id])
            channel = self.browse(channel_info['id'])
            message = _("Hello,<br/>etwork's chat helps employees collaborate efficiently. I'm here to help you discover its features.<br/><b>Try to send me an emoji</b> <span class=\"o_etworkbot_command\">:)</span>")
            channel.sudo().message_post(body=message, author_id=etworkbot_id, message_type="comment", subtype_xmlid="mail.mt_comment")
            self.env.user.etworkbot_state = 'onboarding_emoji'
            return channel
