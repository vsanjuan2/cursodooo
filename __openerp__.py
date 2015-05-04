# -*- encoding: utf-8 -*-
{
    'name': 'Project budget',
    'version': '1.0',
    'author': 'Salvador Sanjuán Catalán',
    'category': 'CRM',
    'description': """
Project budget
==============

Budget module to prepare project budgets
----------------------------------------------
- Budget
- Tecnical card
- Date
    """,
    'depends': ['base'],
    'data': [   
                #'views/budget_menu.xml',
                'views/budget_view.xml',],
    'installable':True,
    'active':True,
    'js':[],
    'qweb':[],
    'css':[],
}
