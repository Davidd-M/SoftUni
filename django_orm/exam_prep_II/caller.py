import os
import django
from django.db.models import Q, F, Count

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Profile, Order, Product


def get_profiles(search_string=None) -> str:
    if search_string is None:
        return ''

    profiles = Profile.objects.filter(
        Q(full_name__icontains=search_string) |
        Q(email__icontains=search_string) |
        Q(phone_number__icontains=search_string)
    ).order_by('full_name')

    if not profiles.exists():
        return ''

    result = []
    for p in profiles:
        result.append(f"Profile: {p.full_name}, email: {p.email}, "
                      f"phone number: {p.phone_number}, orders: {p.orders.count()}")

    return '\n'.join(result)


def get_loyal_profiles() -> str:
    profiles = Profile.objects.get_regular_customers()

    if not profiles.exists():
        return ''

    return '\n'.join(f"Profile: {p.full_name}, orders: {p.orders_count}" for p in profiles)


def get_last_sold_products() -> str:
    order = Order.objects.last()

    if order is None:
        return ''

    products = order.products.order_by('name').values_list('name', flat=True)

    if not products.exists():
        return ''

    return f"Last sold products: {', '.join(products)}"

