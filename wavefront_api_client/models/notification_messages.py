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


class NotificationMessages(object):
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
        'additional_info': 'dict(str, str)',
        'content': 'str',
        'created_epoch_millis': 'int',
        'creator_id': 'str',
        'deleted': 'bool',
        'id': 'str',
        'method': 'str',
        'name': 'str',
        'subject': 'str',
        'updated_epoch_millis': 'int',
        'updater_id': 'str'
    }

    attribute_map = {
        'additional_info': 'additionalInfo',
        'content': 'content',
        'created_epoch_millis': 'createdEpochMillis',
        'creator_id': 'creatorId',
        'deleted': 'deleted',
        'id': 'id',
        'method': 'method',
        'name': 'name',
        'subject': 'subject',
        'updated_epoch_millis': 'updatedEpochMillis',
        'updater_id': 'updaterId'
    }

    def __init__(self, additional_info=None, content=None, created_epoch_millis=None, creator_id=None, deleted=None, id=None, method=None, name=None, subject=None, updated_epoch_millis=None, updater_id=None, _configuration=None):  # noqa: E501
        """NotificationMessages - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._additional_info = None
        self._content = None
        self._created_epoch_millis = None
        self._creator_id = None
        self._deleted = None
        self._id = None
        self._method = None
        self._name = None
        self._subject = None
        self._updated_epoch_millis = None
        self._updater_id = None
        self.discriminator = None

        if additional_info is not None:
            self.additional_info = additional_info
        if content is not None:
            self.content = content
        if created_epoch_millis is not None:
            self.created_epoch_millis = created_epoch_millis
        if creator_id is not None:
            self.creator_id = creator_id
        if deleted is not None:
            self.deleted = deleted
        if id is not None:
            self.id = id
        if method is not None:
            self.method = method
        if name is not None:
            self.name = name
        if subject is not None:
            self.subject = subject
        if updated_epoch_millis is not None:
            self.updated_epoch_millis = updated_epoch_millis
        if updater_id is not None:
            self.updater_id = updater_id

    @property
    def additional_info(self):
        """Gets the additional_info of this NotificationMessages.  # noqa: E501


        :return: The additional_info of this NotificationMessages.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this NotificationMessages.


        :param additional_info: The additional_info of this NotificationMessages.  # noqa: E501
        :type: dict(str, str)
        """

        self._additional_info = additional_info

    @property
    def content(self):
        """Gets the content of this NotificationMessages.  # noqa: E501


        :return: The content of this NotificationMessages.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this NotificationMessages.


        :param content: The content of this NotificationMessages.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def created_epoch_millis(self):
        """Gets the created_epoch_millis of this NotificationMessages.  # noqa: E501


        :return: The created_epoch_millis of this NotificationMessages.  # noqa: E501
        :rtype: int
        """
        return self._created_epoch_millis

    @created_epoch_millis.setter
    def created_epoch_millis(self, created_epoch_millis):
        """Sets the created_epoch_millis of this NotificationMessages.


        :param created_epoch_millis: The created_epoch_millis of this NotificationMessages.  # noqa: E501
        :type: int
        """

        self._created_epoch_millis = created_epoch_millis

    @property
    def creator_id(self):
        """Gets the creator_id of this NotificationMessages.  # noqa: E501


        :return: The creator_id of this NotificationMessages.  # noqa: E501
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this NotificationMessages.


        :param creator_id: The creator_id of this NotificationMessages.  # noqa: E501
        :type: str
        """

        self._creator_id = creator_id

    @property
    def deleted(self):
        """Gets the deleted of this NotificationMessages.  # noqa: E501


        :return: The deleted of this NotificationMessages.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this NotificationMessages.


        :param deleted: The deleted of this NotificationMessages.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def id(self):
        """Gets the id of this NotificationMessages.  # noqa: E501


        :return: The id of this NotificationMessages.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NotificationMessages.


        :param id: The id of this NotificationMessages.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def method(self):
        """Gets the method of this NotificationMessages.  # noqa: E501

        The notification method, can either be WEBHOOK, EMAIL or PAGERDUTY  # noqa: E501

        :return: The method of this NotificationMessages.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this NotificationMessages.

        The notification method, can either be WEBHOOK, EMAIL or PAGERDUTY  # noqa: E501

        :param method: The method of this NotificationMessages.  # noqa: E501
        :type: str
        """
        allowed_values = ["WEBHOOK", "PAGERDUTY", "EMAIL"]  # noqa: E501
        if (self._configuration.client_side_validation and
                method not in allowed_values):
            raise ValueError(
                "Invalid value for `method` ({0}), must be one of {1}"  # noqa: E501
                .format(method, allowed_values)
            )

        self._method = method

    @property
    def name(self):
        """Gets the name of this NotificationMessages.  # noqa: E501

        The alert target name, easier to read than ID  # noqa: E501

        :return: The name of this NotificationMessages.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NotificationMessages.

        The alert target name, easier to read than ID  # noqa: E501

        :param name: The name of this NotificationMessages.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def subject(self):
        """Gets the subject of this NotificationMessages.  # noqa: E501


        :return: The subject of this NotificationMessages.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this NotificationMessages.


        :param subject: The subject of this NotificationMessages.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def updated_epoch_millis(self):
        """Gets the updated_epoch_millis of this NotificationMessages.  # noqa: E501


        :return: The updated_epoch_millis of this NotificationMessages.  # noqa: E501
        :rtype: int
        """
        return self._updated_epoch_millis

    @updated_epoch_millis.setter
    def updated_epoch_millis(self, updated_epoch_millis):
        """Sets the updated_epoch_millis of this NotificationMessages.


        :param updated_epoch_millis: The updated_epoch_millis of this NotificationMessages.  # noqa: E501
        :type: int
        """

        self._updated_epoch_millis = updated_epoch_millis

    @property
    def updater_id(self):
        """Gets the updater_id of this NotificationMessages.  # noqa: E501


        :return: The updater_id of this NotificationMessages.  # noqa: E501
        :rtype: str
        """
        return self._updater_id

    @updater_id.setter
    def updater_id(self, updater_id):
        """Sets the updater_id of this NotificationMessages.


        :param updater_id: The updater_id of this NotificationMessages.  # noqa: E501
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
        if issubclass(NotificationMessages, dict):
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
        if not isinstance(other, NotificationMessages):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NotificationMessages):
            return True

        return self.to_dict() != other.to_dict()
