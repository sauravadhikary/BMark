from django.shortcuts import render, HttpResponse
from datetime import datetime

# Create your views here.
def index(request):
    initialTime1 = datetime.now()
    test = "Benchmarking the Web Servers"
    # for i in range(10000):
    #     if len(test) < 200000000:
    #         test += test
    #     else:
    #         test = test[0:len(test)// 2]  # if the string gets too long just cut it
    finalTime1 = datetime.now()
    timeDiffrence1 = finalTime1 - initialTime1
    return HttpResponse(f"The Process took {timeDiffrence1}")