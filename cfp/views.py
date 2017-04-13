from cfp.forms import ProposalForm
from django.shortcuts import render


def proposal_create(request):
    if request.method == 'GET':
        form = ProposalForm()
    elif request.method == 'POST':
        import ipdb; ipdb.set_trace()

    return render(request, 'cfp.html', {
        'form': form
    })
