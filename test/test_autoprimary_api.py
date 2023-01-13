# coding: utf-8

"""
    PowerDNS Authoritative HTTP API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.15
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import powerdns_client
from powerdns_client.api.autoprimary_api import AutoprimaryApi  # noqa: E501
from powerdns_client.rest import ApiException


class TestAutoprimaryApi(unittest.TestCase):
    """AutoprimaryApi unit test stubs"""

    def setUp(self):
        self.api = AutoprimaryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_autoprimary(self):
        """Test case for create_autoprimary

        Add an autoprimary  # noqa: E501
        """
        pass

    def test_delete_autoprimary(self):
        """Test case for delete_autoprimary

        Delete the autoprimary entry  # noqa: E501
        """
        pass

    def test_get_autoprimaries(self):
        """Test case for get_autoprimaries

        Get a list of autoprimaries  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
