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


class SavedAppMapSearchGroup(object):
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
        'creator_id': 'str',
        'id': 'str',
        'name': 'str',
        'search_filters': 'list[str]',
        'updated_epoch_millis': 'int',
        'updater_id': 'str'
    }

    attribute_map = {
        'created_epoch_millis': 'createdEpochMillis',
        'creator_id': 'creatorId',
        'id': 'id',
        'name': 'name',
        'search_filters': 'searchFilters',
        'updated_epoch_millis': 'updatedEpochMillis',
        'updater_id': 'updaterId'
    }

    def __init__(self, created_epoch_millis=None, creator_id=None, id=None, name=None, search_filters=None, updated_epoch_millis=None, updater_id=None, _configuration=None):  # noqa: E501
        """SavedAppMapSearchGroup - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._created_epoch_millis = None
        self._creator_id = None
        self._id = None
        self._name = None
        self._search_filters = None
        self._updated_epoch_millis = None
        self._updater_id = None
        self.discriminator = None

        if created_epoch_millis is not None:
            self.created_epoch_millis = created_epoch_millis
        if creator_id is not None:
            self.creator_id = creator_id
        if id is not None:
            self.id = id
        self.name = name
        if search_filters is not None:
            self.search_filters = search_filters
        if updated_epoch_millis is not None:
            self.updated_epoch_millis = updated_epoch_millis
        if updater_id is not None:
            self.updater_id = updater_id

    @property
    def created_epoch_millis(self):
        """Gets the created_epoch_millis of this SavedAppMapSearchGroup.  # noqa: E501


        :return: The created_epoch_millis of this SavedAppMapSearchGroup.  # noqa: E501
        :rtype: int
        """
        return self._created_epoch_millis

    @created_epoch_millis.setter
    def created_epoch_millis(self, created_epoch_millis):
        """Sets the created_epoch_millis of this SavedAppMapSearchGroup.


        :param created_epoch_millis: The created_epoch_millis of this SavedAppMapSearchGroup.  # noqa: E501
        :type: int
        """

        self._created_epoch_millis = created_epoch_millis

    @property
    def creator_id(self):
        """Gets the creator_id of this SavedAppMapSearchGroup.  # noqa: E501


        :return: The creator_id of this SavedAppMapSearchGroup.  # noqa: E501
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this SavedAppMapSearchGroup.


        :param creator_id: The creator_id of this SavedAppMapSearchGroup.  # noqa: E501
        :type: str
        """

        self._creator_id = creator_id

    @property
    def id(self):
        """Gets the id of this SavedAppMapSearchGroup.  # noqa: E501


        :return: The id of this SavedAppMapSearchGroup.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SavedAppMapSearchGroup.


        :param id: The id of this SavedAppMapSearchGroup.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this SavedAppMapSearchGroup.  # noqa: E501

        Name of the search group  # noqa: E501

        :return: The name of this SavedAppMapSearchGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SavedAppMapSearchGroup.

        Name of the search group  # noqa: E501

        :param name: The name of this SavedAppMapSearchGroup.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def search_filters(self):
        """Gets the search_filters of this SavedAppMapSearchGroup.  # noqa: E501


        :return: The search_filters of this SavedAppMapSearchGroup.  # noqa: E501
        :rtype: list[str]
        """
        return self._search_filters

    @search_filters.setter
    def search_filters(self, search_filters):
        """Sets the search_filters of this SavedAppMapSearchGroup.


        :param search_filters: The search_filters of this SavedAppMapSearchGroup.  # noqa: E501
        :type: list[str]
        """

        self._search_filters = search_filters

    @property
    def updated_epoch_millis(self):
        """Gets the updated_epoch_millis of this SavedAppMapSearchGroup.  # noqa: E501


        :return: The updated_epoch_millis of this SavedAppMapSearchGroup.  # noqa: E501
        :rtype: int
        """
        return self._updated_epoch_millis

    @updated_epoch_millis.setter
    def updated_epoch_millis(self, updated_epoch_millis):
        """Sets the updated_epoch_millis of this SavedAppMapSearchGroup.


        :param updated_epoch_millis: The updated_epoch_millis of this SavedAppMapSearchGroup.  # noqa: E501
        :type: int
        """

        self._updated_epoch_millis = updated_epoch_millis

    @property
    def updater_id(self):
        """Gets the updater_id of this SavedAppMapSearchGroup.  # noqa: E501


        :return: The updater_id of this SavedAppMapSearchGroup.  # noqa: E501
        :rtype: str
        """
        return self._updater_id

    @updater_id.setter
    def updater_id(self, updater_id):
        """Sets the updater_id of this SavedAppMapSearchGroup.


        :param updater_id: The updater_id of this SavedAppMapSearchGroup.  # noqa: E501
        :type: str
        """

        self._updater_id = updater_id

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
        if issubclass(SavedAppMapSearchGroup, dict):
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
        if not isinstance(other, SavedAppMapSearchGroup):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SavedAppMapSearchGroup):
            return True

        return self.to_dict() != other.to_dict()
