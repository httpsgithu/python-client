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


class UserGroupWrite(object):
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
        'created_epoch_millis': 'int',
        'customer': 'str',
        'description': 'str',
        'id': 'str',
        'name': 'str',
        'role_ids': 'list[str]'
    }

    attribute_map = {
        'created_epoch_millis': 'createdEpochMillis',
        'customer': 'customer',
        'description': 'description',
        'id': 'id',
        'name': 'name',
        'role_ids': 'roleIDs'
    }

    def __init__(self, created_epoch_millis=None, customer=None, description=None, id=None, name=None, role_ids=None, _configuration=None):  # noqa: E501
        """UserGroupWrite - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._created_epoch_millis = None
        self._customer = None
        self._description = None
        self._id = None
        self._name = None
        self._role_ids = None
        self.discriminator = None

        if created_epoch_millis is not None:
            self.created_epoch_millis = created_epoch_millis
        if customer is not None:
            self.customer = customer
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        self.name = name
        self.role_ids = role_ids

    @property
    def created_epoch_millis(self):
        """Gets the created_epoch_millis of this UserGroupWrite.  # noqa: E501


        :return: The created_epoch_millis of this UserGroupWrite.  # noqa: E501
        :rtype: int
        """
        return self._created_epoch_millis

    @created_epoch_millis.setter
    def created_epoch_millis(self, created_epoch_millis):
        """Sets the created_epoch_millis of this UserGroupWrite.


        :param created_epoch_millis: The created_epoch_millis of this UserGroupWrite.  # noqa: E501
        :type: int
        """

        self._created_epoch_millis = created_epoch_millis

    @property
    def customer(self):
        """Gets the customer of this UserGroupWrite.  # noqa: E501

        The id of the customer to which the user group belongs  # noqa: E501

        :return: The customer of this UserGroupWrite.  # noqa: E501
        :rtype: str
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this UserGroupWrite.

        The id of the customer to which the user group belongs  # noqa: E501

        :param customer: The customer of this UserGroupWrite.  # noqa: E501
        :type: str
        """

        self._customer = customer

    @property
    def description(self):
        """Gets the description of this UserGroupWrite.  # noqa: E501

        The description of the user group  # noqa: E501

        :return: The description of this UserGroupWrite.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UserGroupWrite.

        The description of the user group  # noqa: E501

        :param description: The description of this UserGroupWrite.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this UserGroupWrite.  # noqa: E501

        The unique identifier of the user group  # noqa: E501

        :return: The id of this UserGroupWrite.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserGroupWrite.

        The unique identifier of the user group  # noqa: E501

        :param id: The id of this UserGroupWrite.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this UserGroupWrite.  # noqa: E501

        The name of the user group  # noqa: E501

        :return: The name of this UserGroupWrite.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserGroupWrite.

        The name of the user group  # noqa: E501

        :param name: The name of this UserGroupWrite.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def role_ids(self):
        """Gets the role_ids of this UserGroupWrite.  # noqa: E501

        List of role IDs the user group has been linked to.  # noqa: E501

        :return: The role_ids of this UserGroupWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._role_ids

    @role_ids.setter
    def role_ids(self, role_ids):
        """Sets the role_ids of this UserGroupWrite.

        List of role IDs the user group has been linked to.  # noqa: E501

        :param role_ids: The role_ids of this UserGroupWrite.  # noqa: E501
        :type: list[str]
        """
        if self._configuration.client_side_validation and role_ids is None:
            raise ValueError("Invalid value for `role_ids`, must not be `None`")  # noqa: E501

        self._role_ids = role_ids

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
        if issubclass(UserGroupWrite, dict):
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
        if not isinstance(other, UserGroupWrite):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserGroupWrite):
            return True

        return self.to_dict() != other.to_dict()
