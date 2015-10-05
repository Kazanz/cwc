from django.contrib import messages
from django.shortcuts import render, redirect

from codewithchrist.forms import SignUpForm

from ratelimit.decorators import ratelimit


def landing(request):
    context = {}
    return render(request, 'index.html', context)


@ratelimit(key='ip', rate='10/h')
def sign_up_form(request):
    form = SignUpForm(request.POST or None)
    if getattr(request, 'limited', False):
        messages.error(request, "You have been doing that too much.")
    else:
        if form.is_valid():
            form.save()
            msg = "Thank you for signing up!  \
                We will be sending you information on how to prepare for class."
            messages.success(request, msg)
            return redirect('landing')
    context = {
        'form': form,
    }
    return render(request, 'landing.html', context)
