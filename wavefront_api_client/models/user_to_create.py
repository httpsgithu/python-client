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


class UserToCreate(object):
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
        'email_address': 'str',
        'groups': 'list[str]',
        'ingestion_policies': 'list[str]',
        'ingestion_policy_id': 'str',
        'roles': 'list[str]',
        'user_groups': 'list[str]'
    }

    attribute_map = {
        'email_address': 'emailAddress',
        'groups': 'groups',
        'ingestion_policies': 'ingestionPolicies',
        'ingestion_policy_id': 'ingestionPolicyId',
        'roles': 'roles',
        'user_groups': 'userGroups'
    }

    def __init__(self, email_address=None, groups=None, ingestion_policies=None, ingestion_policy_id=None, roles=None, user_groups=None, _configuration=None):  # noqa: E501
        """UserToCreate - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._email_address = None
        self._groups = None
        self._ingestion_policies = None
        self._ingestion_policy_id = None
        self._roles = None
        self._user_groups = None
        self.discriminator = None

        self.email_address = email_address
        self.groups = groups
        if ingestion_policies is not None:
            self.ingestion_policies = ingestion_policies
        if ingestion_policy_id is not None:
            self.ingestion_policy_id = ingestion_policy_id
        if roles is not None:
            self.roles = roles
        self.user_groups = user_groups

    @property
    def email_address(self):
        """Gets the email_address of this UserToCreate.  # noqa: E501

        The (unique) identifier of the user to create. Must be a valid email address  # noqa: E501

        :return: The email_address of this UserToCreate.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this UserToCreate.

        The (unique) identifier of the user to create. Must be a valid email address  # noqa: E501

        :param email_address: The email_address of this UserToCreate.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and email_address is None:
            raise ValueError("Invalid value for `email_address`, must not be `None`")  # noqa: E501

        self._email_address = email_address

    @property
    def groups(self):
        """Gets the groups of this UserToCreate.  # noqa: E501

        List of permission groups to grant to this user. Please note that 'host_tag_management' is the equivalent of the 'Source Tag Management' permission.  Possible values are agent_management, alerts_management, dashboard_management, embedded_charts, events_management, external_links_management, host_tag_management, metrics_management, user_management  # noqa: E501

        :return: The groups of this UserToCreate.  # noqa: E501
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this UserToCreate.

        List of permission groups to grant to this user. Please note that 'host_tag_management' is the equivalent of the 'Source Tag Management' permission.  Possible values are agent_management, alerts_management, dashboard_management, embedded_charts, events_management, external_links_management, host_tag_management, metrics_management, user_management  # noqa: E501

        :param groups: The groups of this UserToCreate.  # noqa: E501
        :type: list[str]
        """
        if self._configuration.client_side_validation and groups is None:
            raise ValueError("Invalid value for `groups`, must not be `None`")  # noqa: E501

        self._groups = groups

    @property
    def ingestion_policies(self):
        """Gets the ingestion_policies of this UserToCreate.  # noqa: E501

        The list of ingestion policy ids, the user will be added to.  # noqa: E501

        :return: The ingestion_policies of this UserToCreate.  # noqa: E501
        :rtype: list[str]
        """
        return self._ingestion_policies

    @ingestion_policies.setter
    def ingestion_policies(self, ingestion_policies):
        """Sets the ingestion_policies of this UserToCreate.

        The list of ingestion policy ids, the user will be added to.  # noqa: E501

        :param ingestion_policies: The ingestion_policies of this UserToCreate.  # noqa: E501
        :type: list[str]
        """

        self._ingestion_policies = ingestion_policies

    @property
    def ingestion_policy_id(self):
        """Gets the ingestion_policy_id of this UserToCreate.  # noqa: E501

        The identifier of the ingestion policy linked with user.  # noqa: E501

        :return: The ingestion_policy_id of this UserToCreate.  # noqa: E501
        :rtype: str
        """
        return self._ingestion_policy_id

    @ingestion_policy_id.setter
    def ingestion_policy_id(self, ingestion_policy_id):
        """Sets the ingestion_policy_id of this UserToCreate.

        The identifier of the ingestion policy linked with user.  # noqa: E501

        :param ingestion_policy_id: The ingestion_policy_id of this UserToCreate.  # noqa: E501
        :type: str
        """

        self._ingestion_policy_id = ingestion_policy_id

    @property
    def roles(self):
        """Gets the roles of this UserToCreate.  # noqa: E501

        The list of role ids, the user will be added to.  # noqa: E501

        :return: The roles of this UserToCreate.  # noqa: E501
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this UserToCreate.

        The list of role ids, the user will be added to.  # noqa: E501

        :param roles: The roles of this UserToCreate.  # noqa: E501
        :type: list[str]
        """

        self._roles = roles

    @property
    def user_groups(self):
        """Gets the user_groups of this UserToCreate.  # noqa: E501

        List of user groups to this user.   # noqa: E501

        :return: The user_groups of this UserToCreate.  # noqa: E501
        :rtype: list[str]
        """
        return self._user_groups

    @user_groups.setter
    def user_groups(self, user_groups):
        """Sets the user_groups of this UserToCreate.

        List of user groups to this user.   # noqa: E501

        :param user_groups: The user_groups of this UserToCreate.  # noqa: E501
        :type: list[str]
        """
        if self._configuration.client_side_validation and user_groups is None:
            raise ValueError("Invalid value for `user_groups`, must not be `None`")  # noqa: E501

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
        if issubclass(UserToCreate, dict):
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
        if not isinstance(other, UserToCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserToCreate):
            return True

        return self.to_dict() != other.to_dict()
