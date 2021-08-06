from django.test import TestCase

from ..models import SalesBranch, SalesManager


class SalesBranchTests(TestCase):
    def setUp(self):
        self.short_name = "WRO"
        self.full_name = "Wrocław"
        return super().setUp()

    def test_employee_creation(self):
        new_sales_branch = SalesBranch.objects.create(
            short_name="WRO", full_name="Wrocław"
        )
        len_list = SalesBranch.objects.all()

        self.assertEqual(new_sales_branch.short_name, self.short_name)
        self.assertEqual(new_sales_branch.full_name, self.full_name)
        self.assertEqual(len(len_list), 1)


class SalesManagerTests(TestCase):
    def setUp(self):
        self.first_name = "Marcin"
        self.last_name = "Opania"
        self.sales_branch = "WRO"
        self.area = "Area51"
        self.position = "Sprzedawca"
        self.supervisor = "508122255"
        self.phone_number = "691200122"
        self.email = "test@test.pl"
        self.id_number = 811290
        self.is_active = True

    def test_sales_manager_creation(self):
        new_sales_branch = SalesBranch.objects.create(
            short_name="WRO", full_name="Wrocław"
        )
        new_sales_manager = SalesManager.objects.create(
            first_name="Marcin",
            last_name="Opania",
            sales_branch=new_sales_branch,
            area="Area51",
            position="Sprzedawca",
            supervisor="508122255",
            phone_number="691200122",
            email="test@test.pl",
            id_number=811290,
            is_active=True,
        )
        len_list = SalesManager.objects.all()

        self.assertEqual(new_sales_manager.first_name, self.first_name)
        self.assertEqual(new_sales_manager.last_name, self.last_name)
        self.assertEqual(new_sales_manager.sales_branch.short_name, self.sales_branch)
        self.assertEqual(new_sales_manager.area, self.area)
        self.assertEqual(new_sales_manager.position, self.position)
        self.assertEqual(new_sales_manager.supervisor, self.supervisor)
        self.assertEqual(new_sales_manager.phone_number, self.phone_number)
        self.assertEqual(new_sales_manager.email, self.email)
        self.assertEqual(new_sales_manager.id_number, self.id_number)
        self.assertEqual(new_sales_manager.is_active, self.is_active)
        self.assertEqual(len(len_list), 1)
