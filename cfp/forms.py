from django import forms
from .models import Proposal


class ProposalForm(forms.ModelForm):
    class Meta:
        model = Proposal
        fields = [
            'first_name', 'last_name', 'email', 'profile_link',
            'phone', 'monthly_talk', 'category', 'speaker_bio',
            'talk_title', 'audience_level', 'description', 'abstract',
            'outcomes', 'talk_history', 'file_submission', 'prior_talks'
        ]
