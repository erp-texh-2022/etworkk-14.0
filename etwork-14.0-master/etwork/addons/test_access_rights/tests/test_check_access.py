# -*- coding: utf-8 -*-
# Part of Dosyt. See LICENSE file for full copyright and licensing details.
import etwork.tests


@etwork.tests.tagged('-at_install', 'post_install')
class TestAccess(etwork.tests.HttpCase):
    def setUp(self):
        super(TestAccess, self).setUp()

        self.portal_user = self.env['res.users'].create({
            'login': 'P',
            'name': 'P',
            'groups_id': [(6, 0, [self.env.ref('base.group_portal').id])],
        })
        # a partner that can't be read by the portal user, would typically be a user's
        self.internal_user_partner = self.env['res.partner'].create({'name': 'I'})

        self.document = self.env['test_access_right.ticket'].create({
            'name': 'Need help here',
            'message_partner_ids': [(6, 0, [self.portal_user.partner_id.id,
                                            self.internal_user_partner.id])],
        })

    def test_check_access(self):
        """Typically, a document consulted by a portal user P
           will point to other records that P cannot read.
           For example, if P wants to consult a ticket of his,
           the ticket will have a reviewer or assigned user that is internal,
           and which partner cannot be read by P.
           This should not block P from accessing the ticket.
        """
        document = self.document.with_user(self.portal_user)
        # at this point, some fields might already be loaded in cache.
        # if so, it means we would bypass the ACL when trying to read the field
        # while this is bad, this is not the object of this test
        self.internal_user_partner.invalidate_cache(fnames=['active'])
        # from portal's _document_check_access:
        document.check_access_rights('read')
        document.check_access_rule('read')
        # no raise, because we are supposed to be able to read our ticket

    def test_name_search_with_sudo(self):
        """Check that _name_search return correct values with sudo
        """
        no_access_user = self.env['res.users'].create({
            'login': 'no_access',
            'name': 'no_access',
            'groups_id': [(5, 0)],
        })
        document = self.env['test_access_right.ticket'].with_user(no_access_user)
        res = document.sudo().name_search('Need help here')
        #Invalide cache in case the name is already there
        #and will not trigget check_access_rights when
        #the name_get will access the name
        self.document.invalidate_cache(fnames=['name'])
        self.assertEqual(res[0][1], "Need help here")
