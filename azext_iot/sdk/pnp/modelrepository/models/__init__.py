# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

try:
    from .subject_metadata_py3 import SubjectMetadata
    from .subject_py3 import Subject
    from .target_py3 import Target
    from .tenant_py3 import Tenant
except (SyntaxError, ImportError):
    from .subject_metadata import SubjectMetadata
    from .subject import Subject
    from .target import Target
    from .tenant import Tenant

__all__ = [
    'SubjectMetadata',
    'Subject',
    'Target',
    'Tenant',
]
