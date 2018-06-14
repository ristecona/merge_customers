# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
import logging
_logger = logging.getLogger('base.customers.merge.automatic.wizard')

class MergeCustomer(models.Model):
    _inherit = 'res.partner'

class MergeTasksLine(models.TransientModel):

    _name = 'base.task.merge.line'
    _order = 'min_id asc'

    wizard_id = fields.Many2one('base.customers.merge.automatic.wizard', 'Wizard')
    min_id = fields.Integer('MinID')
    aggr_ids = fields.Char('Ids', required=True)

class MergeCustomers(models.TransientModel):

    _name = 'base.customers.merge.automatic.wizard'
    _description = 'Merge Customers'

    @api.model
    def default_get(self, fields):
        res = super(MergeCustomers, self).default_get(fields)
        active_ids = self.env.context.get('active_ids')
        if self.env.context.get('active_model') == 'res.partner' and active_ids:
            res['customer_ids'] = active_ids
        return res

    customer_ids = fields.Many2many('res.partner', string='Customers')#'merge_tasks_rel', 'merge_id', 'task_id',)

    dst_customer = fields.Many2one('res.partner', string='Destination Customer')
    @api.multi
    def action_merge(self):

        #write the name of the destination task because it will overwritten
        if not self.dst_customer:
            raise UserError(_("You must select a customer to stay active!"))



        #also write the description of the destination task because it will be overwritten
        for customer in self.customer_ids:
            orders = self.env['sale.order'].search([('partner_id','=',customer.id)])
            if orders:
                for order in orders:
                    order.write({'partner_id' : self.dst_customer.id})
        for customer in self.customer_ids:
            invoices = self.env['account.invoice'].search([('partner_id','=',customer.id)])
            if invoices:
                for invoice in invoices:
                    invoice.write({'partner_id' : self.dst_customer.id})
        for customer in self.customer_ids:
            purchases = self.env['purchase.order'].search([('partner_id','=',customer.id)])
            if purchases:
                for purchase in purchases:
                    purchase.write({'partner_id' : self.dst_customer.id})
            customer.write({'active' : False})
