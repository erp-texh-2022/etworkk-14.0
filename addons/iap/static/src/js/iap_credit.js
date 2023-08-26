etwork.define('iap.redirect_etwork_credit_widget', function(require) {
"use strict";

var AbstractAction = require('web.AbstractAction');
var core = require('web.core');


var IapetworkCreditRedirect = AbstractAction.extend({
    template: 'iap.redirect_to_etwork_credit',
    events : {
        "click .redirect_confirm" : "etwork_redirect",
    },
    init: function (parent, action) {
        this._super(parent, action);
        this.url = action.params.url;
    },

    etwork_redirect: function () {
        window.open(this.url, '_blank');
        this.do_action({type: 'ir.actions.act_window_close'});
        // framework.redirect(this.url);
    },

});
core.action_registry.add('iap_etwork_credit_redirect', IapetworkCreditRedirect);
});
