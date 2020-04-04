from django.contrib import admin
from quora.models import Answer, Question, Upvote
# Register your models here.
admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(Upvote)
