"""
:Copyright: 2024-2025 Jochen Kupperschmidt
:License: MIT
"""

import pytest

from lanpartydb.deserialization import deserialize_series_list_from_toml
from lanpartydb.models import Series


@pytest.mark.parametrize(
    ('toml', 'expected'),
    [
        (
            """
            """,
            [],
        ),
        (
            """
            [[series]]
            slug = "megalan"
            name = "MegaLAN"
            """,
            [
                Series(
                    slug='megalan',
                    name='MegaLAN',
                    alternative_names=[],
                    country_codes=[],
                ),
            ],
        ),
        (
            """
            [[series]]
            slug = "gammalan"
            name = "GammaLAN"
            country_codes = ["ca", "us"]

            [[series]]
            slug = "deltalan"
            name = "DeltaLAN"
            alternative_names = ["Δ LAN", "Δέλτα LAN"]
            country_codes = ["au"]
            """,
            [
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
            ],
        ),
    ],
)
def test_deserialize_series_list_from_toml(toml: str, expected: list[Series]):
    assert deserialize_series_list_from_toml(toml) == expected
