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


class ValidatedUsersDTO(object):
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
        'invalid_identifiers': 'list[str]',
        'valid_users': 'list[UserDTO]'
    }

    attribute_map = {
        'invalid_identifiers': 'invalidIdentifiers',
        'valid_users': 'validUsers'
    }

    def __init__(self, invalid_identifiers=None, valid_users=None, _configuration=None):  # noqa: E501
        """ValidatedUsersDTO - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._invalid_identifiers = None
        self._valid_users = None
        self.discriminator = None

        if invalid_identifiers is not None:
            self.invalid_identifiers = invalid_identifiers
        if valid_users is not None:
            self.valid_users = valid_users

    @property
    def invalid_identifiers(self):
        """Gets the invalid_identifiers of this ValidatedUsersDTO.  # noqa: E501


        :return: The invalid_identifiers of this ValidatedUsersDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._invalid_identifiers

    @invalid_identifiers.setter
    def invalid_identifiers(self, invalid_identifiers):
        """Sets the invalid_identifiers of this ValidatedUsersDTO.


        :param invalid_identifiers: The invalid_identifiers of this ValidatedUsersDTO.  # noqa: E501
        :type: list[str]
        """

        self._invalid_identifiers = invalid_identifiers

    @property
    def valid_users(self):
        """Gets the valid_users of this ValidatedUsersDTO.  # noqa: E501


        :return: The valid_users of this ValidatedUsersDTO.  # noqa: E501
        :rtype: list[UserDTO]
        """
        return self._valid_users

    @valid_users.setter
    def valid_users(self, valid_users):
        """Sets the valid_users of this ValidatedUsersDTO.


        :param valid_users: The valid_users of this ValidatedUsersDTO.  # noqa: E501
        :type: list[UserDTO]
        """

        self._valid_users = valid_users

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
        if issubclass(ValidatedUsersDTO, dict):
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
        if not isinstance(other, ValidatedUsersDTO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ValidatedUsersDTO):
            return True

        return self.to_dict() != other.to_dict()
