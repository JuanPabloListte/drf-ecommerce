from tests.test_setup import TestSetUp
from tests.factories.expense_manager.expense_factories import SupplierFactory
from rest_framework import status
from apps.expense_manager.models import Supplier

class ExpenseTestCase(TestSetUp):
    
    url = '/expense/expense/'
    
    def test_search_supplier(self):
        supplier = SupplierFactory().create_supplier()
        response = self.client.get(
            self.url + 'search_supplier/',
            {
                'cuil_or_business_name': supplier.cuil
            },
            format='json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['cuil'], supplier.cuil)
        
    def test_search_supplier_error(self):
        supplier = SupplierFactory().create_supplier()
        response = self.client.get(
            self.url + 'search_supplier/',
            {
                'cuil_or_business_name': '412310411'
            },
            format='json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotEqual(supplier.cuil, '412310411')
        self.assertEqual(response.data['mensaje'], 'Supplier not found.')
        
        
    def test_new_supplier(self):
        supplier = SupplierFactory().build_supplier_JSON()
        response = self.client.post(
            self.url + 'new_supplier/',
            supplier,
            format='json'
        )
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Supplier.objects.all().count(), 1)
        self.assertEqual(response.data['supplier']['cuil'], supplier['cuil'])