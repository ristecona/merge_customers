# -*- coding: utf-8 -*-
from odoo import http

# class SimplifyMergeCustomers(http.Controller):
#     @http.route('/simplify_merge_customers/simplify_merge_customers/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/simplify_merge_customers/simplify_merge_customers/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('simplify_merge_customers.listing', {
#             'root': '/simplify_merge_customers/simplify_merge_customers',
#             'objects': http.request.env['simplify_merge_customers.simplify_merge_customers'].search([]),
#         })

#     @http.route('/simplify_merge_customers/simplify_merge_customers/objects/<model("simplify_merge_customers.simplify_merge_customers"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('simplify_merge_customers.object', {
#             'object': obj
#         })