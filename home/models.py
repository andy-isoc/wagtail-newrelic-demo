from django.db import models
from wagtail.contrib.routable_page.models import RoutablePageMixin, re_path
from wagtail.fields import RichTextField

from wagtail.models import Page


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + ["body"]


class GenericTransactionNamePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + ["body"]

    class Meta:
        verbose_name = "Page with generic transaction name"

    def __str__(self):
        return "Page with generic transaction name"


class AutoDetectedTransactionNamePage(RoutablePageMixin, Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + ["body"]

    @re_path(r"^routable")
    def index(self, request):
        # Handle URLs of the form /<id>
        return super().serve(request)

    class Meta:
        verbose_name = "Page with auto-detected transaction name"

    def __str__(self):
        return "Page with auto-detected transaction name"
