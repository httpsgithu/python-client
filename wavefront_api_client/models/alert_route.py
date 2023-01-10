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


class AlertRoute(object):
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
        'filter': 'str',
        'method': 'str',
        'target': 'str'
    }

    attribute_map = {
        'filter': 'filter',
        'method': 'method',
        'target': 'target'
    }

    def __init__(self, filter=None, method=None, target=None, _configuration=None):  # noqa: E501
        """AlertRoute - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._filter = None
        self._method = None
        self._target = None
        self.discriminator = None

        self.filter = filter
        self.method = method
        self.target = target

    @property
    def filter(self):
        """Gets the filter of this AlertRoute.  # noqa: E501

        String that filters the route. Space delimited. Currently only allows single key value pair.  filter: env* prod*  # noqa: E501

        :return: The filter of this AlertRoute.  # noqa: E501
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this AlertRoute.

        String that filters the route. Space delimited. Currently only allows single key value pair.  filter: env* prod*  # noqa: E501

        :param filter: The filter of this AlertRoute.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and filter is None:
            raise ValueError("Invalid value for `filter`, must not be `None`")  # noqa: E501

        self._filter = filter

    @property
    def method(self):
        """Gets the method of this AlertRoute.  # noqa: E501

        The end point for the alert route.EMAIL: email address.  PAGERDUTY: PagerDuty routing Key.  WEBHOOK: URL end point  # noqa: E501

        :return: The method of this AlertRoute.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this AlertRoute.

        The end point for the alert route.EMAIL: email address.  PAGERDUTY: PagerDuty routing Key.  WEBHOOK: URL end point  # noqa: E501

        :param method: The method of this AlertRoute.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and method is None:
            raise ValueError("Invalid value for `method`, must not be `None`")  # noqa: E501
        allowed_values = ["WEBHOOK", "PAGERDUTY", "EMAIL"]  # noqa: E501
        if (self._configuration.client_side_validation and
                method not in allowed_values):
            raise ValueError(
                "Invalid value for `method` ({0}), must be one of {1}"  # noqa: E501
                .format(method, allowed_values)
            )

        self._method = method

    @property
    def target(self):
        """Gets the target of this AlertRoute.  # noqa: E501

        The end point for the notification target.EMAIL: email address.  PAGERDUTY: PagerDuty routing Key.  WEBHOOK: URL end point  # noqa: E501

        :return: The target of this AlertRoute.  # noqa: E501
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this AlertRoute.

        The end point for the notification target.EMAIL: email address.  PAGERDUTY: PagerDuty routing Key.  WEBHOOK: URL end point  # noqa: E501

        :param target: The target of this AlertRoute.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and target is None:
            raise ValueError("Invalid value for `target`, must not be `None`")  # noqa: E501

        self._target = target

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
        if issubclass(AlertRoute, dict):
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
        if not isinstance(other, AlertRoute):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AlertRoute):
            return True

        return self.to_dict() != other.to_dict()
