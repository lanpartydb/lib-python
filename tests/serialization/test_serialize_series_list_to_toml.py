"""
:Copyright: 2024-2025 Jochen Kupperschmidt
:License: MIT
"""

from textwrap import dedent

from lanpartydb.models import Series
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
            """)
