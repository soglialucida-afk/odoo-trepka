# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class TrepkaMaserkaController(http.Controller):

    @http.route('/', type='http', auth='public', website=True)
    def homepage(self, **kwargs):
        return request.render('trepka_maserka.trepka_homepage', {})
