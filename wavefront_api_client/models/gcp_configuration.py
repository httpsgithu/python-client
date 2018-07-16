# coding: utf-8

"""
    Wavefront Public API

    <p>The Wavefront public API enables you to interact with Wavefront servers using standard web service API tools. You can use the API to automate commonly executed operations such as automatically tagging sources.</p><p>When you make API calls outside the Wavefront API documentation you must add the header \"Authorization: Bearer &lt;&lt;API-TOKEN&gt;&gt;\" to your HTTP requests.</p><p>For legacy versions of the Wavefront API, see the <a href=\"/api-docs/ui/deprecated\">legacy API documentation</a>.</p>  # noqa: E501

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GCPConfiguration(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'gcp_json_key': 'str',
        'project_id': 'str',
        'metric_filter_regex': 'str',
        'categories_to_fetch': 'list[str]'
    }

    attribute_map = {
        'gcp_json_key': 'gcpJsonKey',
        'project_id': 'projectId',
        'metric_filter_regex': 'metricFilterRegex',
        'categories_to_fetch': 'categoriesToFetch'
    }

    def __init__(self, gcp_json_key=None, project_id=None, metric_filter_regex=None, categories_to_fetch=None):  # noqa: E501
        """GCPConfiguration - a model defined in Swagger"""  # noqa: E501

        self._gcp_json_key = None
        self._project_id = None
        self._metric_filter_regex = None
        self._categories_to_fetch = None
        self.discriminator = None

        self.gcp_json_key = gcp_json_key
        self.project_id = project_id
        if metric_filter_regex is not None:
            self.metric_filter_regex = metric_filter_regex
        if categories_to_fetch is not None:
            self.categories_to_fetch = categories_to_fetch

    @property
    def gcp_json_key(self):
        """Gets the gcp_json_key of this GCPConfiguration.  # noqa: E501

        Private key for a Google Cloud Platform (GCP) service account within your project.  The account must at least be granted Monitoring Viewer permissions.  This key must be in the JSON format generated by GCP.  # noqa: E501

        :return: The gcp_json_key of this GCPConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._gcp_json_key

    @gcp_json_key.setter
    def gcp_json_key(self, gcp_json_key):
        """Sets the gcp_json_key of this GCPConfiguration.

        Private key for a Google Cloud Platform (GCP) service account within your project.  The account must at least be granted Monitoring Viewer permissions.  This key must be in the JSON format generated by GCP.  # noqa: E501

        :param gcp_json_key: The gcp_json_key of this GCPConfiguration.  # noqa: E501
        :type: str
        """
        if gcp_json_key is None:
            raise ValueError("Invalid value for `gcp_json_key`, must not be `None`")  # noqa: E501

        self._gcp_json_key = gcp_json_key

    @property
    def project_id(self):
        """Gets the project_id of this GCPConfiguration.  # noqa: E501

        The Google Cloud Platform (GCP) project id.  # noqa: E501

        :return: The project_id of this GCPConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this GCPConfiguration.

        The Google Cloud Platform (GCP) project id.  # noqa: E501

        :param project_id: The project_id of this GCPConfiguration.  # noqa: E501
        :type: str
        """
        if project_id is None:
            raise ValueError("Invalid value for `project_id`, must not be `None`")  # noqa: E501

        self._project_id = project_id

    @property
    def metric_filter_regex(self):
        """Gets the metric_filter_regex of this GCPConfiguration.  # noqa: E501

        A regular expression that a metric name must match (case-insensitively) in order to be ingested  # noqa: E501

        :return: The metric_filter_regex of this GCPConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._metric_filter_regex

    @metric_filter_regex.setter
    def metric_filter_regex(self, metric_filter_regex):
        """Sets the metric_filter_regex of this GCPConfiguration.

        A regular expression that a metric name must match (case-insensitively) in order to be ingested  # noqa: E501

        :param metric_filter_regex: The metric_filter_regex of this GCPConfiguration.  # noqa: E501
        :type: str
        """

        self._metric_filter_regex = metric_filter_regex

    @property
    def categories_to_fetch(self):
        """Gets the categories_to_fetch of this GCPConfiguration.  # noqa: E501

        A list of Google Cloud Platform (GCP) services (such as ComputeEngine, PubSub, etc) from which to pull metrics.  Allowable values are APPENGINE, BIGQUERY, BIGTABLE, CLOUDFUNCTIONS, CLOUDIOT, CLOUDSQL, CLOUDTASKS, COMPUTE, CONTAINER, DATAFLOW, DATASTORE, FIREBASEDATABASE, FIREBASEHOSTING, LOGGING, ML, PUBSUB, ROUTER, SPANNER, STORAGE, VPN  # noqa: E501

        :return: The categories_to_fetch of this GCPConfiguration.  # noqa: E501
        :rtype: list[str]
        """
        return self._categories_to_fetch

    @categories_to_fetch.setter
    def categories_to_fetch(self, categories_to_fetch):
        """Sets the categories_to_fetch of this GCPConfiguration.

        A list of Google Cloud Platform (GCP) services (such as ComputeEngine, PubSub, etc) from which to pull metrics.  Allowable values are APPENGINE, BIGQUERY, BIGTABLE, CLOUDFUNCTIONS, CLOUDIOT, CLOUDSQL, CLOUDTASKS, COMPUTE, CONTAINER, DATAFLOW, DATASTORE, FIREBASEDATABASE, FIREBASEHOSTING, LOGGING, ML, PUBSUB, ROUTER, SPANNER, STORAGE, VPN  # noqa: E501

        :param categories_to_fetch: The categories_to_fetch of this GCPConfiguration.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["APPENGINE", "BIGQUERY", "BIGTABLE", "CLOUDFUNCTIONS", "CLOUDIOT", "CLOUDSQL", "CLOUDTASKS", "COMPUTE", "CONTAINER", "DATAFLOW", "DATASTORE", "FIREBASEDATABASE", "FIREBASEHOSTING", "LOGGING", "ML", "PUBSUB", "ROUTER", "SPANNER", "STORAGE", "VPN"]  # noqa: E501
        if not set(categories_to_fetch).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `categories_to_fetch` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(categories_to_fetch) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._categories_to_fetch = categories_to_fetch

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GCPConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other