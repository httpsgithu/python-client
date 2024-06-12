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
from wavefront_api_client.api.ingestion_spy_api import IngestionSpyApi  # noqa: E501
from wavefront_api_client.rest import ApiException


class TestIngestionSpyApi(unittest.TestCase):
    """IngestionSpyApi unit test stubs"""

    def setUp(self):
        self.api = wavefront_api_client.api.ingestion_spy_api.IngestionSpyApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_spy_on_delta_counters(self):
        """Test case for spy_on_delta_counters

        Gets new delta counters that are added to existing time series.  # noqa: E501
        """
        pass

    def test_spy_on_histograms(self):
        """Test case for spy_on_histograms

        Gets new histograms that are added to existing time series.  # noqa: E501
        """
        pass

    def test_spy_on_id_creations(self):
        """Test case for spy_on_id_creations

        Gets newly allocated IDs that correspond to new metric names, source names, point tags, or span tags. A new ID generally indicates that a new time series has been introduced.  # noqa: E501
        """
        pass

    def test_spy_on_points(self):
        """Test case for spy_on_points

        Gets a sampling of new metric data points that are added to existing time series.  # noqa: E501
        """
        pass

    def test_spy_on_spans(self):
        """Test case for spy_on_spans

        Gets new spans with existing source names and span tags.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
