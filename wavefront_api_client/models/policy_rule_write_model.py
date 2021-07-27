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


class PolicyRuleWriteModel(object):
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
        'access_type': 'str',
        'accounts': 'list[str]',
        'description': 'str',
        'id': 'str',
        'name': 'str',
        'prefixes': 'list[str]',
        'roles': 'list[str]',
        'tags': 'list[Annotation]',
        'tags_anded': 'bool',
        'user_groups': 'list[str]'
    }

    attribute_map = {
        'access_type': 'accessType',
        'accounts': 'accounts',
        'description': 'description',
        'id': 'id',
        'name': 'name',
        'prefixes': 'prefixes',
        'roles': 'roles',
        'tags': 'tags',
        'tags_anded': 'tagsAnded',
        'user_groups': 'userGroups'
    }

    def __init__(self, access_type=None, accounts=None, description=None, id=None, name=None, prefixes=None, roles=None, tags=None, tags_anded=None, user_groups=None, _configuration=None):  # noqa: E501
        """PolicyRuleWriteModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._access_type = None
        self._accounts = None
        self._description = None
        self._id = None
        self._name = None
        self._prefixes = None
        self._roles = None
        self._tags = None
        self._tags_anded = None
        self._user_groups = None
        self.discriminator = None

        if access_type is not None:
            self.access_type = access_type
        if accounts is not None:
            self.accounts = accounts
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        self.name = name
        if prefixes is not None:
            self.prefixes = prefixes
        if roles is not None:
            self.roles = roles
        if tags is not None:
            self.tags = tags
        if tags_anded is not None:
            self.tags_anded = tags_anded
        if user_groups is not None:
            self.user_groups = user_groups

    @property
    def access_type(self):
        """Gets the access_type of this PolicyRuleWriteModel.  # noqa: E501

        The access type of the policy rule  # noqa: E501

        :return: The access_type of this PolicyRuleWriteModel.  # noqa: E501
        :rtype: str
        """
        return self._access_type

    @access_type.setter
    def access_type(self, access_type):
        """Sets the access_type of this PolicyRuleWriteModel.

        The access type of the policy rule  # noqa: E501

        :param access_type: The access_type of this PolicyRuleWriteModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["ALLOW", "BLOCK"]  # noqa: E501
        if (self._configuration.client_side_validation and
                access_type not in allowed_values):
            raise ValueError(
                "Invalid value for `access_type` ({0}), must be one of {1}"  # noqa: E501
                .format(access_type, allowed_values)
            )

        self._access_type = access_type

    @property
    def accounts(self):
        """Gets the accounts of this PolicyRuleWriteModel.  # noqa: E501

        The list of account identifiers of the policy rule  # noqa: E501

        :return: The accounts of this PolicyRuleWriteModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this PolicyRuleWriteModel.

        The list of account identifiers of the policy rule  # noqa: E501

        :param accounts: The accounts of this PolicyRuleWriteModel.  # noqa: E501
        :type: list[str]
        """

        self._accounts = accounts

    @property
    def description(self):
        """Gets the description of this PolicyRuleWriteModel.  # noqa: E501

        The description of the policy rule  # noqa: E501

        :return: The description of this PolicyRuleWriteModel.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PolicyRuleWriteModel.

        The description of the policy rule  # noqa: E501

        :param description: The description of this PolicyRuleWriteModel.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this PolicyRuleWriteModel.  # noqa: E501


        :return: The id of this PolicyRuleWriteModel.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PolicyRuleWriteModel.


        :param id: The id of this PolicyRuleWriteModel.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this PolicyRuleWriteModel.  # noqa: E501

        The name of the policy rule  # noqa: E501

        :return: The name of this PolicyRuleWriteModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PolicyRuleWriteModel.

        The name of the policy rule  # noqa: E501

        :param name: The name of this PolicyRuleWriteModel.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def prefixes(self):
        """Gets the prefixes of this PolicyRuleWriteModel.  # noqa: E501

        The prefixes of the policy rule  # noqa: E501

        :return: The prefixes of this PolicyRuleWriteModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._prefixes

    @prefixes.setter
    def prefixes(self, prefixes):
        """Sets the prefixes of this PolicyRuleWriteModel.

        The prefixes of the policy rule  # noqa: E501

        :param prefixes: The prefixes of this PolicyRuleWriteModel.  # noqa: E501
        :type: list[str]
        """

        self._prefixes = prefixes

    @property
    def roles(self):
        """Gets the roles of this PolicyRuleWriteModel.  # noqa: E501

        The list of role identifiers of the policy rule  # noqa: E501

        :return: The roles of this PolicyRuleWriteModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this PolicyRuleWriteModel.

        The list of role identifiers of the policy rule  # noqa: E501

        :param roles: The roles of this PolicyRuleWriteModel.  # noqa: E501
        :type: list[str]
        """

        self._roles = roles

    @property
    def tags(self):
        """Gets the tags of this PolicyRuleWriteModel.  # noqa: E501

        The tag/value pairs of the policy rule  # noqa: E501

        :return: The tags of this PolicyRuleWriteModel.  # noqa: E501
        :rtype: list[Annotation]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this PolicyRuleWriteModel.

        The tag/value pairs of the policy rule  # noqa: E501

        :param tags: The tags of this PolicyRuleWriteModel.  # noqa: E501
        :type: list[Annotation]
        """

        self._tags = tags

    @property
    def tags_anded(self):
        """Gets the tags_anded of this PolicyRuleWriteModel.  # noqa: E501

        Whether tags should be AND-ed or OR-ed.If true, a metric must contain all tags in order for the policy rule to apply. If false, the tags are OR-ed, and a metric must contain one of the tags. Default: false  # noqa: E501

        :return: The tags_anded of this PolicyRuleWriteModel.  # noqa: E501
        :rtype: bool
        """
        return self._tags_anded

    @tags_anded.setter
    def tags_anded(self, tags_anded):
        """Sets the tags_anded of this PolicyRuleWriteModel.

        Whether tags should be AND-ed or OR-ed.If true, a metric must contain all tags in order for the policy rule to apply. If false, the tags are OR-ed, and a metric must contain one of the tags. Default: false  # noqa: E501

        :param tags_anded: The tags_anded of this PolicyRuleWriteModel.  # noqa: E501
        :type: bool
        """

        self._tags_anded = tags_anded

    @property
    def user_groups(self):
        """Gets the user_groups of this PolicyRuleWriteModel.  # noqa: E501

        The list of user group identifiers of the policy rule  # noqa: E501

        :return: The user_groups of this PolicyRuleWriteModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._user_groups

    @user_groups.setter
    def user_groups(self, user_groups):
        """Sets the user_groups of this PolicyRuleWriteModel.

        The list of user group identifiers of the policy rule  # noqa: E501

        :param user_groups: The user_groups of this PolicyRuleWriteModel.  # noqa: E501
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
        if issubclass(PolicyRuleWriteModel, dict):
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
        if not isinstance(other, PolicyRuleWriteModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PolicyRuleWriteModel):
            return True

        return self.to_dict() != other.to_dict()
