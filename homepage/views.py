from django.shortcuts import render
from django.db.models import Sum
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, TemplateView
from inventory.models import Stock
from transactions.models import SaleBill, PurchaseBill


class HomeView(View):
    template_name = "home.html"
    def get(self, request):        
        # Agrupa por categoría y suma el stock
        stock_by_category = (
            Stock.objects
            .filter(is_deleted=False)
            .values('category__name')
            .annotate(total=Sum('quantity'))
            .order_by('-total')
        )
        labels = [item['category__name'] for item in stock_by_category]
        data = [item['total'] for item in stock_by_category]

        sales = SaleBill.objects.order_by('-time')[:3]
        purchases = PurchaseBill.objects.order_by('-time')[:3]
        context = {
            'labels': labels,
            'data': data,
            'sales': sales,
            'purchases': purchases
        }
        return render(request, self.template_name, context)

class AboutView(TemplateView):
    template_name = "about.html"