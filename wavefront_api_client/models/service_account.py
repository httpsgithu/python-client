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

from wavefront_api_client.models.user_api_token import UserApiToken  # noqa: F401,E501
from wavefront_api_client.models.user_group import UserGroup  # noqa: F401,E501


class ServiceAccount(object):
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
        'active': 'bool',
        'description': 'str',
        'groups': 'list[str]',
        'identifier': 'str',
        'last_used': 'int',
        'tokens': 'list[UserApiToken]',
        'user_groups': 'list[UserGroup]'
    }

    attribute_map = {
        'active': 'active',
        'description': 'description',
        'groups': 'groups',
        'identifier': 'identifier',
        'last_used': 'lastUsed',
        'tokens': 'tokens',
        'user_groups': 'userGroups'
    }

    def __init__(self, active=None, description=None, groups=None, identifier=None, last_used=None, tokens=None, user_groups=None):  # noqa: E501
        """ServiceAccount - a model defined in Swagger"""  # noqa: E501

        self._active = None
        self._description = None
        self._groups = None
        self._identifier = None
        self._last_used = None
        self._tokens = None
        self._user_groups = None
        self.discriminator = None

        self.active = active
        if description is not None:
            self.description = description
        if groups is not None:
            self.groups = groups
        self.identifier = identifier
        if last_used is not None:
            self.last_used = last_used
        if tokens is not None:
            self.tokens = tokens
        if user_groups is not None:
            self.user_groups = user_groups

    @property
    def active(self):
        """Gets the active of this ServiceAccount.  # noqa: E501

        The state of the service account.  # noqa: E501

        :return: The active of this ServiceAccount.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this ServiceAccount.

        The state of the service account.  # noqa: E501

        :param active: The active of this ServiceAccount.  # noqa: E501
        :type: bool
        """
        if active is None:
            raise ValueError("Invalid value for `active`, must not be `None`")  # noqa: E501

        self._active = active

    @property
    def description(self):
        """Gets the description of this ServiceAccount.  # noqa: E501

        The description of the service account.  # noqa: E501

        :return: The description of this ServiceAccount.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ServiceAccount.

        The description of the service account.  # noqa: E501

        :param description: The description of this ServiceAccount.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def groups(self):
        """Gets the groups of this ServiceAccount.  # noqa: E501

        The list of service account's permissions.  # noqa: E501

        :return: The groups of this ServiceAccount.  # noqa: E501
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this ServiceAccount.

        The list of service account's permissions.  # noqa: E501

        :param groups: The groups of this ServiceAccount.  # noqa: E501
        :type: list[str]
        """

        self._groups = groups

    @property
    def identifier(self):
        """Gets the identifier of this ServiceAccount.  # noqa: E501

        The unique identifier of a service account.  # noqa: E501

        :return: The identifier of this ServiceAccount.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this ServiceAccount.

        The unique identifier of a service account.  # noqa: E501

        :param identifier: The identifier of this ServiceAccount.  # noqa: E501
        :type: str
        """
        if identifier is None:
            raise ValueError("Invalid value for `identifier`, must not be `None`")  # noqa: E501

        self._identifier = identifier

    @property
    def last_used(self):
        """Gets the last_used of this ServiceAccount.  # noqa: E501

        The last time when a token of the service account was used.  # noqa: E501

        :return: The last_used of this ServiceAccount.  # noqa: E501
        :rtype: int
        """
        return self._last_used

    @last_used.setter
    def last_used(self, last_used):
        """Sets the last_used of this ServiceAccount.

        The last time when a token of the service account was used.  # noqa: E501

        :param last_used: The last_used of this ServiceAccount.  # noqa: E501
        :type: int
        """

        self._last_used = last_used

    @property
    def tokens(self):
        """Gets the tokens of this ServiceAccount.  # noqa: E501

        The service account's API tokens.  # noqa: E501

        :return: The tokens of this ServiceAccount.  # noqa: E501
        :rtype: list[UserApiToken]
        """
        return self._tokens

    @tokens.setter
    def tokens(self, tokens):
        """Sets the tokens of this ServiceAccount.

        The service account's API tokens.  # noqa: E501

        :param tokens: The tokens of this ServiceAccount.  # noqa: E501
        :type: list[UserApiToken]
        """

        self._tokens = tokens

    @property
    def user_groups(self):
        """Gets the user_groups of this ServiceAccount.  # noqa: E501

        The list of service account's user groups.  # noqa: E501

        :return: The user_groups of this ServiceAccount.  # noqa: E501
        :rtype: list[UserGroup]
        """
        return self._user_groups

    @user_groups.setter
    def user_groups(self, user_groups):
        """Sets the user_groups of this ServiceAccount.

        The list of service account's user groups.  # noqa: E501

        :param user_groups: The user_groups of this ServiceAccount.  # noqa: E501
        :type: list[UserGroup]
        """

        self._user_groups = user_groups

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
        if issubclass(ServiceAccount, dict):
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
        if not isinstance(other, ServiceAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other