import json

import requests

URL = 'https://mydelivengo.laposte.fr/api/v2/'


class PyDelivengo(object):
    """A class to manage the interaction with the MyDelivengo API"""

    def __init__(self, api_authorization):
        """Create the headers for the connection with MyDelivengo API"""
        self.headers = {
            'cookie': 'locale=fr;',
            'api-authorization': api_authorization,
        }

    def get_depots(self, params=None):
        """
        Return all the deposits.

        :param params: dict of parameters for the request.
        :type params: dict
        :return: a list of deposits.
        :rtype: dict
        """
        url = URL + 'depots'
        response = requests.request('GET', url, headers=self.headers, params=params)
        return json.loads(response.text)

    def get_depot(self, depot_id, params=None):
        """
        Return the data for the ID.

        :param depot_id: the ID of the deposit.
        :type depot_id: int
        :return: a dictionary with deposit's data for the ID given.
        :rtype: dict
        """
        url = URL + 'depots/' + str(depot_id)
        response = requests.request('GET', url, headers=self.headers, params=params)
        return json.loads(response.text)

    # -------------------------------------------------------------------------

    def get_envois(self, params=None):
        """
        Get all the shipments.

        :return: all the shipments.
        :rtype: dict
        """
        url = URL + 'envois'
        response = requests.request('GET', url, headers=self.headers, params=params)
        return json.loads(response.text)

    def get_envoi(self, envoi_id, params=None):
        """
        Get the data for the ID given.

        :param envoi_id: a shipment ID.
        :type envoi_id: int
        :return: a dict with the data of the shipment.
        :rtype: dict
        """
        url = URL + 'envois/' + str(envoi_id)
        response = requests.request('GET', url, headers=self.headers, params=params)
        return json.loads(response.text)

    def delete_envois(self, envoi_id):
        """
        Delete the shipment for the ID given.

        :param envoi_id: the ID of the shipment to delete.
        :type envoi_id: int
        :return: the request's status.
        :rtype: bool
        """
        url = URL + 'envois/' + str(envoi_id)
        response = requests.request('DELETE', url, headers=self.headers)
        return response.ok

    # -------------------------------------------------------------------------

    def get_imputations(self):
        """
        Get all the imputations.

        :return: a list of imputations.
        :rtype: dict
        """
        url = URL + 'imputations/'
        response = requests.request('GET', url, headers=self.headers)
        return json.loads(response.text)

    def get_imputation(self, imputation_id):
        """
        Get the imputation for the ID given.

        :param imputation_id: the ID of the imputation.
        :type imputation_id: int
        :return: a dict with the data of this imputation.
        :rtype: dict
        """
        url = URL + 'imputations/' + str(imputation_id)
        response = requests.request('GET', url, headers=self.headers)
        return json.loads(response.text)

    # -------------------------------------------------------------------------

    def get_plis(self, params=None):
        """
        Get all the envelopes.

        :return: a list of envelopes.
        :rtype: dict
        """
        url = URL + 'plis'
        response = requests.request('GET', url, headers=self.headers, params=params)
        return json.loads(response.text)

    def get_pli(self, pli_id):
        """
        Get the envelope for the ID given.

        :param pli_id: The ID of the envelope.
        :type pli_id: int
        :return: a dict with data of the envelope for the ID given.
        :rtype: dict
        """
        url = URL + 'plis/' + str(pli_id)
        response = requests.request('GET', url, headers=self.headers)
        return json.loads(response.text)

    def delete_plis(self, pli_id):
        """
        Delete the envelope with the ID given.

        :param pli_id: the ID of the envelope to delete.
        :type pli_id: int
        :return: the request's status.
        :rtype: bool
        """
        url = URL + 'plis/' + str(pli_id)
        response = requests.request('DELETE', url, headers=self.headers)
        return response.ok

    # -------------------------------------------------------------------------

    def get_user_info(self, user_id=0):
        """
        Return the data for the user given (if empty, return the data for the main account).

        :param user_id: the ID
        :type user_id: int
        :return: a dict with the data of the user
        :rtype: dict
        """
        url = URL + 'utilisateurs/' + str(user_id)
        response = requests.request('GET', url, headers=self.headers)
        return json.loads(response.text)
