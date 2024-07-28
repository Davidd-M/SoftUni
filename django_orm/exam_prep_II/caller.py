import os
from decimal import Decimal

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


def get_top_products() -> str:
    products = (Product.objects.annotate(quantity_sold=Count('order'))
                .filter(quantity_sold__gt=0)
                .order_by('-quantity_sold', 'name'))[:5]

    if not products.exists():
        return ''

    return (f"Top products:\n" +
            '\n'.join(f"{p.name}, sold {p.quantity_sold} times" for p in products))


def apply_discounts() -> str:
    orders = (Order.objects.annotate(products_count=Count('products'))
              .filter(is_completed=False, products_count__gt=2)
              .update(total_price=F('total_price')*0.9))

    return f"Discount applied to {orders} orders."


def complete_order() -> str:
    oldest_order = Order.objects.filter(is_completed=False).order_by('creation_date').first()

    if not oldest_order:
        return ''

    products = oldest_order.products.all()

    for p in products:
        p.in_stock -= 1

        if p.in_stock <= 0:
            p.is_available = False
            p.in_stock = 0

        p.save()

    '''
    order.products.update(
        in_stock=F('in_stock') - 1,
        is_available=Case(
            When(in_stock=1, then=Value(False)),
            default=F('is_available'),
            output_field=BooleanField()            
        )
    )
    '''

    oldest_order.is_completed = True
    oldest_order.save()

    return "Order has been completed!"

