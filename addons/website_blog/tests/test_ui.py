# -*- coding: utf-8 -*-
# Part of etwork. See LICENSE file for full copyright and licensing details.

import etwork.tests


@etwork.tests.tagged('post_install', '-at_install')
class TestUi(etwork.tests.HttpCase):
    def test_admin(self):
        # Ensure at least two blogs exist for the step asking to select a blog
        self.env['blog.blog'].create({'name': 'Travel'})

        # Ensure at least one image exists for the step that chooses one
        self.env['ir.attachment'].create({
            'public': True,
            'type': 'url',
            'url': '/web/image/123/transparent.png',
            'name': 'transparent.png',
            'mimetype': 'image/png',
        })

        self.start_tour("/", 'blog', login='admin')
