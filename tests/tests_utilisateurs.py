# Copyright © 2018 Alexandria
#
# Distributed under terms of the MIT license.

from codecs import open

import pytest
import requests_mock

from pydelivengo.exception import PyDelivengoTypeError
from pydelivengo.pydelivengo import PyDelivengo


def test_get_user_info():
    """Test get_user_info  with a mock."""
    with requests_mock.Mocker() as m:
        api_response = open("tests/assets/get_utilisateur_ok.json", "rb", encoding='utf8').read()
        m.get('https://mydelivengo.laposte.fr/api/v2/utilisateurs/0', text=api_response)

        api = PyDelivengo(api_authorization='Loremipsumdolorsitametconsectetu')
        result = api.get_user_info()

        assert result == {"data": {"id": "22852", "email": "johndoe@my_best_company.com",
                                   "nom": "Doe", "prenom": "John"}}


def test_get_user_info_type_none():
    """Test get_user_info when user_id is none."""
    api = PyDelivengo(api_authorization='Loremipsumdolorsitametconsectetu')
    with pytest.raises(PyDelivengoTypeError):
        # noinspection PyTypeChecker
        api.get_user_info(user_id=None)


def test_get_user_info_type_error():
    """Test get_user_info when user_id is not an integer."""
    api = PyDelivengo(api_authorization='Loremipsumdolorsitametconsectetu')
    with pytest.raises(PyDelivengoTypeError):
        # noinspection PyTypeChecker
        api.get_user_info(user_id='lolcatz')
