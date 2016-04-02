from django.utils.translation import ugettext_lazy as _

from mezzanine.conf import register_setting


register_setting(
    name="SOCIAL_LINK_FACEBOOK",
    label=_("Facebook link"),
    description=_("If present a Facebook icon linking here will be in the "
        "header."),
    editable=True,
    default="https://facebook.com/mezzatheme",
)

register_setting(
    name="SOCIAL_LINK_TWITTER",
    label=_("Twitter link"),
    description=_("If present a Twitter icon linking here will be in the "
        "header."),
    editable=True,
    default="https://twitter.com/mezzatheme",
)

register_setting(
    name="SOCIAL_LINK_LINKEDIN",
    label=_("LinkedIn link"),
    description=_("If present a LinkedIn link will show in the header."),
    editable=True,
    default="https://gr.linkedin.com/in/mmilonakis",
)

register_setting(
    name="ADDRESS",
    label=_("Map Address"),
    description=_("If present a map will be shown on the contact page with this address"),
    editable=True,
    default="Bakersfield, CA 93309",
)

register_setting(
    name="TEMPLATE_ACCESSIBLE_SETTINGS",
    append=True,
    default=("SOCIAL_LINK_FACEBOOK",
             "SOCIAL_LINK_TWITTER",
             "SOCIAL_LINK_LINKEDIN",
             "ADDRESS"),
)
