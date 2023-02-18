import stripe
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import Items

stripe.api_key = settings.STRIPE_SECRET_KEY

class CreateCheckoutSessionView(View):

    def post(self, request, *args, **kwargs):
        DOMEN = "http://localhost:8080"
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': '{{PRICE_ID}}',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=DOMAIN + '/success/',
            cancel_url=DOMAIN + '/cancel/',
        )
        return JsonResponse({'id': checkout_session.id})


class ItemView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'Тут товар')

    

class ListView(View):
    def get(self, request, *args, **kwargs):
        items = Items.objects.all()
        return render(request, 'list.html', {'items': items})