from django.db import models


class Proposal(models.Model):
    first_name = models.CharField(verbose_name="First Name", max_length=50)
    last_name = models.CharField(verbose_name="Last Name", max_length=50)
    email = models.EmailField(verbose_name="Email Adress", max_length=50)
    profile_link = models.URLField(verbose_name="GitHub/Home Page", max_length=50, blank=True)
    phone = models.CharField(verbose_name="Phone Number", max_length=12)
    monthly_talk = models.BooleanField(verbose_name="Interest in monthly talk?", max_length=50)
    category = models.IntegerField(choices=
        [(1, 'Fundamentals'),
         (2, 'Language Internals'),
         (3, 'All things Web'),
         (4, 'Dealing with Data'),
         (5, 'Security'),
         (6, 'Performant Python'),
         (7, 'Scalable Python'),
         (8, '/etc')])
    speaker_bio = models.TextField(verbose_name="Speaker Bio", max_length=500)
    talk_title = models.TextField(verbose_name="Talk Title", max_length=200)
    audience_level = models.IntegerField(choices=
        [(1, 'Beginner'),
         (2, 'Intermediate'),
         (3, 'Advanced')            
        ])
    description = models.TextField(max_length=500)
    abstract = models.TextField(max_length=1500)
    outcomes = models.TextField(verbose_name="Learning Outcomes", max_length=250)
    talk_history = models.TextField(verbose_name="Speaker and Talk History", max_length=250)
    file_submission = models.FileField(blank=True, null=True)
    prior_talks = models.URLField(verbose_name="Links to previous talks", max_length=50, blank=True)
        
    
    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
