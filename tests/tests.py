# -*- coding: utf-8 -*-
import requests_mock
from codecs import open

from pydelivengo.pydelivengo import PyDelivengo


def test_get_depots():
    """Test get_depots function"""
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


def test_get_envois():
    """Test get_envois function"""
    with requests_mock.Mocker() as m:
        api_response = open("tests/assets/get_envois_ok.json", "rb", encoding='utf8').read()
        m.get('https://mydelivengo.laposte.fr/api/v2/envois', text=api_response)

        api = PyDelivengo(api_authorization='Loremipsumdolorsitametconsectetu')
        result = api.get_envois()

        assert result == {"data": [
            {"id": "5256598", "id_support": "33", "id_utilisateur": "22852",
             "date_creation": "2018-01-18 10:48:37", "date_impression": "2018-01-18 10:48:37",
             "descriptif": "DESCRIPTIF DELIVENGO SUIVI 18", "total": "2",
             "plis": ["11349969", "11349970"]}], "recordsFiltered": 1, "recordsTotal": 1}


def test_get_plis():
    """Test get_plis function"""
    with requests_mock.Mocker() as m:
        api_response = open("tests/assets/get_plis_ok.json", "rb", encoding='utf8').read()
        m.get('https://mydelivengo.laposte.fr/api/v2/plis', text=api_response)

        api = PyDelivengo(api_authorization='Loremipsumdolorsitametconsectetu')
        result = api.get_plis()

        assert 'data' in result.keys()

        # Check if there are some keys in the result
        data_keys_set = set(result['data'][0].keys())
        assert {'id', 'id_envoi', 'numero', 'date_creation'}.issubset(data_keys_set)


def test_get_user_info():
    """Test get_user_info function"""
    with requests_mock.Mocker() as m:
        api_response = open("tests/assets/get_utilisateur_ok.json", "rb", encoding='utf8').read()
        m.get('https://mydelivengo.laposte.fr/api/v2/utilisateurs/0', text=api_response)

        api = PyDelivengo(api_authorization='Loremipsumdolorsitametconsectetu')
        result = api.get_user_info()

        assert result == {"data": {"id": "22852", "email": "johndoe@my_best_company.com",
                                   "nom": "Doe", "prenom": "John"}}

