# Copyright © 2018 Alexandria
#
# Distributed under terms of the MIT license.

from codecs import open

import pytest
import requests_mock

from pydelivengo.exception import PyDelivengoTypeError
from pydelivengo.pydelivengo import PyDelivengo


# ------------------------------------------------------- get_plis -----------------------------------------------------

def test_get_plis():
    """Test get_plis with a mock."""
    with requests_mock.Mocker() as m:
        api_response = open("tests/assets/get_plis_ok.json", "rb", encoding='utf8').read()
        m.get('https://mydelivengo.laposte.fr/api/v2/plis', text=api_response)

        api = PyDelivengo(api_authorization='Loremipsumdolorsitametconsectetu')
        result = api.get_plis()

        assert 'data' in result.keys()

        # Check if there are some keys in the result
        data_keys_set = set(result['data'][0].keys())
        assert {'id', 'id_envoi', 'numero', 'date_creation'}.issubset(data_keys_set)


def test_get_plis_type_error():
    """Test get_plis when params is not a dictionary."""
    api = PyDelivengo(api_authorization='Loremipsumdolorsitametconsectetu')
    with pytest.raises(PyDelivengoTypeError):
        # noinspection PyTypeChecker
        api.get_plis(params='lolcatz')


# ------------------------------------------------------- get_pli ------------------------------------------------------

# def test_get_pli():  # TODO: anonymize PDF
#     """Test get_pli when the pdf is requested."""
#     with requests_mock.Mocker() as m:
#         api_response = open("tests/assets/get_pli_pdf_ok.json", "rb", encoding='utf8').read()
#         m.get('https://mydelivengo.laposte.fr/api/v2/plis/11437479', text=api_response)
#
#         api = PyDelivengo(api_authorization='Loremipsumdolorsitametconsectetu')
#         result = api.get_pli(11437479, print_pdf=True)
#
#         # Check if 'id', 'plis' and 'documents_supports' are keys of result
#         data_keys_set = set(result['data'].keys())
#         assert {'id', 'documents_supports'}.issubset(data_keys_set)


def test_get_pli_missing_parameter():
    """Test get_pli when pli_id is none."""
    api = PyDelivengo(api_authorization='Loremipsumdolorsitametconsectetu')
    with pytest.raises(PyDelivengoTypeError):
        # noinspection PyTypeChecker
        api.get_pli(pli_id=None)


# ----------------------------------------------------- delete_plis ----------------------------------------------------

def test_delete_plis_missing_parameter():
    """Test delete_plis when pli_id is none."""
    api = PyDelivengo(api_authorization='Loremipsumdolorsitametconsectetu')
    with pytest.raises(PyDelivengoTypeError):
        # noinspection PyTypeChecker
        api.delete_plis(pli_id=None)
