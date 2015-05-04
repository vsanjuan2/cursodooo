# -*- coding: utf-8 -*-
# OpenERP
import openerp
# Necesario para poder definir nuestro modelo.
from osv import orm, fields
# Utilizaremos el paquete python PDB para debuggear.
import pdb
# Tratando fechas
from datetime import datetime, date
# from datetime import datetime
from tools import DEFAULT_SERVER_DATE_FORMAT as DEF_DATE
from tools import DEFAULT_SERVER_DATETIME_FORMAT as DEF_DATETIME
# Loggers
import logging
_logger = logging.getLogger(__name__)

class budget(orm.Model):
    
    _name = 'budgets.budget'
    
    _description = 'Budget information'
    
    _order = 'budget_no desc'
    
    _log_access = True
    
    _columns = {
        
        'budget_no' : fields.char(
            string = "Budget number",
            size = 128,
            translate = True,
            required = True,
            readonly = True
            
            ),
            
        'name' : fields.char(
            string = 'Title',
            size = 128,
            translate=True,
            required=True
            ),
            
        'description': fields.text(
            string = 'Description',
            translate = True,
            ),
        'budget_date': fields.date('Budget date'),
        'amount': fields.float('Budget amount'),
        'active' : fields.boolean("Active"), 
        'author_id': fields.many2one(
            'res.users',string="Responsible",required=True),
            
        }
        
        
    def create(self, cr, uid, vals, context=None):
        vals['budget_no'] = self.pool.get('ir.sequence').get(cr,uid,'budget_number')
        pdb.set_trace()
        
        return super(budget, self).create(cr,uid,vals,context=context)
        
    #_sql_constraints = [('uniqe_budget_no', 'UNIQUE(budget_no)', 'Budget number must be unique'),]


    # def _check(self, cr, uid, ids, vals, context=None):
    #     if vals['name'] == vals['description']:
    #         raise openerp.exceptions.AccessError("Budget name and description"\
    #         " cannot be equal.")
    
    # _constraints = _check
    
    _defaults = {
        #'budget_no': lambda obj, cr, uid, context:obj.pool.get('ir.sequence').get(cr,uid,'budget_number_type'),
        'active' : True,
        'author_id' : lambda self, cre, uid, context, *a: uid,
        'budget_date': fields.date.today()
        }

budget()
