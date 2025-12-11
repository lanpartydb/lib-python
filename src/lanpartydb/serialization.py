"""
lanpartydb.serialization
~~~~~~~~~~~~~~~~~~~~~~~~

Object serialization to TOML

:Copyright: 2024-2025 Jochen Kupperschmidt
:License: MIT
"""

import dataclasses
from typing import Any

from lanpartydb.models import Party, Series
import tomlkit


# series


def serialize_series_list(series_list: list[Series]) -> str:
    """Serialize list of series to TOML document."""
    aot = tomlkit.aot()

    for series in series_list:
        series_dict = _series_to_sparse_dict(series)
        aot.append(tomlkit.item(series_dict))

    doc = tomlkit.document()
    doc.append('series', aot)

    return _write_toml(doc)


def serialize_series(series: Series) -> str:
    """Serialize series to TOML document."""
    series_dict = _series_to_sparse_dict(series)

    return _write_toml(series_dict)


def _series_to_sparse_dict(series: Series) -> dict[str, Any]:
    data = dataclasses.asdict(series)
    _remove_default_values(data)
    return data


# party


def serialize_party(party: Party) -> str:
    """Serialize party to TOML document."""
    party_dict = _party_to_sparse_dict(party)

    location = party_dict.get('location', None)
    if location is not None:
        _convert_decimal_to_float(location, 'latitude')
        _convert_decimal_to_float(location, 'longitude')

    return _write_toml(party_dict)


def _party_to_sparse_dict(party: Party) -> dict[str, Any]:
    data = dataclasses.asdict(party)
    _remove_default_values(data)
    return data


def _convert_decimal_to_float(d: dict[str, Any], key: str) -> None:
    value = d.get(key)
    if value is not None:
        d[key] = float(value)


# util


def _write_toml(d: dict[str, Any]) -> str:
    return tomlkit.dumps(d)


def _remove_default_values(d: dict[str, Any]) -> dict[str, Any]:
    """Remove `None`, `False`, and `[]` values from first level of
    dictionary.
    """
    for k, v in list(d.items()):
        if (v is None) or (v is False) or (v == []):
            del d[k]
        elif isinstance(v, dict):
            _remove_default_values(v)

    return d
