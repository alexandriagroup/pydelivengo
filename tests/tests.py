# -*- coding: utf-8 -*-
import requests_mock

from pydelivengo.pydelivengo import PyDelivengo


def test_get_depots():
    """"""
    with requests_mock.Mocker() as m:
        m.get('https://mydelivengo.laposte.fr/api/v2/depots',
              text='{"data":[{"id":1814183,"id_utilisateur":22852,"date":"2018-01-15 14:57:51","num_coclico":"2205490",'
                   '"num_siret":"","bordereaux":[{"id":1727987,"numero":"0000000001","nb_pages":2,"type":35}]}],"record'
                   'sFiltered":1,"recordsTotal":1}')
        api = PyDelivengo(api_authorization='Loremipsumdolorsitametconsectetu')
        result = api.get_depots()
        assert dict == type(result)
        assert result == {"data": [
            {"id": 1814183, "id_utilisateur": 22852, "date": "2018-01-15 14:57:51",
             "num_coclico": "2205490", "num_siret": "",
             "bordereaux": [
                 {"id": 1727987, "numero": "0000000001",
                  "nb_pages": 2, "type": 35}]}],
            "recordsFiltered": 1, "recordsTotal": 1}


def test_get_envois():
    """"""
    with requests_mock.Mocker() as m:
        m.get('https://mydelivengo.laposte.fr/api/v2/envois',
              text='{"data":[{"id":"5256598","id_support":"33","id_utilisateur":"22852","date_creation":"2018-01-18 10:'
                   '48:37","date_impression":"2018-01-18 10:48:37","descriptif":"DESCRIPTIF DELIVENGO SUIVI 18","total"'
                   ':"2","plis":["11349969","11349970"]}],"recordsFiltered":1,"recordsTotal":1}')
        api = PyDelivengo(api_authorization='Loremipsumdolorsitametconsectetu')
        result = api.get_envois()
        assert dict == type(result)
        assert result == {"data": [
            {"id": "5256598", "id_support": "33", "id_utilisateur": "22852",
             "date_creation": "2018-01-18 10:48:37", "date_impression": "2018-01-18 10:48:37",
             "descriptif": "DESCRIPTIF DELIVENGO SUIVI 18", "total": "2",
             "plis": ["11349969", "11349970"]}], "recordsFiltered": 1, "recordsTotal": 1}


def test_get_plis():
    """"""
    with requests_mock.Mocker() as m:
        m.get('https://mydelivengo.laposte.fr/api/v2/plis',
              text='{"data":[{"id":11349969,"id_envoi":"5256598","numero":"LD037180243FR","date_creation":"2018-01-18 1'
                   '0:48:37","date_impression":"2018-01-18 10:48:37","date_depot":null,"date_retour_ar":null,"descripti'
                   'f":"DESCRIPTIF DELIVENGO SUIVI 18","reference":"","reference_interne":"DESCRIPTIF DELIVENGO SUIVI 1'
                   '8Réf du 1er pli 2","options":"68","support":{"id":33,"nom":"Delivengo Suivi","nom_long":"Delivengo '
                   'Suivi","nom_court":"DELIVENGOSUIVI","code":"DELIVENGOSUIVI","classname":"DelivengoSuivi","transport'
                   'er_code":"LP2"},"imputation":{"libelle":"Doe John","id_code_imputation":0,"id_utilisateur_imputatio'
                   'n":22852},"createur":{"id":22852,"nom":"Doe John","email":"johndoe@my_best_company.com"},"expediteu'
                   'r":{"raison_sociale":"EXPEDITEUR RAISON SOCIALE","nom":"EXPEDITEUR NOM EXPEDITEUR NOM EXPEDITE","co'
                   'mplement_voie":"EXPEDITEUR COMPLEMENT VOIE EXPEDITEUR","voie":"26 RUE GEORGE SAND 26 RUE GEORGE SAN'
                   'D2","boite_postale":"EXPEDITEUR BOITE POSTALEEXPEDITEUR BOI","code_postal_commune":"75016 PARIS","p'
                   'ays":""},"destinataire":{"raison_sociale":"DESTINATAIRE 1","nom":"EXPEDITEUR NOM EXPEDITEUR NOM EXP'
                   'EDITE","complement_voie":"EXPEDITEUR COMPLEMENT VOIE EXPEDITEUR","voie":"26 RUE GEORGE SAND 26 RUE '
                   'GEORGE SAND2","boite_postale":"EXPEDITEUR BOITE POSTALEEXPEDITEUR BOI","code_postal_commune":"75016'
                   ' PARIS","pays":"FRANCE"},"retour_ar":{"raison_sociale":null,"nom":null,"complement_voie":null,"voie'
                   '":null,"boite_postale":null,"code_postal_commune":"","pays":""},"documents_douaniers":[],"tracking"'
                   ':{"url":null,"api_key":null},"statut":{"id":"0","libelle":"Préparation","date":null},"data":{"email'
                   's_notifications_suivi":[],"email_destinataire":"jean.reneau@test.fr","reference":"","envoiNotificat'
                   'ion":"0","poids":100},"cart":null}],"recordsFiltered":1,"recordsTotal":1}')
        api = PyDelivengo(api_authorization='Loremipsumdolorsitametconsectetu')
        result = api.get_plis()
        assert 'data' in result.keys()
        assert dict == type(result)

        # Check if there are some keys in the result
        data_keys_set = set(result['data'][0].keys())
        assert {'id', 'id_envoi', 'numero', 'date_creation'}.issubset(data_keys_set)


def test_get_user_info():
    """"""
    with requests_mock.Mocker() as m:
        m.get('https://mydelivengo.laposte.fr/api/v2/utilisateurs/0',
              text='{"data":{"id":"22852","email":"johndoe@my_best_company.com","nom":"Doe","prenom":"John"}}')
        api = PyDelivengo(api_authorization='Loremipsumdolorsitametconsectetu')
        result = api.get_user_info()
        assert dict == type(result)
        assert result == {"data": {"id": "22852", "email": "johndoe@my_best_company.com",
                                   "nom": "Doe", "prenom": "John"}}

