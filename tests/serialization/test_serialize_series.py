"""
:Copyright: 2024-2025 Jochen Kupperschmidt
:License: MIT
"""

from textwrap import dedent

import pytest

from lanpartydb.models import Series
from lanpartydb.serialization import (
    serialize_series_to_toml,
    serialize_series_list_to_toml,
)


def test_serialize_series_list_to_toml():
    series_list = [
        Series(
            slug='gammalan',
            name='GammaLAN',
            alternative_names=[],
            country_codes=['ca', 'us'],
        ),
        Series(
            slug='deltalan',
            name='DeltaLAN',
            alternative_names=['Δ LAN', 'Δέλτα LAN'],
            country_codes=['au'],
        ),
    ]

    assert serialize_series_list_to_toml(series_list) == dedent("""\
            [[series]]
            slug = "gammalan"
            name = "GammaLAN"
            country_codes = ["ca", "us"]

            [[series]]
            slug = "deltalan"
            name = "DeltaLAN"
            alternative_names = ["Δ LAN", "Δέλτα LAN"]
            country_codes = ["au"]
            """)


@pytest.mark.parametrize(
    ('series', 'expected'),
    [
        (
            Series(
                slug='gammalan',
                name='GammaLAN',
                alternative_names=[],
                country_codes=['ca', 'us'],
            ),
            dedent("""\
            slug = "gammalan"
            name = "GammaLAN"
            country_codes = ["ca", "us"]
            """),
        ),
        (
            Series(
                slug='deltalan',
                name='DeltaLAN',
                alternative_names=['Δ LAN', 'Δέλτα LAN'],
                country_codes=['au'],
            ),
            dedent("""\
            slug = "deltalan"
            name = "DeltaLAN"
            alternative_names = ["Δ LAN", "Δέλτα LAN"]
            country_codes = ["au"]
            """),
        ),
    ],
)
def test_serialize_series_to_toml(series: Series, expected: str):
    assert serialize_series_to_toml(series) == expected
