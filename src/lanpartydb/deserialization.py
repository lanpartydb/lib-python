"""
lanpartydb.deserialization
~~~~~~~~~~~~~~~~~~~~~~~~~~

TOML deserialization to objects

:Copyright: 2024-2025 Jochen Kupperschmidt
:License: MIT
"""

from decimal import Decimal
from pathlib import Path
import tomllib
from typing import Any

from .models import Location, Party, PartyLinks, Resource, Series


# series


def deserialize_series_list_from_toml_file(filename: Path) -> list[Series]:
    """Deserialize list of series from a TOML file."""
    toml = filename.read_text()
    return deserialize_series_list_from_toml(toml)


def deserialize_series_list_from_toml(toml: str) -> list[Series]:
    """Deserialize list of series from a TOML document."""
    data = _load_toml(toml)
    return _deserialize_series_list_from_dict(data)


def _deserialize_series_list_from_dict(data: dict[str, Any]) -> list[Series]:
    """Build list of series from a dictionary."""
    return [Series(**item) for item in data.get('series', [])]


# party


def deserialize_party_from_toml_file(filename: Path) -> Party:
    """Deserialize party from a TOML file."""
    toml = filename.read_text()
    return deserialize_party_from_toml(toml)


def deserialize_party_from_toml(toml: str) -> Party:
    """Deserialize party from a TOML document."""
    data = _load_toml(toml)
    return _deserialize_party_from_dict(data)


def _deserialize_party_from_dict(party_dict: dict[str, Any]) -> Party:
    """Build party from a dictionary."""
    location_dict = party_dict.pop('location', None)
    if location_dict:
        party_dict['location'] = Location(**location_dict)

    links_dict = party_dict.pop('links', None)
    if links_dict:
        website_dict = links_dict.pop('website', None)
        if website_dict:
            website = Resource(
                url=website_dict['url'],
                offline=website_dict.get('offline', False),
            )
            party_dict['links'] = PartyLinks(website=website)

    return Party(**party_dict)


# util


def _load_toml(toml: str) -> str:
    return tomllib.loads(toml, parse_float=Decimal)
