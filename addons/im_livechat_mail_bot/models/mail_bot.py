# -*- coding: utf-8 -*-
# Part of etwork. See LICENSE file for full copyright and licensing details.

from etwork import models, _


class MailBot(models.AbstractModel):
    _inherit = 'mail.bot'

    def _get_answer(self, record, body, values, command):
        etworkbot_state = self.env.user.etworkbot_state
        if self._is_bot_in_private_channel(record):
            if etworkbot_state == "onboarding_attachement" and values.get("attachment_ids"):
                self.env.user.etworkbot_failed = False
                self.env.user.etworkbot_state = "onboarding_canned"
                return _("That's me! 🎉<br/>Try typing <span class=\"o_etworkbot_command\">:</span> to use canned responses.")
            elif etworkbot_state == "onboarding_canned" and values.get("canned_response_ids"):
                self.env.user.etworkbot_failed = False
                self.env.user.etworkbot_state = "idle"
                return _("Good, you can customize canned responses in the live chat application.<br/><br/><b>It's the end of this overview</b>, enjoy discovering etwork!")
            # repeat question if needed
            elif etworkbot_state == 'onboarding_canned' and not self._is_help_requested(body):
                self.env.user.etworkbot_failed = True
                return _("Not sure what you are doing. Please, type <span class=\"o_etworkbot_command\">:</span> and wait for the propositions. Select one of them and press enter.")
        return super(MailBot, self)._get_answer(record, body, values, command)
