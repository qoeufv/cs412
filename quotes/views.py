# file: quotes/views.py

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

import random

# Keep quotes and images as separate lists; use the same index to keep them aligned.
QUOTES = [
    "Imagination is more important than knowledge.",
    "Life is like riding a bicycle. To keep your balance, you must keep moving.",
    "The important thing is not to stop questioning. Curiosity has its own reason for existing.",
]
IMAGES = [
    "https://upload.wikimedia.org/wikipedia/commons/9/90/Albert_Einstein_1921_%28cropped%29.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/2/2f/Albert_Einstein_%28Nobel%29.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/a/a7/Albert_Einstein%2C_1921%2C_SFA002010156.jpg",
]

def quote(request):
    '''Define a view to show the 'home.html' template.'''

    template_name = 'quotes/quote.html'
    # choose a matching quote/image by shared index
    idx = random.randrange(len(QUOTES))
    context = {
        "q": QUOTES[idx], 
        "i": IMAGES[idx]
    }
    return render(request, template_name, context)

def show_all(request):
    template_name = 'quotes/show_all.html'
    context = {
        "items": [(QUOTES[i], IMAGES[i]) for i in range(len(QUOTES))],
    }
    return render(request, template_name, context)


def about(request):
    template_name = 'quotes/about.html'
    context = {
        "name": "Albert Einstein",
        "lifespan": "1879-1955",
        "bio": (
            "Theoretical physicist whose 1905 papers reshaped modern physics, "
            "best known for special relativity, E = mc², and the photoelectric effect."
        ),
        "highlights": [
            "Nobel Prize in Physics (1921) for the photoelectric effect",
            "Developed the theories of special and general relativity",
            "Proposed the concept of light quanta (photons)",
            "Influenced cosmology with work on gravitational waves and the cosmological constant",
        ],
        "image": IMAGES[0],
        "more_link": "https://en.wikipedia.org/wiki/Albert_Einstein",
        "quote_count": len(QUOTES),
    }
    return render(request, template_name, context)
