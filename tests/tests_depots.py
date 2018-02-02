# Copyright © 2018 Alexandria
#
# Distributed under terms of the MIT license.

from codecs import open

import pytest
import requests_mock

from pydelivengo.exception import PyDelivengoTypeError
from pydelivengo.pydelivengo import PyDelivengo


# ------------------------------------------------------ get_depots ----------------------------------------------------

def test_get_depots():
    """Test get_depots function with a mock."""
    with requests_mock.Mocker() as m:
        api_response = open("tests/assets/get_depots_ok.json", "rb", encoding='utf8').read()
        m.get('https://mydelivengo.laposte.fr/api/v2/depots', text=api_response)

        api = PyDelivengo(api_authorization='Loremipsumdolorsitametconsectetu')
        result = api.get_depots()

        assert result == {"data": [
            {"id": 1814183, "id_utilisateur": 22852, "date": "2018-01-15 14:57:51",
             "num_coclico": "2205490", "num_siret": "",
             "bordereaux": [
                 {"id": 1727987, "numero": "0000000001",
                  "nb_pages": 2, "type": 35}]}],
            "recordsFiltered": 1, "recordsTotal": 1}


def test_get_depots_type_error():
    """Test get_depots when params is not a dictionary."""
    api = PyDelivengo(api_authorization='Loremipsumdolorsitametconsectetu')
    with pytest.raises(PyDelivengoTypeError):
        # noinspection PyTypeChecker
        api.get_depots(params='lolcatz')


# ------------------------------------------------------ get_depot -----------------------------------------------------

def test_get_depot():
    """Test get_depot with a mock."""
    with requests_mock.Mocker() as m:
        api_response = open("tests/assets/get_depot_ok.json", "rb", encoding='utf8').read()
        m.get('https://mydelivengo.laposte.fr/api/v2/depots/1814183', text=api_response)

        api = PyDelivengo(api_authorization='Loremipsumdolorsitametconsectetu')
        result = api.get_depot(1814183)

        assert result == {"data": {"id": 1814183, "id_utilisateur": 22855, "date": "2018-01-15 14:57:51",
                                   "num_coclico": "2205490", "num_siret": "",
                                   "bordereaux": [{"id": 1727987,  "numero": "0000000001",
                                                   "nb_pages": 2, "type": 35, "plis": []}]}
                          }


def test_get_depot_application_pdf():
    """Test get_depot when the pdf is requested."""
    with requests_mock.Mocker() as m:
        api_response = open("tests/assets/get_depot_ok.json", "rb", encoding='utf8').read()
        m.get('https://mydelivengo.laposte.fr/api/v2/depots/1814183', text=api_response)

        api = PyDelivengo(api_authorization='Loremipsumdolorsitametconsectetu')
        result = api.get_depot(1814183, print_pdf=True)

        assert result == {"data": {"id": 1814183, "id_utilisateur": 22855, "date": "2018-01-15 14:57:51",
                                   "num_coclico": "2205490", "num_siret": "",
                                   "bordereaux": [{"id": 1727987,  "numero": "0000000001",
                                                   "nb_pages": 2, "type": 35, "plis": []}]}
                          }


def test_get_depot_missing_parameter():
    """Test get_depot when depot_id is none."""
    api = PyDelivengo(api_authorization='Loremipsumdolorsitametconsectetu')
    with pytest.raises(PyDelivengoTypeError):
        # noinspection PyTypeChecker
        api.get_depot(depot_id=None)


def test_get_depot_type_error():
    """Test get_depot when params is not a dictionary."""
    api = PyDelivengo(api_authorization='Loremipsumdolorsitametconsectetu')
    with pytest.raises(PyDelivengoTypeError):
        # noinspection PyTypeChecker
        api.get_depot(123, params='lolcatz')


# ------------------------------------------------------ post_depot ----------------------------------------------------

def test_post_depot_param_none():
    """Test post_depot when data_dict is none."""
    api = PyDelivengo(api_authorization='Loremipsumdolorsitametconsectetu')
    with pytest.raises(PyDelivengoTypeError):
        # noinspection PyTypeChecker
        api.post_depot(data_dict=None)


def test_post_depot_type_error():
    """Test post_depot when data_dict is not a dictionary."""
    api = PyDelivengo(api_authorization='Loremipsumdolorsitametconsectetu')
    with pytest.raises(PyDelivengoTypeError):
        # noinspection PyTypeChecker
        api.post_depot(data_dict='lolcatz')
