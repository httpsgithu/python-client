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


class AlertErrorGroupInfo(object):
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
        'error_group_id': 'str',
        'error_group_name': 'str',
        'total_failed': 'int',
        'total_failed_per_group': 'int'
    }

    attribute_map = {
        'error_group_id': 'errorGroupId',
        'error_group_name': 'errorGroupName',
        'total_failed': 'totalFailed',
        'total_failed_per_group': 'totalFailedPerGroup'
    }

    def __init__(self, error_group_id=None, error_group_name=None, total_failed=None, total_failed_per_group=None, _configuration=None):  # noqa: E501
        """AlertErrorGroupInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._error_group_id = None
        self._error_group_name = None
        self._total_failed = None
        self._total_failed_per_group = None
        self.discriminator = None

        if error_group_id is not None:
            self.error_group_id = error_group_id
        if error_group_name is not None:
            self.error_group_name = error_group_name
        if total_failed is not None:
            self.total_failed = total_failed
        if total_failed_per_group is not None:
            self.total_failed_per_group = total_failed_per_group

    @property
    def error_group_id(self):
        """Gets the error_group_id of this AlertErrorGroupInfo.  # noqa: E501


        :return: The error_group_id of this AlertErrorGroupInfo.  # noqa: E501
        :rtype: str
        """
        return self._error_group_id

    @error_group_id.setter
    def error_group_id(self, error_group_id):
        """Sets the error_group_id of this AlertErrorGroupInfo.


        :param error_group_id: The error_group_id of this AlertErrorGroupInfo.  # noqa: E501
        :type: str
        """

        self._error_group_id = error_group_id

    @property
    def error_group_name(self):
        """Gets the error_group_name of this AlertErrorGroupInfo.  # noqa: E501


        :return: The error_group_name of this AlertErrorGroupInfo.  # noqa: E501
        :rtype: str
        """
        return self._error_group_name

    @error_group_name.setter
    def error_group_name(self, error_group_name):
        """Sets the error_group_name of this AlertErrorGroupInfo.


        :param error_group_name: The error_group_name of this AlertErrorGroupInfo.  # noqa: E501
        :type: str
        """

        self._error_group_name = error_group_name

    @property
    def total_failed(self):
        """Gets the total_failed of this AlertErrorGroupInfo.  # noqa: E501


        :return: The total_failed of this AlertErrorGroupInfo.  # noqa: E501
        :rtype: int
        """
        return self._total_failed

    @total_failed.setter
    def total_failed(self, total_failed):
        """Sets the total_failed of this AlertErrorGroupInfo.


        :param total_failed: The total_failed of this AlertErrorGroupInfo.  # noqa: E501
        :type: int
        """

        self._total_failed = total_failed

    @property
    def total_failed_per_group(self):
        """Gets the total_failed_per_group of this AlertErrorGroupInfo.  # noqa: E501


        :return: The total_failed_per_group of this AlertErrorGroupInfo.  # noqa: E501
        :rtype: int
        """
        return self._total_failed_per_group

    @total_failed_per_group.setter
    def total_failed_per_group(self, total_failed_per_group):
        """Sets the total_failed_per_group of this AlertErrorGroupInfo.


        :param total_failed_per_group: The total_failed_per_group of this AlertErrorGroupInfo.  # noqa: E501
        :type: int
        """

        self._total_failed_per_group = total_failed_per_group

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
        if issubclass(AlertErrorGroupInfo, dict):
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
        if not isinstance(other, AlertErrorGroupInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AlertErrorGroupInfo):
            return True

        return self.to_dict() != other.to_dict()
