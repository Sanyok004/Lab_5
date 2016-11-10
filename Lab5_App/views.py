from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


data = {'orders': []}
for i in range(1, 10):
    data['orders'].append(
        {
            'id': i,
            'title': '{0}{1}'.format('Заказ №', i),
            'description': 'Краткое описание заказа (может быть довольно длинным, что даже не поместится на одной строке)',
            'text': 'Подробное описание заказа',
            'date': '10.11.2016'
        }
    )


class OrdersView(View):
    def get(self, request):
        return render(request, 'orders.html', data)


class OrderView(View):
    def get(self, request, id):
        data_order = {
            'order': data['orders'][int(id)-1]
        }
        return render(request, 'order.html', data_order)
