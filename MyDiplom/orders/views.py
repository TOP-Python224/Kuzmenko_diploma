from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from orders.forms import OrderForm
from orders.models import Order
from django.shortcuts import render


class SuccessView(TemplateView):
    template_name = 'success.html'


class OrderCreateView(CreateView):
    template_name = 'order-create.html'
    form_class = OrderForm
    success_url = reverse_lazy('orders:payment')

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super(OrderCreateView, self).form_valid(form)


class OrderListView(ListView):
    template_name = 'orders.html'
    queryset = Order.objects.all()
    ordering = ('-created')

    def get_queryset(self):
        queryset = super(OrderListView, self).get_queryset()
        return queryset.filter(initiator=self.request.user)


class OrderDetailView(DetailView):
    template_name = 'order.html'
    model = Order


def full_fill_order(request):
    orders = Order.objects.get_or_create(initiator=request.user, status=0)
    orders[0].update_after_payment()
    return render(request, 'payment.html')
