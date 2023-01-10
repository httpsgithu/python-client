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


class Message(object):
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
        'attributes': 'dict(str, str)',
        'content': 'str',
        'display': 'str',
        'end_epoch_millis': 'int',
        'id': 'str',
        'read': 'bool',
        'scope': 'str',
        'severity': 'str',
        'source': 'str',
        'start_epoch_millis': 'int',
        'target': 'str',
        'title': 'str'
    }

    attribute_map = {
        'attributes': 'attributes',
        'content': 'content',
        'display': 'display',
        'end_epoch_millis': 'endEpochMillis',
        'id': 'id',
        'read': 'read',
        'scope': 'scope',
        'severity': 'severity',
        'source': 'source',
        'start_epoch_millis': 'startEpochMillis',
        'target': 'target',
        'title': 'title'
    }

    def __init__(self, attributes=None, content=None, display=None, end_epoch_millis=None, id=None, read=None, scope=None, severity=None, source=None, start_epoch_millis=None, target=None, title=None, _configuration=None):  # noqa: E501
        """Message - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._attributes = None
        self._content = None
        self._display = None
        self._end_epoch_millis = None
        self._id = None
        self._read = None
        self._scope = None
        self._severity = None
        self._source = None
        self._start_epoch_millis = None
        self._target = None
        self._title = None
        self.discriminator = None

        if attributes is not None:
            self.attributes = attributes
        self.content = content
        self.display = display
        self.end_epoch_millis = end_epoch_millis
        if id is not None:
            self.id = id
        if read is not None:
            self.read = read
        self.scope = scope
        self.severity = severity
        self.source = source
        self.start_epoch_millis = start_epoch_millis
        if target is not None:
            self.target = target
        self.title = title

    @property
    def attributes(self):
        """Gets the attributes of this Message.  # noqa: E501

        A string->string map of additional properties associated with this message  # noqa: E501

        :return: The attributes of this Message.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this Message.

        A string->string map of additional properties associated with this message  # noqa: E501

        :param attributes: The attributes of this Message.  # noqa: E501
        :type: dict(str, str)
        """

        self._attributes = attributes

    @property
    def content(self):
        """Gets the content of this Message.  # noqa: E501

        Message content  # noqa: E501

        :return: The content of this Message.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this Message.

        Message content  # noqa: E501

        :param content: The content of this Message.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

    @property
    def display(self):
        """Gets the display of this Message.  # noqa: E501

        The form of display for this message  # noqa: E501

        :return: The display of this Message.  # noqa: E501
        :rtype: str
        """
        return self._display

    @display.setter
    def display(self, display):
        """Sets the display of this Message.

        The form of display for this message  # noqa: E501

        :param display: The display of this Message.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and display is None:
            raise ValueError("Invalid value for `display`, must not be `None`")  # noqa: E501
        allowed_values = ["BANNER", "TOASTER", "MODAL"]  # noqa: E501
        if (self._configuration.client_side_validation and
                display not in allowed_values):
            raise ValueError(
                "Invalid value for `display` ({0}), must be one of {1}"  # noqa: E501
                .format(display, allowed_values)
            )

        self._display = display

    @property
    def end_epoch_millis(self):
        """Gets the end_epoch_millis of this Message.  # noqa: E501

        When this message will stop being displayed, in epoch millis  # noqa: E501

        :return: The end_epoch_millis of this Message.  # noqa: E501
        :rtype: int
        """
        return self._end_epoch_millis

    @end_epoch_millis.setter
    def end_epoch_millis(self, end_epoch_millis):
        """Sets the end_epoch_millis of this Message.

        When this message will stop being displayed, in epoch millis  # noqa: E501

        :param end_epoch_millis: The end_epoch_millis of this Message.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and end_epoch_millis is None:
            raise ValueError("Invalid value for `end_epoch_millis`, must not be `None`")  # noqa: E501

        self._end_epoch_millis = end_epoch_millis

    @property
    def id(self):
        """Gets the id of this Message.  # noqa: E501


        :return: The id of this Message.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Message.


        :param id: The id of this Message.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def read(self):
        """Gets the read of this Message.  # noqa: E501

        A derived field for whether the current user has read this message  # noqa: E501

        :return: The read of this Message.  # noqa: E501
        :rtype: bool
        """
        return self._read

    @read.setter
    def read(self, read):
        """Sets the read of this Message.

        A derived field for whether the current user has read this message  # noqa: E501

        :param read: The read of this Message.  # noqa: E501
        :type: bool
        """

        self._read = read

    @property
    def scope(self):
        """Gets the scope of this Message.  # noqa: E501

        The audience scope that this message should reach  # noqa: E501

        :return: The scope of this Message.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this Message.

        The audience scope that this message should reach  # noqa: E501

        :param scope: The scope of this Message.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and scope is None:
            raise ValueError("Invalid value for `scope`, must not be `None`")  # noqa: E501
        allowed_values = ["CLUSTER", "CUSTOMER", "USER"]  # noqa: E501
        if (self._configuration.client_side_validation and
                scope not in allowed_values):
            raise ValueError(
                "Invalid value for `scope` ({0}), must be one of {1}"  # noqa: E501
                .format(scope, allowed_values)
            )

        self._scope = scope

    @property
    def severity(self):
        """Gets the severity of this Message.  # noqa: E501

        Message severity  # noqa: E501

        :return: The severity of this Message.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this Message.

        Message severity  # noqa: E501

        :param severity: The severity of this Message.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and severity is None:
            raise ValueError("Invalid value for `severity`, must not be `None`")  # noqa: E501
        allowed_values = ["MARKETING", "INFO", "WARN", "SEVERE"]  # noqa: E501
        if (self._configuration.client_side_validation and
                severity not in allowed_values):
            raise ValueError(
                "Invalid value for `severity` ({0}), must be one of {1}"  # noqa: E501
                .format(severity, allowed_values)
            )

        self._severity = severity

    @property
    def source(self):
        """Gets the source of this Message.  # noqa: E501

        Message source.  System messages will com from 'system@wavefront.com'  # noqa: E501

        :return: The source of this Message.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this Message.

        Message source.  System messages will com from 'system@wavefront.com'  # noqa: E501

        :param source: The source of this Message.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and source is None:
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source

    @property
    def start_epoch_millis(self):
        """Gets the start_epoch_millis of this Message.  # noqa: E501

        When this message will begin to be displayed, in epoch millis  # noqa: E501

        :return: The start_epoch_millis of this Message.  # noqa: E501
        :rtype: int
        """
        return self._start_epoch_millis

    @start_epoch_millis.setter
    def start_epoch_millis(self, start_epoch_millis):
        """Sets the start_epoch_millis of this Message.

        When this message will begin to be displayed, in epoch millis  # noqa: E501

        :param start_epoch_millis: The start_epoch_millis of this Message.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and start_epoch_millis is None:
            raise ValueError("Invalid value for `start_epoch_millis`, must not be `None`")  # noqa: E501

        self._start_epoch_millis = start_epoch_millis

    @property
    def target(self):
        """Gets the target of this Message.  # noqa: E501

        For scope=CUSTOMER or scope=USER, the individual customer or user id  # noqa: E501

        :return: The target of this Message.  # noqa: E501
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this Message.

        For scope=CUSTOMER or scope=USER, the individual customer or user id  # noqa: E501

        :param target: The target of this Message.  # noqa: E501
        :type: str
        """

        self._target = target

    @property
    def title(self):
        """Gets the title of this Message.  # noqa: E501

        Title of this message  # noqa: E501

        :return: The title of this Message.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Message.

        Title of this message  # noqa: E501

        :param title: The title of this Message.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

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
        if issubclass(Message, dict):
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
        if not isinstance(other, Message):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Message):
            return True

        return self.to_dict() != other.to_dict()
