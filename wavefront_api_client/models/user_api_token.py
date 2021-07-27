# coding: utf-8

"""
    Wavefront REST API

    <p>The Wavefront REST API enables you to interact with Wavefront servers using standard REST API tools. You can use the REST API to automate commonly executed operations such as automatically tagging sources.</p><p>When you make REST API calls outside the Wavefront REST API documentation you must add the header \"Authorization: Bearer &lt;&lt;API-TOKEN&gt;&gt;\" to your HTTP requests.</p>  # noqa: E501

    OpenAPI spec version: v2
    Contact: chitimba@wavefront.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from wavefront_api_client.configuration import Configuration


class UserApiToken(object):
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
        'last_used': 'int',
        'token_id': 'str',
        'token_name': 'str'
    }

    attribute_map = {
        'last_used': 'lastUsed',
        'token_id': 'tokenID',
        'token_name': 'tokenName'
    }

    def __init__(self, last_used=None, token_id=None, token_name=None, _configuration=None):  # noqa: E501
        """UserApiToken - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._last_used = None
        self._token_id = None
        self._token_name = None
        self.discriminator = None

        if last_used is not None:
            self.last_used = last_used
        self.token_id = token_id
        if token_name is not None:
            self.token_name = token_name

    @property
    def last_used(self):
        """Gets the last_used of this UserApiToken.  # noqa: E501

        The last time this token was used  # noqa: E501

        :return: The last_used of this UserApiToken.  # noqa: E501
        :rtype: int
        """
        return self._last_used

    @last_used.setter
    def last_used(self, last_used):
        """Sets the last_used of this UserApiToken.

        The last time this token was used  # noqa: E501

        :param last_used: The last_used of this UserApiToken.  # noqa: E501
        :type: int
        """

        self._last_used = last_used

    @property
    def token_id(self):
        """Gets the token_id of this UserApiToken.  # noqa: E501

        The identifier of the user API token  # noqa: E501

        :return: The token_id of this UserApiToken.  # noqa: E501
        :rtype: str
        """
        return self._token_id

    @token_id.setter
    def token_id(self, token_id):
        """Sets the token_id of this UserApiToken.

        The identifier of the user API token  # noqa: E501

        :param token_id: The token_id of this UserApiToken.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and token_id is None:
            raise ValueError("Invalid value for `token_id`, must not be `None`")  # noqa: E501

        self._token_id = token_id

    @property
    def token_name(self):
        """Gets the token_name of this UserApiToken.  # noqa: E501

        The name of the user API token  # noqa: E501

        :return: The token_name of this UserApiToken.  # noqa: E501
        :rtype: str
        """
        return self._token_name

    @token_name.setter
    def token_name(self, token_name):
        """Sets the token_name of this UserApiToken.

        The name of the user API token  # noqa: E501

        :param token_name: The token_name of this UserApiToken.  # noqa: E501
        :type: str
        """

        self._token_name = token_name

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
        if issubclass(UserApiToken, dict):
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
        if not isinstance(other, UserApiToken):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserApiToken):
            return True

        return self.to_dict() != other.to_dict()
