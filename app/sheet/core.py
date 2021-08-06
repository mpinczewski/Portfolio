import random
from .models import SalesManager


def unique_sales_manager_id():
    id_unique = False
    while id_unique == False:
        random_number = random.randint(99999, 999999)
        check_id = SalesManager.objects.filter(id_number=random_number)
        if len(check_id) == 0:
            id_unique = True
            return random_number
