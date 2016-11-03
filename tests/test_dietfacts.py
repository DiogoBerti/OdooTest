# -*- coding: utf-8 -*-

from openerp.tests.common import TransactionCase
import logging

_logger = logging.getLogger(__name__)

class testModelDietfacts(TransactionCase):
        
    def test_calories_include(self):
    
        record = self.env['product.template'].create({'name':'Voiture',
                                                      'calories':3.6})
        
        self.assertEqual(record.name,'Voiture', 'Nome esta diferente')
        
        #self.assertEqual(record.calories,3.6)
        
        _logger.info("Test Calories OK!")


    def test_name_valid(self):
        countErr = 0
        charaInv=['.',',','/','\\','\|','+','=','-','(',')']
        
        record = self.env['product.template'].create({'name':'Voiture',
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
    

