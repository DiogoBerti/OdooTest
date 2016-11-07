# -*- coding: utf-8 -*-

from openerp.tests.common import SingleTransactionCase
import logging

_logger = logging.getLogger(__name__)

class testModelDietFactsSingle(SingleTransactionCase):
    
    def test_the_test(self):
		
        listRecordTest = []        

        record_test = self.env['product.template'].create({'name':'DONTSTARVE',
                                                           'calories':1,
                                                           'totalfat':3,
                                                           'serving_size':'A plate'})
        
        record_test2 = self.env['product.template'].create({'name':'Diogo',
                                                      'calories':1,
                                                      'totalfat':4,
                                                      'serving_size':'Kg'})
        
        
        record_test_ver = self.env['product.template'].search([('name','=','Diogo')])
        
        listRecordTest.append(record_test)
        listRecordTest.append(record_test2)
        listRecordTest.append(record_test_ver)

        assert record_test.name.isupper(),"Nome nao esta conforme as regras"
		
        for recordTest in listRecordTest:
		    assert recordTest.serving_size == "A plate" or recordTest.serving_size == "Kg" , "Serving Size is wrong."

        assert record_test_ver.calories == record_test.calories , "a quantidade de calorias de %s nao eh igual a quantidade de calorias de %s" % (record_test_ver.name, record_test.name)
        _logger.info("Test the Test OK!")
        
        
