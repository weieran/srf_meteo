# coding: utf-8

"""
    SRF Weather

    SRF Meteo serves weather forecast for over 100'000 locations within Switzerland  # noqa: E501

    The version of the OpenAPI document: 1.0.4
    Contact: api@srgssr.ch
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, List
from pydantic import BaseModel, StrictInt, StrictStr, conlist

class GeolocationNamesObj(BaseModel):
    """
    GeolocationNamesObj
    """
    id: StrictInt = ...
    lat: StrictInt = ...
    lon: StrictInt = ...
    station_id: StrictStr = ...
    timezone: StrictStr = ...
    default_name: StrictStr = ...
    district: StrictStr = ...
    geolocation_names: conlist(Dict[str, Any]) = ...
    __properties = ["id", "lat", "lon", "station_id", "timezone", "default_name", "district", "geolocation_names"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> GeolocationNamesObj:
        """Create an instance of GeolocationNamesObj from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GeolocationNamesObj:
        """Create an instance of GeolocationNamesObj from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return GeolocationNamesObj.parse_obj(obj)

        _obj = GeolocationNamesObj.parse_obj({
            "id": obj.get("id"),
            "lat": obj.get("lat"),
            "lon": obj.get("lon"),
            "station_id": obj.get("station_id"),
            "timezone": obj.get("timezone"),
            "default_name": obj.get("default_name"),
            "district": obj.get("district"),
            "geolocation_names": obj.get("geolocation_names")
        })
        return _obj
