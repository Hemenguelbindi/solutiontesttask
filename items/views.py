import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render

from items.models import Item


def get_session_id(request, id):
    item = Item.objects.get(pk=id)
    stripe.api_key = settings.STRIPE_SECRET_KEY

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name,
                    'description': item.description,
                },
                'unit_amount': int(item.price * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://localhost:8000/success.html',
        cancel_url='http://localhost:8000/cancel.html',
    )

    return JsonResponse({'session_id': session.id})


def item_detail(request, id):
    item = Item.objects.get(id=id)
    context = {'item': item}
    return render(request, 'item_detail.html', context)