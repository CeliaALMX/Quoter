# -*- coding: utf-8 -*-
# from odoo import http


# class AlmxQuoter(http.Controller):
#     @http.route('/almx_quoter/almx_quoter', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/almx_quoter/almx_quoter/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('almx_quoter.listing', {
#             'root': '/almx_quoter/almx_quoter',
#             'objects': http.request.env['almx_quoter.almx_quoter'].search([]),
#         })

#     @http.route('/almx_quoter/almx_quoter/objects/<model("almx_quoter.almx_quoter"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('almx_quoter.object', {
#             'object': obj
#         })
