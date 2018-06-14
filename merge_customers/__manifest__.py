# -*- coding: utf-8 -*-
{
    'name': "merge_customers",

    'summary': """
        Select two or more customers and their ORDERS INVOICES AND PURCHASE ORDERS will be moved to the 
        selected customer""",

    'description': """
       Select two or more customers and their ORDERS INVOICES AND PURCHASE ORDERS will be moved to the 
        selected custome
    """,

    'author': "Unknown",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'sales',
    'version': '0.1',
    'price': 79,
    'currency': 'EUR',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','account_invoicing','purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
