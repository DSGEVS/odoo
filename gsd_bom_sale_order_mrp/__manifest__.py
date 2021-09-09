# -*- coding: utf-8 -*-
{
    'name': "gsd_bom_sale_order_mrp",

    'summary': """
        Select BOM in your sale order and show the components in your quotation 
        """,

    'description': """
        Add BOM to Sale order line and show its components in description field and quotation. Also you can view the Sale order in your Manufacture order
    """,

    'author': "GSD Intellegence",
    'category': 'Sales',
    'version': '13.0.1',
    'license': 'AGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management', 'mrp'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/sale_order.xml',
        'views/mrp_production.xml',
    ],
    # only loaded in demonstration mode
    'images': ['static/description/banner.PNG'],
    'price': 20,
    'currency': 'EUR',
}



