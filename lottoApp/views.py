from django.shortcuts import render
import random

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
    
from django.shortcuts import render
import random
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
    
def result(request):

    input_lotto = request.GET['fulltext']

    input_num = input_lotto.split()
    input_num = list(map(int, input_num))
    correct_lotto = []

    lotto = []
    num = 0

    while True:
        num = random.randrange(1,46)
        while num in lotto:
            num = random.randrange(1,46)
        lotto.append(num)
        if len(lotto) >= 6:
            break

    lotto.sort()

    for i in lotto:
        if i in input_num:
            correct_lotto.append(i)

    
    return render(request, 'result.html', {'full':input_num,'correct':correct_lotto, 'answer':lotto, 'count': len(correct_lotto)}) 
