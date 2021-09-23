# -*- coding: utf-8 -*-
{
    'name': "Add BoM in sale order line",

    'summary': """
        Select BOM in your sale order and list the components in your quotation 
        """,

    'description': """
        Add BOM to Sale order line and show its components in description field and quotation. Also you can view the Sale order in your Manufacture order
    """,

    'author': "GSD Devs",
    'category': 'Sales',
    'version': '14.0.1',
    'license': 'AGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management', 'mrp'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/sale_order.xml',
    ],
    # only loaded in demonstration mode
    'images': ['static/description/banner.jpg'],
    'price': 20,
    'currency': 'EUR',
}
