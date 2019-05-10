# coding: utf-8

"""
    Wavefront REST API

    <p>The Wavefront REST API enables you to interact with Wavefront servers using standard REST API tools. You can use the REST API to automate commonly executed operations such as automatically tagging sources.</p><p>When you make REST API calls outside the Wavefront REST API documentation you must add the header \"Authorization: Bearer &lt;&lt;API-TOKEN&gt;&gt;\" to your HTTP requests.</p>  # noqa: E501

    OpenAPI spec version: v2
    Contact: chitimba@wavefront.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import wavefront_api_client
from wavefront_api_client.api.external_link_api import ExternalLinkApi  # noqa: E501
from wavefront_api_client.rest import ApiException


class TestExternalLinkApi(unittest.TestCase):
    """ExternalLinkApi unit test stubs"""

    def setUp(self):
        self.api = wavefront_api_client.api.external_link_api.ExternalLinkApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_external_link(self):
        """Test case for create_external_link

        Create a specific external link  # noqa: E501
        """
        pass

    def test_delete_external_link(self):
        """Test case for delete_external_link

        Delete a specific external link  # noqa: E501
        """
        pass

    def test_get_all_external_link(self):
        """Test case for get_all_external_link

        Get all external links for a customer  # noqa: E501
        """
        pass

    def test_get_external_link(self):
        """Test case for get_external_link

        Get a specific external link  # noqa: E501
        """
        pass

    def test_update_external_link(self):
        """Test case for update_external_link

        Update a specific external link  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()