# -*- coding: utf-8 -*-

from openerp.tests.common import TransactionCase
from openerp.tools.float_utils import float_compare
import logging

_logger = logging.getLogger(__name__)

class testModelDietfacts(TransactionCase):
        
    def test_calories_include(self):
    
        record = self.env['product.template'].create({'name':'Danasco',
                                                      'calories':3.6})
        self.assertEqual(record.name,'Danasco', 'Nome esta diferente')
        assert float_compare(record.calories, 3.5,2,0), "Numero esta invalido!"
        
        _logger.info("Test Calories OK!")


    def test_name_valid(self):
        countErr = 0
        charaInv=['.',',','/','\\','\|','+','=','-','(',')']
        record = self.env['product.template'].create({'name':'Diogo',
                                                      'calories':3.6})
        for item in charaInv:
            if(item in record.name):
                countErr = countErr + 1        
        
        self.assertEqual(countErr,0 , 'Nome possui caracteres especiais')       
        _logger.info("Test Name Valid OK!")








'''    def __init__(self):
        self.test_calories_include()

if __name__ == '__main__':
    testDietFacts = testModelDietfacts()
 '''
    

