#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2018 Alexandria
#
# Distributed under terms of the MIT license.

from __future__ import absolute_import

import json

import requests

from pydelivengo.exception import PyDelivengoTypeError

URL = 'https://mydelivengo.laposte.fr/api/v2/'


def add_headers(x, y):
    """
    Add new headers.

    :param x: a dict with headers for the API
    :type x: dict
    :param y: a dict with headers for the API
    :type y: dict
    :return: a dict with headers merged
    :rtype: dict
    """
    z = x.copy()
    z.update(y)
    return z


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
        if params is not None and not isinstance(params, dict):
            raise PyDelivengoTypeError('params should be a dictionary and not {}.'.format(type(params)))

        url = URL + 'depots'
        response = requests.request('GET', url, headers=self.headers, params=params)
        return json.loads(response.text)

    def get_depot(self, depot_id, params=None, print_pdf=False):
        """
        Return the data for the ID.

        :param depot_id: the ID of the deposit.
        :type depot_id: int
        :param params: dict of parameters for the request.
        :type params: dict
        :param print_pdf: True if you want the PDF of the deposit, else False.
        :type print_pdf: bool
        :return: a dictionary with deposit's data for the ID given.
        :rtype: dict
        """
        if not isinstance(depot_id, int):
            raise PyDelivengoTypeError('depot_id should be a dictionary and not {}.'.format(type(depot_id)))
        if params is not None and not isinstance(params, dict):
            raise PyDelivengoTypeError('params should be a dictionary and not {}.'.format(type(params)))

        url = URL + 'depots/' + str(depot_id)

        if print_pdf:  # Merge the 2 dicts
            headers = add_headers(self.headers, {'Accept': 'application/pdf'})
        else:
            headers = self.headers

        response = requests.request('GET', url, headers=headers, params=params)
        return json.loads(response.text)

    def post_depot(self, data_dict, print_pdf=False):
        """
        Post a deposit.

        :param data_dict: the data of the deposit.
        :type data_dict: dict
        :param print_pdf: True if you want the PDF of the deposit, else False.
        :type print_pdf: bool
        :return: a dict of the new deposit posted.
        :rtype: dict
        """
        if not isinstance(data_dict, dict):
            raise PyDelivengoTypeError('data_dict should be a dictionary and not {}.'.format(type(data_dict)))

        url = URL + 'depots/'

        if print_pdf:  # Merge the 2 dicts
            headers = add_headers(self.headers, {'Accept': 'application/pdf'})
        else:
            headers = self.headers

        # Json encoding
        data_json = json.dumps(data_dict)

        response = requests.request('POST', url, data=data_json, headers=headers)
        return json.loads(response.text)

    # -------------------------------------------------------------------------

    def get_envois(self, params=None):
        """
        Get all the shipments.

        :param params: dict of parameters for the request.
        :type params: dict
        :return: all the shipments.
        :rtype: dict
        """
        if params is not None and not isinstance(params, dict):
            raise PyDelivengoTypeError('params should be a dictionary and not {}.'.format(type(params)))

        url = URL + 'envois'
        response = requests.request('GET', url, headers=self.headers, params=params)
        return json.loads(response.text)

    def get_envoi(self, envoi_id, params=None, print_pdf=False):
        """
        Get the data for the ID given.

        :param envoi_id: a shipment ID.
        :type envoi_id: int
        :param params: dict of parameters for the request.
        :type params: dict
        :param print_pdf: True if you want the PDF of the deposit, else False.
        :type print_pdf: bool
        :return: a dict with the data of the shipment.
        :rtype: dict
        """
        if not isinstance(envoi_id, int):
            raise PyDelivengoTypeError('Type of envoi_id should be int and not {}.'.format(type(envoi_id)))
        if params is not None and not isinstance(params, dict):
            raise PyDelivengoTypeError('params should be a dictionary and not {}.'.format(type(params)))

        url = URL + 'envois/' + str(envoi_id)

        if print_pdf:  # Merge the 2 dicts
            headers = add_headers(self.headers, {'Accept': 'application/pdf'})
        else:
            headers = self.headers

        response = requests.request('GET', url, headers=headers, params=params)
        return json.loads(response.text)

    def delete_envois(self, envoi_id):
        """
        Delete the shipment for the ID given.

        :param envoi_id: the ID of the shipment to delete.
        :type envoi_id: int
        :return: the request's status.
        :rtype: bool
        """
        if not isinstance(envoi_id, int):
            raise PyDelivengoTypeError('pli_id should be an integer and not a {}'.format(type(envoi_id)))

        url = URL + 'envois/' + str(envoi_id)
        response = requests.request('DELETE', url, headers=self.headers)
        return response.ok

    def post_envois(self, data_dict, print_pdf=False, params=None):
        """
        Post a shipment.

        :param data_dict: the data of the shipment.
        :type data_dict: dict
        :param print_pdf: True if you want the PDF of the deposit, else False.
        :type print_pdf: bool
        :param params: dict of parameters for the request.
        :type params: dict
        :return: a dict of the new deposit posted.
        :rtype: dict
        """
        if not isinstance(data_dict, dict):
            raise PyDelivengoTypeError('data_dict should be a and not a {}'.format(type(data_dict)))
        if params is not None and not isinstance(params, dict):
            raise PyDelivengoTypeError('params should be a dictionary and not {}.'.format(type(params)))

        url = URL + 'envois/'

        if print_pdf:  # Merge the 2 dicts
            headers = add_headers(self.headers, {'Accept': 'application/pdf'})
        else:
            headers = self.headers

        # Json encoding
        data_json = json.dumps(data_dict)

        # Request
        response = requests.request('POST', url, data=data_json, headers=headers, params=params)
        return json.loads(response.text)

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
        if not isinstance(imputation_id, int):
            raise PyDelivengoTypeError('pli_id should be an integer and not a {}'.format(type(imputation_id)))

        url = URL + 'imputations/' + str(imputation_id)
        response = requests.request('GET', url, headers=self.headers)
        return json.loads(response.text)

    # -------------------------------------------------------------------------

    def get_plis(self, params=None):
        """
        Get all the envelopes.

        :param params: dict of parameters for the request.
        :type params: dict
        :return: a list of envelopes.
        :rtype: dict
        """
        if params is not None and not isinstance(params, dict):
            raise PyDelivengoTypeError('params should be a dictionary and not {}.'.format(type(params)))

        url = URL + 'plis'
        response = requests.request('GET', url, headers=self.headers, params=params)
        return json.loads(response.text)

    def get_pli(self, pli_id, print_pdf=False):
        """
        Get the envelope for the ID given.

        :param pli_id: The ID of the envelope.
        :type pli_id: int
        :param print_pdf: True if you want the PDF of the deposit, else False.
        :type print_pdf: bool
        :return: a dict with data of the envelope for the ID given.
        :rtype: dict
        """
        if not isinstance(pli_id, int):
            raise PyDelivengoTypeError('pli_id should be an integer and not a {}'.format(type(pli_id)))

        url = URL + 'plis/' + str(pli_id)

        if print_pdf:  # Merge the 2 dicts
            headers = add_headers(self.headers, {'Accept': 'application/pdf'})
        else:
            headers = self.headers

        response = requests.request('GET', url, headers=headers)
        return json.loads(response.text)

    def delete_plis(self, pli_id):
        """
        Delete the envelope with the ID given.

        :param pli_id: the ID of the envelope to delete.
        :type pli_id: int
        :return: the request's status.
        :rtype: bool
        """
        if not isinstance(pli_id, int):
            raise PyDelivengoTypeError('pli_id should be an integer and not a {}'.format(type(pli_id)))

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
        if not isinstance(user_id, int):
            raise PyDelivengoTypeError('user_id should be an integer and not a {}'.format(type(user_id)))

        url = URL + 'utilisateurs/' + str(user_id)
        response = requests.request('GET', url, headers=self.headers)
        return json.loads(response.text)
