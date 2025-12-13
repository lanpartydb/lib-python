"""
:Copyright: 2024-2025 Jochen Kupperschmidt
:License: MIT
"""

from textwrap import dedent

from lanpartydb.models import Series, SeriesLinks, Resource
from lanpartydb.serialization import serialize_series_list_to_toml


def test_serialize_series_list_to_toml():
    series_list = [
        Series(
            slug='gammalan',
            title='GammaLAN',
            alternative_titles=[],
            country_codes=['ca', 'us'],
        ),
        Series(
            slug='deltalan',
            title='DeltaLAN',
            alternative_titles=['Δ LAN', 'Δέλτα LAN'],
            country_codes=['au'],
            links=SeriesLinks(
                website=Resource(
                    url='https://www.deltalan.example/',
                ),
            ),
        ),
    ]

    assert serialize_series_list_to_toml(series_list) == dedent("""\
            [[series]]
            slug = "gammalan"
            title = "GammaLAN"
            country_codes = ["ca", "us"]

            [[series]]
            slug = "deltalan"
            title = "DeltaLAN"
            alternative_titles = ["Δ LAN", "Δέλτα LAN"]
            country_codes = ["au"]

            [series.links.website]
            url = "https://www.deltalan.example/"
            """)
