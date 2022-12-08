import logging

from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import Sum, F

from cart.cart import Cart
from booking.models import Rooms, Order
from cart.forms import CartAddProductForm
from booking.forms import OrderForm, RoomsFiltersForm

logger = logging.getLogger(__name__)


def prod_list(request):
    prod = Rooms.objects.all()

    filters_form = RoomsFiltersForm(request.GET)

    if filters_form.is_valid():
        cost__gt = filters_form.cleaned_data["cost__gt"]
        if cost__gt:
            prod = prod.filter(cost__gt=cost__gt)

        cost__lt = filters_form.cleaned_data["cost__lt"]
        if cost__lt:
            prod = prod.filter(cost__lt=cost__lt)

        order_by = filters_form.cleaned_data["order_by"]
        if order_by:
            if order_by == "cost_asc":
                prod = prod.order_by("cost")
            if order_by == "cost_desc":
                prod = prod.order_by("-cost")
            if order_by == "max_price":
                prod = prod.annotate(
                    total_cost=Sum("rooms__count") * F("cost")
                ).order_by("-total_cost")

    return render(request, "booking/list.html",
                  {"products": prod, "filters_form": filters_form})


def product_details_view(request, product_id):
    product = get_object_or_404(Rooms, id=product_id)
    product_cart_form = CartAddProductForm()
    return render(request, "booking/details.html",
                  {"product": product, 'product_cart_form': product_cart_form})


def order_list(request):
    cart = Cart(request)
    if request.user.is_authenticated:
        if request.method == "POST":
            form = OrderForm(request.POST)
            if form.is_valid():
                order = []
                logger.info(form.cleaned_data)
                for item in cart:
                    ordr = Order.objects.create(purchase=item['product'],
                                                cost=item['cost'],
                                                count=item['quantity'],
                                                user=request.user,
                                                first_name=form.cleaned_data['first_name'],
                                                last_name=form.cleaned_data['last_name'],
                                                email=form.cleaned_data['email'],
                                                date_come=form.cleaned_data['date_come'],
                                                date_out=form.cleaned_data['date_out'])
                    ordr.save()
                    order.append(ordr)
                cart.clear()
                return render(request, 'booking/order_created.html',
                              {'order': order})
        else:
            form = OrderForm()
    else:
        return redirect('/login/', )
    return render(request, 'booking/order_create.html',
                  {'cart': cart, 'form': form})


def history_list(request):
    if request.user.is_authenticated:
        product = Rooms.objects.all()
        order = Order.objects.filter(user=request.user)
        return render(request, "booking/history.html", {"order": order, "product": product})
    else:
        return redirect('/login/', )

