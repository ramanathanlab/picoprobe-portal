import os

from django.apps import AppConfig

from picoprobe_portal import fields

APP_DIR = os.path.join(os.path.dirname(__file__))


class PicoProbeIndexConfig(AppConfig):
    name = "picoprobe_portal"


SEARCH_INDEXES = {
    "picoprobe": {
        "uuid": "5e2dd679-6e3f-4b4d-b255-87ccc326aea7",
        # "uuid": "6077d057-989d-41e2-b60b-91fe001f0687",
        "name": "PicoProbe Index",
        "group": "a695bbc6-3ad2-11ee-88ba-27cb577dbd96",
        "collection": "300ef593-e55e-4bc1-ab21-6d26d82c3b99",
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
