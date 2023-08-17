import os

from django.apps import AppConfig

from picoprobe_portal import fields

APP_DIR = os.path.join(os.path.dirname(__file__))


class PicoProbeIndexConfig(AppConfig):
    name = "picoprobe_portal"


SEARCH_INDEXES = {
    "picoprobe": {
        "uuid": "6077d057-989d-41e2-b60b-91fe001f0687",
        "name": "PicoProbe Index",
        "group": "dda56f31-53d1-11ed-bd8b-0db7472df7d6",
        "collection": "d8e16504-eaab-44b6-aa56-ff7d1b6040a3",
        "base_templates": "globus-portal-framework/v2/",
        "template_override_dir": "picoprobe",
        "tabbed_project": False,
        "access": "private",
        "description": ("PicoProbe portal"),
        "fields": [
            ("title", fields.title),
            "dc",
            "files",
            ("display_image", fields.display_image),
        ],
        "facets": [
            {
                "name": "Dates",
                "field_name": "dc.dates.date",
                "type": "date_histogram",
                "date_interval": "day",
            }
        ],
        "facet_modifiers": [],
        "sort": [{"field_name": "dc.dates.date", "order": "desc"}],
        "default_filters": [
            {
                "type": "match_all",
                "field_name": "result.exp_type",
                "values": [],
            }
        ],
    }
}
