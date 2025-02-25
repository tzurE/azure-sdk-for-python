# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class CategoryType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    WORKBOOK = "workbook"
    TSG = "TSG"
    PERFORMANCE = "performance"
    RETENTION = "retention"

class CreatedByType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of identity that created the resource.
    """

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"

class Kind(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The kind of workbook. Choices are user and shared.
    """

    USER = "user"
    SHARED = "shared"

class ManagedServiceIdentityType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Type of managed service identity (where both SystemAssigned and UserAssigned types are
    allowed).
    """

    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned,UserAssigned"

class SharedTypeKind(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The kind of workbook. Choices are user and shared.
    """

    USER = "user"
    SHARED = "shared"
