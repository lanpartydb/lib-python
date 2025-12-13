"""
:Copyright: 2024-2025 Jochen Kupperschmidt
:License: MIT
"""

import pytest

from lanpartydb.deserialization import deserialize_series_from_toml
from lanpartydb.models import Series


@pytest.mark.parametrize(
    ('toml', 'expected'),
    [
        (
            """
            slug = "megalan"
            title = "MegaLAN"
            """,
            Series(
                slug='megalan',
                title='MegaLAN',
                alternative_titles=[],
                country_codes=[],
            ),
        ),
        (
            """
            slug = "gammalan"
            title = "GammaLAN"
            country_codes = ["ca", "us"]
            """,
            Series(
                slug='gammalan',
                title='GammaLAN',
                alternative_titles=[],
                country_codes=['ca', 'us'],
            ),
        ),
        (
            """
            slug = "deltalan"
            title = "DeltaLAN"
            alternative_titles = ["Δ LAN", "Δέλτα LAN"]
            country_codes = ["au"]
            """,
            Series(
                slug='deltalan',
                title='DeltaLAN',
                alternative_titles=['Δ LAN', 'Δέλτα LAN'],
                country_codes=['au'],
            ),
        ),
    ],
)
def test_deserialize_series_from_toml(toml: str, expected: Series):
    assert deserialize_series_from_toml(toml) == expected
