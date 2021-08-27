from django.contrib import admin
from . models import Question,Choice

class ChoiceInlineStacked(admin.StackedInline):
    model = Choice
    extra = 4


class ChoiceInlineTabular(admin.TabularInline):
    model = Choice
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    # fields = ["pub_date", "question_text"]
    fieldsets = [
        ("Question", {"fields":["question_text"]}),
        ("Date information", {"fields":["pub_date"]})
        ]
    inlines = [ChoiceInlineTabular]

    list_display = ("question_text", "pub_date", "active", "was_published_recently")

    list_filter = ["pub_date"]

    search_fields = ["question_text"]

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
