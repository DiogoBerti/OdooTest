# -*- coding: utf-8 -*-
#Dietfacts Application

from openerp import models, fields, api

#extendendo o modelo product.template com o campo calories

class Dietfacts_product_template(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    calories = fields.Integer("Calories")
    totalfat = fields.Float("Total Fat")
    serving_size = fields.Char("Serving Size")
    #field_test_function = fields.Float("Teste", readonly=True)
    
    '''@api.multi
    def calculate_test_field(self):
        self.ensure_one()
        #newvalue = float(self.calories) + self.totalfat
        #self.field_test_function = 0.5
        self.write({'field_test_function':0.5})
    '''
    
