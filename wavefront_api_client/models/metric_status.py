# coding: utf-8

"""
    Wavefront REST API Documentation

    <p>The REST API enables you to interact with the Wavefront service by using standard REST API tools. You can use the REST API to automate commonly executed operations, for example to tag sources automatically.</p><p>When you make REST API calls outside the REST API documentation UI, to authenticate to the service, you must use an API token associated with a user account or a service account. For information on how to get the API token and examples, see <a href=\"http://docs.wavefront.com/using_wavefront_api.html\">Use the Wavefront REST API.</a></p>  # noqa: E501

    OpenAPI spec version: v2
    Contact: chitimba@wavefront.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from wavefront_api_client.configuration import Configuration


class MetricStatus(object):
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
        'ever': 'bool',
        'now': 'bool',
        'recent_except_now': 'bool',
        'status': 'str'
    }

    attribute_map = {
        'ever': 'ever',
        'now': 'now',
        'recent_except_now': 'recentExceptNow',
        'status': 'status'
    }

    def __init__(self, ever=None, now=None, recent_except_now=None, status=None, _configuration=None):  # noqa: E501
        """MetricStatus - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ever = None
        self._now = None
        self._recent_except_now = None
        self._status = None
        self.discriminator = None

        if ever is not None:
            self.ever = ever
        if now is not None:
            self.now = now
        if recent_except_now is not None:
            self.recent_except_now = recent_except_now
        if status is not None:
            self.status = status

    @property
    def ever(self):
        """Gets the ever of this MetricStatus.  # noqa: E501


        :return: The ever of this MetricStatus.  # noqa: E501
        :rtype: bool
        """
        return self._ever

    @ever.setter
    def ever(self, ever):
        """Sets the ever of this MetricStatus.


        :param ever: The ever of this MetricStatus.  # noqa: E501
        :type: bool
        """

        self._ever = ever

    @property
    def now(self):
        """Gets the now of this MetricStatus.  # noqa: E501


        :return: The now of this MetricStatus.  # noqa: E501
        :rtype: bool
        """
        return self._now

    @now.setter
    def now(self, now):
        """Sets the now of this MetricStatus.


        :param now: The now of this MetricStatus.  # noqa: E501
        :type: bool
        """

        self._now = now

    @property
    def recent_except_now(self):
        """Gets the recent_except_now of this MetricStatus.  # noqa: E501


        :return: The recent_except_now of this MetricStatus.  # noqa: E501
        :rtype: bool
        """
        return self._recent_except_now

    @recent_except_now.setter
    def recent_except_now(self, recent_except_now):
        """Sets the recent_except_now of this MetricStatus.


        :param recent_except_now: The recent_except_now of this MetricStatus.  # noqa: E501
        :type: bool
        """

        self._recent_except_now = recent_except_now

    @property
    def status(self):
        """Gets the status of this MetricStatus.  # noqa: E501


        :return: The status of this MetricStatus.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MetricStatus.


        :param status: The status of this MetricStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["OK", "PENDING"]  # noqa: E501
        if (self._configuration.client_side_validation and
                status not in allowed_values):
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

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
        if issubclass(MetricStatus, dict):
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
        if not isinstance(other, MetricStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MetricStatus):
            return True

        return self.to_dict() != other.to_dict()
