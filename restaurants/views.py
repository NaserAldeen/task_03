from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {

    "my_list": [
    {"restaurant_name": "KFC", "food_type": "Fast food" },
    {"restaurant_name": "McDonald's", "food_type": "Better fast food" },
    {"restaurant_name": "Hardees", "food_type": "Not so good fast food" },

    ],

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
        "my_object":{
            "restaurant_name": "KFC",
            "food_type": "Fast food",
        }
    }
    return render(request, 'detail.html', context)
