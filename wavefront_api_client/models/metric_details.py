# coding: utf-8

"""
    Wavefront REST API Documentation

    <p>The Wavefront REST API enables you to interact with Wavefront servers using standard REST API tools. You can use the REST API to automate commonly executed operations such as automatically tagging sources.</p><p>When you make REST API calls outside the Wavefront REST API documentation you must add the header \"Authorization: Bearer &lt;&lt;API-TOKEN&gt;&gt;\" to your HTTP requests.</p>  # noqa: E501

    OpenAPI spec version: v2
    Contact: chitimba@wavefront.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from wavefront_api_client.configuration import Configuration


class MetricDetails(object):
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
        'host': 'str',
        'last_update': 'int',
        'tags': 'dict(str, str)'
    }

    attribute_map = {
        'host': 'host',
        'last_update': 'last_update',
        'tags': 'tags'
    }

    def __init__(self, host=None, last_update=None, tags=None, _configuration=None):  # noqa: E501
        """MetricDetails - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._host = None
        self._last_update = None
        self._tags = None
        self.discriminator = None

        if host is not None:
            self.host = host
        if last_update is not None:
            self.last_update = last_update
        if tags is not None:
            self.tags = tags

    @property
    def host(self):
        """Gets the host of this MetricDetails.  # noqa: E501

        The source reporting this metric  # noqa: E501

        :return: The host of this MetricDetails.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this MetricDetails.

        The source reporting this metric  # noqa: E501

        :param host: The host of this MetricDetails.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def last_update(self):
        """Gets the last_update of this MetricDetails.  # noqa: E501

        Approximate time of last reporting, in milliseconds since the Unix epoch  # noqa: E501

        :return: The last_update of this MetricDetails.  # noqa: E501
        :rtype: int
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        """Sets the last_update of this MetricDetails.

        Approximate time of last reporting, in milliseconds since the Unix epoch  # noqa: E501

        :param last_update: The last_update of this MetricDetails.  # noqa: E501
        :type: int
        """

        self._last_update = last_update

    @property
    def tags(self):
        """Gets the tags of this MetricDetails.  # noqa: E501

        A key-value map of the point tags associated with this source  # noqa: E501

        :return: The tags of this MetricDetails.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this MetricDetails.

        A key-value map of the point tags associated with this source  # noqa: E501

        :param tags: The tags of this MetricDetails.  # noqa: E501
        :type: dict(str, str)
        """

        self._tags = tags

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
        if issubclass(MetricDetails, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MetricDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MetricDetails):
            return True

        return self.to_dict() != other.to_dict()
