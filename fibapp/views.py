from django.shortcuts import render
from django.http import HttpResponse
import time


def index(request):
    if request.method == 'POST':
        number_count = int(request.POST.get('number_count'))

        if number_count > 0:
            start = time.clock()

            fib_list = []
            a, b = 1, 1
            for i in range(number_count - 1):
                a, b = b, a + b
                fib_list.append(a)

            end = time.clock()

            time_taken = end - start

            results = {'fib_list': fib_list,
                       'time_taken': time_taken}

            return render(request, 'fibapp/index.html', {'data':
                                                         results})
        else:
            error = "Please Enter a Possitve Number"
            return render(request, 'fibapp/index.html', {'error': error})

    return render(request, 'fibapp/index.html', {})
