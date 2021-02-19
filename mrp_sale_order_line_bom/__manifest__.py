# -*- coding: utf-8 -*-
{
    'name': 'Select BOM in sale order line',

    'summary': """
       Choose your BOM in the sale order line and get all the bom for description. 
       """,

    'description': """
         This app allow you to create manufacturing order from a sale order, also you can to choose, creating or editing your BOM from a sale order line. 
        The order line description can be the product's name and BOM if you activate the option.
    """,

    'author': "GSD intelligence - David Lizarraga Corne",
    'website': "http://www.tecniases.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Manufacturing',
    'version': '11.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base_setup', 'sale_management'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/sale_order.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}