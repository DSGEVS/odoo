# -*- coding: utf-8 -*-
{
    'name': "Stock card report",

    'summary': """
               Enables stock card by product  in inventory reports
               """,

    'description': """
        You can get reports of inputs, outputs and stock balances by product and location. 
    """,

    'author': "David Lizarraga",
    'category': 'Warehouse',
    'version': '0.1',
    

    # any module necessary for this one to work correctly

    'depends': ['base', 'stock','report_xlsx'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'report/stock_card_report.xml',
        'wizard/stock_card_wizard.xml',
    ],
    'license': 'GPL-3',
    'price': 12,
    'currency': 'USD', 
    'maintainer': 'David Lizarraga',   
    'support': "David Lizarraga",

}