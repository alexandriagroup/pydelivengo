# Copyright © 2018 Alexandria
#
# Distributed under terms of the MIT license.

from codecs import open

import pytest
import requests_mock

from pydelivengo.exception import PyDelivengoTypeError
from pydelivengo.pydelivengo import PyDelivengo


# ----------------------------------------------------- get_envois -----------------------------------------------------

def test_get_envois():
    """Test get_envois with a mock."""
    with requests_mock.Mocker() as m:
        api_response = open("pydelivengo/tests/assets/get_envois_ok.json", "rb", encoding='utf8').read()
        m.get('https://mydelivengo.laposte.fr/api/v2/envois', text=api_response)

        api = PyDelivengo(api_authorization='Loremipsumdolorsitametconsectetu')
        result = api.get_envois()

        assert result == {"data": [
            {"id": "5256598", "id_support": "33", "id_utilisateur": "22852",
             "date_creation": "2018-01-18 10:48:37", "date_impression": "2018-01-18 10:48:37",
             "descriptif": "DESCRIPTIF DELIVENGO SUIVI 18", "total": "2",
             "plis": ["11349969", "11349970"]}], "recordsFiltered": 1, "recordsTotal": 1}


def test_get_envois_type_error():
    """Test get_envois when params is not a dictionary."""
    api = PyDelivengo(api_authorization='Loremipsumdolorsitametconsectetu')
    with pytest.raises(PyDelivengoTypeError):
        # noinspection PyTypeChecker
        api.get_envois(params='lolcatz')

# ----------------------------------------------------- get_envoi ------------------------------------------------------

def test_get_envoi_pdf():
    """Test get_envoi with a mock."""
    with requests_mock.Mocker() as m:
        api_response = open("pydelivengo/tests/assets/get_envoi_ok.json", "rb", encoding='utf8').read()
        m.get('https://mydelivengo.laposte.fr/api/v2/envois/5306429', text=api_response)

        api = PyDelivengo(api_authorization='Loremipsumdolorsitametconsectetu')
        result = api.get_envoi(5306429 )

        # Check if 'id', 'plis' and 'documents_supports' are keys of result
        data_keys_set = set(result['data'].keys())
        assert {'id', 'id_support', 'id_utilisateur', 'date_creation', 'date_impression'}.issubset(data_keys_set)


def test_get_envoi():
    """Test get_envoi with pdf"""
    with requests_mock.Mocker() as m:
        api_response = open("pydelivengo/tests/assets/get_envoi_pdf_ok.json", "rb", encoding='utf8').read()
        m.get('https://mydelivengo.laposte.fr/api/v2/envois/5306429', text=api_response)

        api = PyDelivengo(api_authorization='Loremipsumdolorsitametconsectetu')
        result = api.get_envoi(5306429, print_pdf=True)

        # Check if 'id', 'plis' and 'documents_supports' are keys of result
        data_keys_set = set(result['data'].keys())
        assert {'id', 'plis', 'documents_supports'}.issubset(data_keys_set)


def test_get_envoi_missing_parameter():
    """Test get_envoi when envoi_id is none."""
    api = PyDelivengo(api_authorization='Loremipsumdolorsitametconsectetu')
    with pytest.raises(PyDelivengoTypeError):
        # noinspection PyTypeChecker
        api.get_envoi(envoi_id=None)


def test_get_envoi_type_error():
    """Test get_envoi when params is not a dictionary."""
    api = PyDelivengo(api_authorization='Loremipsumdolorsitametconsectetu')
    with pytest.raises(PyDelivengoTypeError):
        # noinspection PyTypeChecker
        api.get_envoi(123, params='lolcatz')


# --------------------------------------------------- delete_envois ----------------------------------------------------

# def test_delete_envois():  # FIXME: find how to return "ok = true" in the mock
#     """Test delete_envois with a mock."""
#     with requests_mock.Mocker() as m:
#         # api_response = open("pydelivengo/tests/assets/delete_envoi_ok.json", "rb", encoding='utf8').read()
#         m.delete('https://mydelivengo.laposte.fr/api/v2/envois/5306429', text='[]', ok=True)
#
#         api = PyDelivengo(api_authorization='Loremipsumdolorsitametconsectetu')
#         result = api.delete_envois(5306429)
#         # import pdb; pdb.set_trace()
#
#         assert result == True


def test_delete_envois_param_none():
    """Test delete_envois when envoi_id is none."""
    api = PyDelivengo(api_authorization='Loremipsumdolorsitametconsectetu')
    with pytest.raises(PyDelivengoTypeError):
        # noinspection PyTypeChecker
        api.delete_envois(envoi_id=None)


def test_delete_envois_type_error():
    """Test delete_envois when there is a type error on envoi_id."""
    api = PyDelivengo(api_authorization='Loremipsumdolorsitametconsectetu')
    with pytest.raises(PyDelivengoTypeError):
        # noinspection PyTypeChecker
        api.delete_envois(envoi_id='lolcatz')


# ---------------------------------------------------- post_envois -----------------------------------------------------

def test_post_envois_param_none():
    """Test post_envois when data_dict is none."""
    api = PyDelivengo(api_authorization='Loremipsumdolorsitametconsectetu')
    with pytest.raises(PyDelivengoTypeError):
        # noinspection PyTypeChecker
        api.post_envois(data_dict=None)


def test_post_envoi_type_error():
    """Test post_envois when data_dict is not a dictionary."""
    api = PyDelivengo(api_authorization='Loremipsumdolorsitametconsectetu')
    with pytest.raises(PyDelivengoTypeError):
        # noinspection PyTypeChecker
        api.post_envois(data_dict='lolcatz')

def test_post_envoi_type_param_error():
    """Test post_envois when params is not a dictionary."""
    api = PyDelivengo(api_authorization='Loremipsumdolorsitametconsectetu')
    with pytest.raises(PyDelivengoTypeError):
        # noinspection PyTypeChecker
        api.post_envois(data_dict={}, params='')
