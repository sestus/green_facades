from django.contrib import admin

from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin

from theme.models import (HomePage, Slide, IconBlurb,
                    Portfolio, PortfolioItem, PortfolioItemCategory,
                    PortfolioItemImage)


class SlideInline(TabularDynamicInlineAdmin):
    model = Slide


class IconInline(TabularDynamicInlineAdmin):
    model = IconBlurb


class HomePageAdmin(PageAdmin):
    inlines = (SlideInline, IconInline)


admin.site.register(HomePage, HomePageAdmin)
admin.site.register(Portfolio, PageAdmin)


class PortfolioItemImageInline(TabularDynamicInlineAdmin):
    model = PortfolioItemImage


class PortfolioItemAdmin(PageAdmin):
    inlines = (PortfolioItemImageInline,)

admin.site.register(PortfolioItem, PortfolioItemAdmin)
admin.site.register(PortfolioItemCategory)
