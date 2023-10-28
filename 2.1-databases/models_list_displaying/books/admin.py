from django.contrib import admin

from .models import Article, Scope, Tag
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            try:
                if form.cleamed_data["is_main"]:
                    count += 1
            except KeyError:
                pass
        if count > 1:
            raise ValidationError('Основным может быть один ТЕГ')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 3


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]



@admin.register(Tag)
class TagsAdmin(admin.ModelAdmin):
    pass
