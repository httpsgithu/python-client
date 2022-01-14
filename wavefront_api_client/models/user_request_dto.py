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


class UserRequestDTO(object):
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
        'credential': 'str',
        'customer': 'str',
        'groups': 'list[str]',
        'identifier': 'str',
        'ingestion_policies': 'list[str]',
        'ingestion_policy_id': 'str',
        'roles': 'list[str]',
        'sso_id': 'str',
        'user_groups': 'list[str]'
    }

    attribute_map = {
        'credential': 'credential',
        'customer': 'customer',
        'groups': 'groups',
        'identifier': 'identifier',
        'ingestion_policies': 'ingestionPolicies',
        'ingestion_policy_id': 'ingestionPolicyId',
        'roles': 'roles',
        'sso_id': 'ssoId',
        'user_groups': 'userGroups'
    }

    def __init__(self, credential=None, customer=None, groups=None, identifier=None, ingestion_policies=None, ingestion_policy_id=None, roles=None, sso_id=None, user_groups=None, _configuration=None):  # noqa: E501
        """UserRequestDTO - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._credential = None
        self._customer = None
        self._groups = None
        self._identifier = None
        self._ingestion_policies = None
        self._ingestion_policy_id = None
        self._roles = None
        self._sso_id = None
        self._user_groups = None
        self.discriminator = None

        if credential is not None:
            self.credential = credential
        if customer is not None:
            self.customer = customer
        if groups is not None:
            self.groups = groups
        if identifier is not None:
            self.identifier = identifier
        if ingestion_policies is not None:
            self.ingestion_policies = ingestion_policies
        if ingestion_policy_id is not None:
            self.ingestion_policy_id = ingestion_policy_id
        if roles is not None:
            self.roles = roles
        if sso_id is not None:
            self.sso_id = sso_id
        if user_groups is not None:
            self.user_groups = user_groups

    @property
    def credential(self):
        """Gets the credential of this UserRequestDTO.  # noqa: E501


        :return: The credential of this UserRequestDTO.  # noqa: E501
        :rtype: str
        """
        return self._credential

    @credential.setter
    def credential(self, credential):
        """Sets the credential of this UserRequestDTO.


        :param credential: The credential of this UserRequestDTO.  # noqa: E501
        :type: str
        """

        self._credential = credential

    @property
    def customer(self):
        """Gets the customer of this UserRequestDTO.  # noqa: E501


        :return: The customer of this UserRequestDTO.  # noqa: E501
        :rtype: str
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this UserRequestDTO.


        :param customer: The customer of this UserRequestDTO.  # noqa: E501
        :type: str
        """

        self._customer = customer

    @property
    def groups(self):
        """Gets the groups of this UserRequestDTO.  # noqa: E501


        :return: The groups of this UserRequestDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this UserRequestDTO.


        :param groups: The groups of this UserRequestDTO.  # noqa: E501
        :type: list[str]
        """

        self._groups = groups

    @property
    def identifier(self):
        """Gets the identifier of this UserRequestDTO.  # noqa: E501


        :return: The identifier of this UserRequestDTO.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this UserRequestDTO.


        :param identifier: The identifier of this UserRequestDTO.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def ingestion_policies(self):
        """Gets the ingestion_policies of this UserRequestDTO.  # noqa: E501


        :return: The ingestion_policies of this UserRequestDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._ingestion_policies

    @ingestion_policies.setter
    def ingestion_policies(self, ingestion_policies):
        """Sets the ingestion_policies of this UserRequestDTO.


        :param ingestion_policies: The ingestion_policies of this UserRequestDTO.  # noqa: E501
        :type: list[str]
        """

        self._ingestion_policies = ingestion_policies

    @property
    def ingestion_policy_id(self):
        """Gets the ingestion_policy_id of this UserRequestDTO.  # noqa: E501


        :return: The ingestion_policy_id of this UserRequestDTO.  # noqa: E501
        :rtype: str
        """
        return self._ingestion_policy_id

    @ingestion_policy_id.setter
    def ingestion_policy_id(self, ingestion_policy_id):
        """Sets the ingestion_policy_id of this UserRequestDTO.


        :param ingestion_policy_id: The ingestion_policy_id of this UserRequestDTO.  # noqa: E501
        :type: str
        """

        self._ingestion_policy_id = ingestion_policy_id

    @property
    def roles(self):
        """Gets the roles of this UserRequestDTO.  # noqa: E501


        :return: The roles of this UserRequestDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this UserRequestDTO.


        :param roles: The roles of this UserRequestDTO.  # noqa: E501
        :type: list[str]
        """

        self._roles = roles

    @property
    def sso_id(self):
        """Gets the sso_id of this UserRequestDTO.  # noqa: E501


        :return: The sso_id of this UserRequestDTO.  # noqa: E501
        :rtype: str
        """
        return self._sso_id

    @sso_id.setter
    def sso_id(self, sso_id):
        """Sets the sso_id of this UserRequestDTO.


        :param sso_id: The sso_id of this UserRequestDTO.  # noqa: E501
        :type: str
        """

        self._sso_id = sso_id

    @property
    def user_groups(self):
        """Gets the user_groups of this UserRequestDTO.  # noqa: E501


        :return: The user_groups of this UserRequestDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._user_groups

    @user_groups.setter
    def user_groups(self, user_groups):
        """Sets the user_groups of this UserRequestDTO.


        :param user_groups: The user_groups of this UserRequestDTO.  # noqa: E501
        :type: list[str]
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
        if issubclass(UserRequestDTO, dict):
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
        if not isinstance(other, UserRequestDTO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserRequestDTO):
            return True

        return self.to_dict() != other.to_dict()
