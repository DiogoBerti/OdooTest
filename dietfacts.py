# -*- coding: utf-8 -*-
#Dietfacts Application

from openerp import models, fields 

#extendendo o modelo product.template com o campo calories

class Dietfacts_product_template(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    calories = fields.Integer("Calories")
    totalfat = fields.Float("Total Fat")
    serving_size = fields.Char("Serving Size")
    
    
    
    