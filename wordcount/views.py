from django.shortcuts import render
from django.http import HttpResponse
import operator
# Create your views here.

def homepage(request):
    return render(request,'/home/machinelearning101/Desktop/Project1/templates/home.html',{'name' : 'Hi there Rishikesh'})

def contact(request):
    return HttpResponse('<h1>Contact-Us</h1><br>This is our contact page</br>')

def count(request):


    data = request.GET["smalltextarea"]

    print(data)
    word_list = data.split()
    print(word_list)
    list_len = len(word_list)
    print(list_len)

    wordDictionary = {}

    for word in word_list:

        if word in wordDictionary:

            # increase by 01
            wordDictionary[word] += 1

        else:
            #add to the dictionary
            wordDictionary[word] = 1
    sorted_list = sorted(wordDictionary.items(), key=operator.itemgetter(1),reverse=True)
    return render(request,'/home/machinelearning101/Desktop/Project1/templates/count.html', {'fulltext':data,"words":list_len , 'word_dict':sorted_list})





