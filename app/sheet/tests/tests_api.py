from ..models import SalesBranch, SalesManager

from django.test import TestCase, Client
from django.urls import reverse


class EndPointTest(TestCase):
    def setUp(self):
        self.c = Client(HTTP_USER_AGENT="Mozilla/5.0")
        self.new_sales_branch = SalesBranch.objects.create(
            short_name="WRO", full_name="Wrocław"
        )
        self.new_sales_manager = SalesManager.objects.create(
            first_name="Marcin",
            last_name="Opania",
            sales_branch=self.new_sales_branch,
            area="Area51",
            position="Sprzedawca",
            supervisor="508122255",
            phone_number="691200122",
            email="test@test.pl",
            id_number=811290,
            is_active=True,
        )


    def test_all_traders_adress(self):
        all_traders_response = self.c.get("/sheet/all-traders/")
        self.assertEqual(all_traders_response.status_code, 200)

        all_traders_list = all_traders_response.context["test"]
        self.assertEqual(len(all_traders_list), 1)

        specific_trader = all_traders_list[0]
        self.assertEqual(specific_trader.last_name, "Opania")


    def test_specific_trader_adress(self):
        specific_trader_response = self.c.get(
            f"/sheet/submit/{self.new_sales_manager.id_number}/"
        )
        self.assertEqual(specific_trader_response.status_code, 200)

        specific_trader_list = specific_trader_response.context["test"]
        specific_trader = specific_trader_list[0]
        self.assertEqual(specific_trader.last_name, "Opania")


    def test_add_sales_manager(self):
        add_sales_manager = self.c.post(
            "/sheet/add-sales-manager/",
            data={
                "first_name": "Adam",
                "last_name": "Kowalski",
                "area": "Grochow",
                "sales_branch": [self.new_sales_branch],
                "position": "Sprzedawca",
                "supervisor": "510233945",
                "phone_number": "510233941",
                "email": "test@test.pl",
                "is_active": True,
            },
        )
        self.assertEqual(add_sales_manager.status_code, 200)
        test_form = add_sales_manager.context["form"]
        test_data = test_form.data

        self.assertEqual(test_data.get("first_name"), "Adam")
        self.assertEqual(test_data.get("sales_branch"), "WRO")
        self.assertEqual(test_data.get("is_active"), "True")
