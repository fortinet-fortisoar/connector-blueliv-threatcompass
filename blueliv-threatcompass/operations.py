"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""
import json

import requests
from connectors.core.connector import get_logger, ConnectorError

from .constants import *

logger = get_logger('blueliv-threatcompass')


class ThreatCompass:
    def __init__(self, config):
        self.server_url = config.get('server_url')
        if not (self.server_url.startswith('https://') or self.server_url.startswith('http://')):
            self.server_url = 'https://' + self.server_url
        self.server_url = self.server_url.strip('/')
        self.api_key = config.get('api_key')
        self.verify_ssl = config.get('verify_ssl')

    def make_request(self, endpoint, method='GET', data=None, params=None, files=None):
        try:
            url = self.server_url + endpoint
            logger.info('Executing url {}'.format(url))
            headers = {'Authorization': f"Bearer {self.api_key}", 'Content-Type': 'application/json'}

            # CURL UTILS CODE
            try:
                from connectors.debug_utils.curl_script import make_curl
                make_curl(method, endpoint, headers=headers, params=params, data=data, verify_ssl=self.verify_ssl)
            except Exception as err:
                logger.error(f"Error in curl utils: {str(err)}")

            response = requests.request(method, url, params=params, files=files, data=data, headers=headers,
                                        verify=self.verify_ssl)
            if response.ok:
                logger.info('Successfully got response for url {}'.format(url))
                if method.upper() == 'DELETE':
                    return response
                else:
                    return response.json()
            elif response.status_code == 400:
                error_response = response.json()
                raise ConnectorError(error_response)
            elif response.status_code == 401:
                error_response = response.json()
                raise ConnectorError(error_response)
            elif response.status_code == 404:
                error_response = response.json()
                raise ConnectorError(error_response)
            else:
                logger.error(response.json())
        except requests.exceptions.SSLError:
            raise ConnectorError('SSL certificate validation failed')
        except requests.exceptions.ConnectTimeout:
            raise ConnectorError('The request timed out while trying to connect to the server')
        except requests.exceptions.ReadTimeout:
            raise ConnectorError('The server did not send any data in the allotted amount of time')
        except requests.exceptions.ConnectionError:
            raise ConnectorError('Invalid endpoint or credentials')
        except Exception as err:
            raise ConnectorError(str(err))
        raise ConnectorError(response.text)


def _check_health(config):
    try:
        tg = ThreatCompass(config)
        endpoint = '/api/v4/projects'
        response = tg.make_request(endpoint=endpoint)
        if response:
            logger.info("GitLab Connector Available")
            return True
    except Exception as err:
        logger.error(str(err))
        raise ConnectorError(str(err))


def _build_payload(params: dict, options_dict: dict = {}) -> dict:
    if params.get('other_fields'):
        params.update(params.pop('other_fields'))
    if params.get('module_type'):
        params.update({'module_type': MODULES_DICT.get(params.pop("module_type"))})
    return {key: options_dict.get(val, val) if isinstance(val, str) else val for key, val in params.items() if
            isinstance(val, (bool, int)) or val}


def get_resource_list(config: dict, params: dict):
    try:
        tc = ThreatCompass(config)
        params = _build_payload(params)
        endpoint = f'/api/v2/organization/{params.pop("org_id")}/module/{params.pop("module_id")}/resource'
        return tc.make_request(endpoint=endpoint, method='GET', params=params)
    except Exception as err:
        logger.error(str(err))
        raise ConnectorError(str(err))


def get_resource_by_id(config: dict, params: dict):
    try:
        tc = ThreatCompass(config)
        params = _build_payload(params)
        endpoint = f'/api/v2/organization/{params.pop("org_id")}/module/{params.pop("module_id")}/resource/{params.pop("resource_id")}'
        return tc.make_request(endpoint=endpoint, method='GET', params=params)
    except Exception as err:
        logger.error(str(err))
        raise ConnectorError(str(err))


def update_resource_status(config: dict, params: dict):
    try:
        tc = ThreatCompass(config)
        params = _build_payload(params, set_resource_status_dict)
        endpoint = f'/api/v2/organization/{params.pop("org_id")}/module/{params.pop("module_id")}/{params.pop("module_type")}/resource/{params.pop("resource_id")}/{params.pop("status")}'
        return tc.make_request(endpoint=endpoint, method='PUT', data=json.dumps(params))
    except Exception as err:
        logger.error(str(err))
        raise ConnectorError(str(err))


def update_resource_label(config: dict, params: dict):
    try:
        tc = ThreatCompass(config)
        params = _build_payload(params, set_resource_status_dict)
        endpoint = f'/api/v2/organization/{params.pop("org_id")}/module/{params.pop("module_id")}/{params.pop("module_type")}/resource/label'
        if isinstance(params.get('resources'), str):
            params.update({'resources': [params.pop("resources")]})
        return tc.make_request(endpoint=endpoint, method='PUT', data=json.dumps(params))
    except Exception as err:
        logger.error(str(err))
        raise ConnectorError(str(err))


def update_resource_read_status(config: dict, params: dict):
    try:
        tc = ThreatCompass(config)
        params = _build_payload(params)
        endpoint = f'/api/v2/organization/{params.pop("org_id")}/module/{params.pop("module_id")}/{params.pop("module_type")}/resource/markAs'
        if isinstance(params.get('resources'), str):
            params.update({'resources': [params.pop("resources")]})
        return tc.make_request(endpoint=endpoint, method='PUT', data=json.dumps(params))
    except Exception as err:
        logger.error(str(err))
        raise ConnectorError(str(err))


def update_resource_rating(config: dict, params: dict):
    try:
        tc = ThreatCompass(config)
        params = _build_payload(params)
        endpoint = f'/api/v2/organization/{params.pop("org_id")}/module/{params.pop("module_id")}/{params.pop("module_type")}/resource/rating'
        if isinstance(params.get('resources'), str):
            params.update({'resources': [params.pop("resources")]})
        return tc.make_request(endpoint=endpoint, method='PUT', data=json.dumps(params))
    except Exception as err:
        logger.error(str(err))
        raise ConnectorError(str(err))


def update_resource_fav(config: dict, params: dict):
    try:
        tc = ThreatCompass(config)
        params = _build_payload(params, set_resource_fav_dict)
        endpoint = f'/api/v2/organization/{params.pop("org_id")}/module/{params.pop("module_id")}/{params.pop("module_type")}/resource/fav'
        if isinstance(params.get('resources'), str):
            params.update({'resources': [params.pop("resources")]})
        return tc.make_request(endpoint=endpoint, method='PUT', data=json.dumps(params))
    except Exception as err:
        logger.error(str(err))
        raise ConnectorError(str(err))


def update_resource_tlp(config: dict, params: dict):
    try:
        tc = ThreatCompass(config)
        params = _build_payload(params)
        endpoint = f'/api/v2/organization/{params.pop("org_id")}/module/{params.pop("module_id")}/{params.pop("module_type")}/resource/{params.pop("resource_id")}/tlpStatus/{params.pop("tlp_status")}'
        return tc.make_request(endpoint=endpoint, method='PUT', data=json.dumps(params))
    except Exception as err:
        logger.error(str(err))
        raise ConnectorError(str(err))


def get_module_labels(config: dict, params: dict):
    try:
        tc = ThreatCompass(config)
        params = _build_payload(params)
        endpoint = f'/api/v2/organization/{params.pop("org_id")}/module/{params.pop("module_id")}/{params.pop("module_type")}/resource/label'
        return tc.make_request(endpoint=endpoint, method='GET', params=params)
    except Exception as err:
        logger.error(str(err))
        raise ConnectorError(str(err))


operations = {
    "get_resource_list": get_resource_list,
    "get_resource_by_id": get_resource_by_id,
    "update_resource_status": update_resource_status,
    "update_resource_label": update_resource_label,
    "update_resource_read_status": update_resource_read_status,
    "update_resource_rating": update_resource_rating,
    "update_resource_fav": update_resource_fav,
    "update_resource_tlp": update_resource_tlp,
    "get_module_labels": get_module_labels
}