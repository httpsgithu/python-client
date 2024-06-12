# coding: utf-8

"""
    Tanzu Observability REST API Documentation

    <p>The REST API enables you to interact with the Tanzu Observability service by using standard REST API tools. You can use the REST API to automate commonly executed operations, for example to tag sources automatically.</p><p>When you make REST API calls outside the REST API documentation UI, to authenticate to the service, you must use an API token associated with a user account or a service account. For information on how to get the API token and examples, see <a href=\"http://docs.wavefront.com/using_wavefront_api.html\">Use the Tanzu Observability REST API.</a></p>  # noqa: E501

    OpenAPI spec version: v2
    Contact: chitimba@wavefront.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from wavefront_api_client.configuration import Configuration


class RoleUpdateDTO(object):
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
        'description': 'str',
        'id': 'str',
        'name': 'str',
        'permissions': 'list[str]'
    }

    attribute_map = {
        'description': 'description',
        'id': 'id',
        'name': 'name',
        'permissions': 'permissions'
    }

    def __init__(self, description=None, id=None, name=None, permissions=None, _configuration=None):  # noqa: E501
        """RoleUpdateDTO - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._id = None
        self._name = None
        self._permissions = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if permissions is not None:
            self.permissions = permissions

    @property
    def description(self):
        """Gets the description of this RoleUpdateDTO.  # noqa: E501

        The description of the role  # noqa: E501

        :return: The description of this RoleUpdateDTO.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RoleUpdateDTO.

        The description of the role  # noqa: E501

        :param description: The description of this RoleUpdateDTO.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this RoleUpdateDTO.  # noqa: E501

        The unique identifier of the role  # noqa: E501

        :return: The id of this RoleUpdateDTO.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RoleUpdateDTO.

        The unique identifier of the role  # noqa: E501

        :param id: The id of this RoleUpdateDTO.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this RoleUpdateDTO.  # noqa: E501

        The name of the role  # noqa: E501

        :return: The name of this RoleUpdateDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RoleUpdateDTO.

        The name of the role  # noqa: E501

        :param name: The name of this RoleUpdateDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def permissions(self):
        """Gets the permissions of this RoleUpdateDTO.  # noqa: E501

        List of permissions the role has been granted access to  # noqa: E501

        :return: The permissions of this RoleUpdateDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this RoleUpdateDTO.

        List of permissions the role has been granted access to  # noqa: E501

        :param permissions: The permissions of this RoleUpdateDTO.  # noqa: E501
        :type: list[str]
        """

        self._permissions = permissions

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
        if issubclass(RoleUpdateDTO, dict):
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
        if not isinstance(other, RoleUpdateDTO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RoleUpdateDTO):
            return True

        return self.to_dict() != other.to_dict()
