etwork.define('sms/static/src/bugfix/bugfix_tests.js', function (require) {
'use strict';

/**
 * This file allows introducing new QUnit test modules without contaminating
 * other test files. This is useful when bug fixing requires adding new
 * components for instance in stable versions of etwork. Any test that is defined
 * in this file should be isolated in its own file in master.
 */
QUnit.module('sms', {}, function () {
QUnit.module('bugfix', {}, function () {
QUnit.module('bugfix_tests.js', {

});
});
});

});
