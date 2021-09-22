# -*- coding: utf-8 -*-
{
    'name': "gsd_operations_stock_available",
    'summary': """
        Adds new field in Sale Order Line, Purchase Order Line and Transfer Stock Line to grab the stock.
        """,
    'description': """
    """,
    'author': "GSD intelligence - David Lizarraga Corne",
    'category': 'Warehouse',
    'license': 'AGPL-3',
    'version': '14.0.1',
    # any module necessary for this one to work correctly
    'depends': [
        'purchase',
        'sale_management',
        'stock',
    ],
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/purchase_order_stock.xml',
        'views/sale_order_stock.xml',
        'views/stock_picking.xml'
    ],
    'images': ['static/description/banner.png'],
    'price': 8,
    'currency': 'USD',
}