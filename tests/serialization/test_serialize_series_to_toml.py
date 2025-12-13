"""
:Copyright: 2024-2025 Jochen Kupperschmidt
:License: MIT
"""

from textwrap import dedent

import pytest

from lanpartydb.models import Series, SeriesLinks, Resource
from lanpartydb.serialization import serialize_series_to_toml


@pytest.mark.parametrize(
    ('series', 'expected'),
    [
        (
            Series(
                slug='gammalan',
                title='GammaLAN',
                alternative_titles=[],
                country_codes=['ca', 'us'],
            ),
            dedent("""\
            slug = "gammalan"
            title = "GammaLAN"
            country_codes = ["ca", "us"]
            """),
        ),
        (
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
            dedent("""\
            slug = "deltalan"
            title = "DeltaLAN"
            alternative_titles = ["Δ LAN", "Δέλτα LAN"]
            country_codes = ["au"]

            [links.website]
            url = "https://www.deltalan.example/"
            """),
        ),
        (
            Series(
                slug='epsilan',
                title='EpsiLAN',
                country_codes=['gr'],
                links=SeriesLinks(
                    website=Resource(
                        url='https://www.epsilan.example/',
                        offline=True,
                    ),
                ),
            ),
            dedent("""\
            slug = "epsilan"
            title = "EpsiLAN"
            country_codes = ["gr"]

            [links.website]
            url = "https://www.epsilan.example/"
            offline = true
            """),
        ),
    ],
)
def test_serialize_series_to_toml(series: Series, expected: str):
    assert serialize_series_to_toml(series) == expected
