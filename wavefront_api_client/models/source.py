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


class Source(object):
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
        'description': 'str',
        'hidden': 'bool',
        'id': 'str',
        'marked_new_epoch_millis': 'int',
        'source_name': 'str',
        'tags': 'dict(str, bool)',
        'updated_epoch_millis': 'int',
        'updater_id': 'str'
    }

    attribute_map = {
        'created_epoch_millis': 'createdEpochMillis',
        'creator_id': 'creatorId',
        'description': 'description',
        'hidden': 'hidden',
        'id': 'id',
        'marked_new_epoch_millis': 'markedNewEpochMillis',
        'source_name': 'sourceName',
        'tags': 'tags',
        'updated_epoch_millis': 'updatedEpochMillis',
        'updater_id': 'updaterId'
    }

    def __init__(self, created_epoch_millis=None, creator_id=None, description=None, hidden=None, id=None, marked_new_epoch_millis=None, source_name=None, tags=None, updated_epoch_millis=None, updater_id=None, _configuration=None):  # noqa: E501
        """Source - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._created_epoch_millis = None
        self._creator_id = None
        self._description = None
        self._hidden = None
        self._id = None
        self._marked_new_epoch_millis = None
        self._source_name = None
        self._tags = None
        self._updated_epoch_millis = None
        self._updater_id = None
        self.discriminator = None

        if created_epoch_millis is not None:
            self.created_epoch_millis = created_epoch_millis
        if creator_id is not None:
            self.creator_id = creator_id
        if description is not None:
            self.description = description
        if hidden is not None:
            self.hidden = hidden
        self.id = id
        if marked_new_epoch_millis is not None:
            self.marked_new_epoch_millis = marked_new_epoch_millis
        self.source_name = source_name
        if tags is not None:
            self.tags = tags
        if updated_epoch_millis is not None:
            self.updated_epoch_millis = updated_epoch_millis
        if updater_id is not None:
            self.updater_id = updater_id

    @property
    def created_epoch_millis(self):
        """Gets the created_epoch_millis of this Source.  # noqa: E501


        :return: The created_epoch_millis of this Source.  # noqa: E501
        :rtype: int
        """
        return self._created_epoch_millis

    @created_epoch_millis.setter
    def created_epoch_millis(self, created_epoch_millis):
        """Sets the created_epoch_millis of this Source.


        :param created_epoch_millis: The created_epoch_millis of this Source.  # noqa: E501
        :type: int
        """

        self._created_epoch_millis = created_epoch_millis

    @property
    def creator_id(self):
        """Gets the creator_id of this Source.  # noqa: E501


        :return: The creator_id of this Source.  # noqa: E501
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this Source.


        :param creator_id: The creator_id of this Source.  # noqa: E501
        :type: str
        """

        self._creator_id = creator_id

    @property
    def description(self):
        """Gets the description of this Source.  # noqa: E501

        Description of this source  # noqa: E501

        :return: The description of this Source.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Source.

        Description of this source  # noqa: E501

        :param description: The description of this Source.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def hidden(self):
        """Gets the hidden of this Source.  # noqa: E501

        A derived field denoting whether this source has been hidden (e.g. excluding it from query autocomplete among other things)  # noqa: E501

        :return: The hidden of this Source.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this Source.

        A derived field denoting whether this source has been hidden (e.g. excluding it from query autocomplete among other things)  # noqa: E501

        :param hidden: The hidden of this Source.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

    @property
    def id(self):
        """Gets the id of this Source.  # noqa: E501

        id of this source, must be exactly equivalent to 'sourceName'  # noqa: E501

        :return: The id of this Source.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Source.

        id of this source, must be exactly equivalent to 'sourceName'  # noqa: E501

        :param id: The id of this Source.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def marked_new_epoch_millis(self):
        """Gets the marked_new_epoch_millis of this Source.  # noqa: E501

        Epoch Millis when this source was marked as ~status.new  # noqa: E501

        :return: The marked_new_epoch_millis of this Source.  # noqa: E501
        :rtype: int
        """
        return self._marked_new_epoch_millis

    @marked_new_epoch_millis.setter
    def marked_new_epoch_millis(self, marked_new_epoch_millis):
        """Sets the marked_new_epoch_millis of this Source.

        Epoch Millis when this source was marked as ~status.new  # noqa: E501

        :param marked_new_epoch_millis: The marked_new_epoch_millis of this Source.  # noqa: E501
        :type: int
        """

        self._marked_new_epoch_millis = marked_new_epoch_millis

    @property
    def source_name(self):
        """Gets the source_name of this Source.  # noqa: E501

        The name of the source, usually set by ingested telemetry  # noqa: E501

        :return: The source_name of this Source.  # noqa: E501
        :rtype: str
        """
        return self._source_name

    @source_name.setter
    def source_name(self, source_name):
        """Sets the source_name of this Source.

        The name of the source, usually set by ingested telemetry  # noqa: E501

        :param source_name: The source_name of this Source.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and source_name is None:
            raise ValueError("Invalid value for `source_name`, must not be `None`")  # noqa: E501

        self._source_name = source_name

    @property
    def tags(self):
        """Gets the tags of this Source.  # noqa: E501

        A Map (String -> boolean) Representing the source tags associated with this source.  To create a tag, set it as a KEY in this map, with associated value equal to true  # noqa: E501

        :return: The tags of this Source.  # noqa: E501
        :rtype: dict(str, bool)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Source.

        A Map (String -> boolean) Representing the source tags associated with this source.  To create a tag, set it as a KEY in this map, with associated value equal to true  # noqa: E501

        :param tags: The tags of this Source.  # noqa: E501
        :type: dict(str, bool)
        """

        self._tags = tags

    @property
    def updated_epoch_millis(self):
        """Gets the updated_epoch_millis of this Source.  # noqa: E501


        :return: The updated_epoch_millis of this Source.  # noqa: E501
        :rtype: int
        """
        return self._updated_epoch_millis

    @updated_epoch_millis.setter
    def updated_epoch_millis(self, updated_epoch_millis):
        """Sets the updated_epoch_millis of this Source.


        :param updated_epoch_millis: The updated_epoch_millis of this Source.  # noqa: E501
        :type: int
        """

        self._updated_epoch_millis = updated_epoch_millis

    @property
    def updater_id(self):
        """Gets the updater_id of this Source.  # noqa: E501


        :return: The updater_id of this Source.  # noqa: E501
        :rtype: str
        """
        return self._updater_id

    @updater_id.setter
    def updater_id(self, updater_id):
        """Sets the updater_id of this Source.


        :param updater_id: The updater_id of this Source.  # noqa: E501
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
        if issubclass(Source, dict):
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
        if not isinstance(other, Source):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Source):
            return True

        return self.to_dict() != other.to_dict()
