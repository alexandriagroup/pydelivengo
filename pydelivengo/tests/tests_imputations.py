#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2018 Alexandria
#
# Distributed under terms of the MIT license.

from __future__ import absolute_import

import pytest

from pydelivengo.exception import PyDelivengoTypeError
from pydelivengo.pydelivengo import PyDelivengo


def test_get_imputation():
    """Test get_imputation when imputation_id is none."""
    api = PyDelivengo(api_authorization='Loremipsumdolorsitametconsectetu')
    with pytest.raises(PyDelivengoTypeError):
        # noinspection PyTypeChecker
        api.get_imputation(imputation_id=None)
