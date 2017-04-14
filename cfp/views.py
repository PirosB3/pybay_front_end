from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

from cfp.forms import ProposalForm


def proposal_create(request):
    if request.method == 'GET':
        return render(request, 'cfp.html', {
            'form': ProposalForm()
        })

    elif request.method == 'POST':
        form = ProposalForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'cfp.html', {
                'form': form
            })

        model = form.save()
        messages.add_message(request, messages.INFO,
                             "Thank you {}, Your Talk '{}' was submitted correctly. We will let you know on XXX".format(
                             model.first_name, model.talk_title))
        return redirect(reverse('cfp') + "#form-container")

    else:
        return redirect('home')
