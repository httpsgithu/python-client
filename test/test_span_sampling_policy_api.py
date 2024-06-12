# coding: utf-8

"""
    Wavefront REST API Documentation

    <p>The REST API enables you to interact with the Wavefront service by using standard REST API tools. You can use the REST API to automate commonly executed operations, for example to tag sources automatically.</p><p>When you make REST API calls outside the REST API documentation UI, to authenticate to the service, you must use an API token associated with a user account or a service account. For information on how to get the API token and examples, see <a href=\"http://docs.wavefront.com/using_wavefront_api.html\">Use the Wavefront REST API.</a></p>  # noqa: E501

    OpenAPI spec version: v2
    Contact: chitimba@wavefront.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import wavefront_api_client
from wavefront_api_client.api.span_sampling_policy_api import SpanSamplingPolicyApi  # noqa: E501
from wavefront_api_client.rest import ApiException


class TestSpanSamplingPolicyApi(unittest.TestCase):
    """SpanSamplingPolicyApi unit test stubs"""

    def setUp(self):
        self.api = wavefront_api_client.api.span_sampling_policy_api.SpanSamplingPolicyApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_span_sampling_policy(self):
        """Test case for create_span_sampling_policy

        Create a span sampling policy  # noqa: E501
        """
        pass

    def test_delete_span_sampling_policy(self):
        """Test case for delete_span_sampling_policy

        Delete a specific span sampling policy  # noqa: E501
        """
        pass

    def test_get_all_deleted_span_sampling_policy(self):
        """Test case for get_all_deleted_span_sampling_policy

        Get all deleted sampling policies for a customer  # noqa: E501
        """
        pass

    def test_get_all_span_sampling_policy(self):
        """Test case for get_all_span_sampling_policy

        Get all sampling policies for a customer  # noqa: E501
        """
        pass

    def test_get_span_sampling_policy(self):
        """Test case for get_span_sampling_policy

        Get a specific span sampling policy  # noqa: E501
        """
        pass

    def test_get_span_sampling_policy_history(self):
        """Test case for get_span_sampling_policy_history

        Get the version history of a specific sampling policy  # noqa: E501
        """
        pass

    def test_get_span_sampling_policy_version(self):
        """Test case for get_span_sampling_policy_version

        Get a specific historical version of a specific sampling policy  # noqa: E501
        """
        pass

    def test_undelete_span_sampling_policy(self):
        """Test case for undelete_span_sampling_policy

        Restore a deleted span sampling policy  # noqa: E501
        """
        pass

    def test_update_span_sampling_policy(self):
        """Test case for update_span_sampling_policy

        Update a specific span sampling policy  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
