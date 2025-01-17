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


class IntegrationAlias(object):
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
        'base_url': 'str',
        'description': 'str',
        'icon': 'str',
        'id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'base_url': 'baseUrl',
        'description': 'description',
        'icon': 'icon',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, base_url=None, description=None, icon=None, id=None, name=None, _configuration=None):  # noqa: E501
        """IntegrationAlias - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._base_url = None
        self._description = None
        self._icon = None
        self._id = None
        self._name = None
        self.discriminator = None

        if base_url is not None:
            self.base_url = base_url
        if description is not None:
            self.description = description
        if icon is not None:
            self.icon = icon
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name

    @property
    def base_url(self):
        """Gets the base_url of this IntegrationAlias.  # noqa: E501

        Base URL of this alias Integration  # noqa: E501

        :return: The base_url of this IntegrationAlias.  # noqa: E501
        :rtype: str
        """
        return self._base_url

    @base_url.setter
    def base_url(self, base_url):
        """Sets the base_url of this IntegrationAlias.

        Base URL of this alias Integration  # noqa: E501

        :param base_url: The base_url of this IntegrationAlias.  # noqa: E501
        :type: str
        """

        self._base_url = base_url

    @property
    def description(self):
        """Gets the description of this IntegrationAlias.  # noqa: E501

        Description of the alias Integration  # noqa: E501

        :return: The description of this IntegrationAlias.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IntegrationAlias.

        Description of the alias Integration  # noqa: E501

        :param description: The description of this IntegrationAlias.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def icon(self):
        """Gets the icon of this IntegrationAlias.  # noqa: E501

        Icon path of the alias Integration  # noqa: E501

        :return: The icon of this IntegrationAlias.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this IntegrationAlias.

        Icon path of the alias Integration  # noqa: E501

        :param icon: The icon of this IntegrationAlias.  # noqa: E501
        :type: str
        """

        self._icon = icon

    @property
    def id(self):
        """Gets the id of this IntegrationAlias.  # noqa: E501

        ID of the alias Integration  # noqa: E501

        :return: The id of this IntegrationAlias.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IntegrationAlias.

        ID of the alias Integration  # noqa: E501

        :param id: The id of this IntegrationAlias.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this IntegrationAlias.  # noqa: E501

        Name of the alias Integration  # noqa: E501

        :return: The name of this IntegrationAlias.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IntegrationAlias.

        Name of the alias Integration  # noqa: E501

        :param name: The name of this IntegrationAlias.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(IntegrationAlias, dict):
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
        if not isinstance(other, IntegrationAlias):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IntegrationAlias):
            return True

        return self.to_dict() != other.to_dict()
