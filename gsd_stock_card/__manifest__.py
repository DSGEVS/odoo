# -*- coding: utf-8 -*-
{
    'name': "Stock card report",

    'summary': """
               Enables stock card by product  in inventory reports
               """,

    'description': """
        You can get reports of inputs, outputs and stock balances by product and location. 
    """,

    'author': "GSD Devs",
    'category': 'Warehouse',
    'version': '13.0.1',
    'license': 'AGPL-3',

    # any module necessary for this one to work correctly

    'depends': ['base', 'stock','report_xlsx'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'report/stock_card_report.xml',
        'wizard/stock_card_wizard.xml',
    ],
    'images': ['static/description/banner.png'],
    'price': 12,
    'currency': 'EUR',
}
