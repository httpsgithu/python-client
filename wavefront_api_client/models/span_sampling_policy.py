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


class SpanSamplingPolicy(object):
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
        'active': 'bool',
        'created_epoch_millis': 'int',
        'creator_id': 'str',
        'deleted': 'bool',
        'description': 'str',
        'expression': 'str',
        'id': 'str',
        'name': 'str',
        'sampling_percent': 'int',
        'updated_epoch_millis': 'int',
        'updater_id': 'str'
    }

    attribute_map = {
        'active': 'active',
        'created_epoch_millis': 'createdEpochMillis',
        'creator_id': 'creatorId',
        'deleted': 'deleted',
        'description': 'description',
        'expression': 'expression',
        'id': 'id',
        'name': 'name',
        'sampling_percent': 'samplingPercent',
        'updated_epoch_millis': 'updatedEpochMillis',
        'updater_id': 'updaterId'
    }

    def __init__(self, active=None, created_epoch_millis=None, creator_id=None, deleted=None, description=None, expression=None, id=None, name=None, sampling_percent=None, updated_epoch_millis=None, updater_id=None, _configuration=None):  # noqa: E501
        """SpanSamplingPolicy - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._active = None
        self._created_epoch_millis = None
        self._creator_id = None
        self._deleted = None
        self._description = None
        self._expression = None
        self._id = None
        self._name = None
        self._sampling_percent = None
        self._updated_epoch_millis = None
        self._updater_id = None
        self.discriminator = None

        if active is not None:
            self.active = active
        if created_epoch_millis is not None:
            self.created_epoch_millis = created_epoch_millis
        if creator_id is not None:
            self.creator_id = creator_id
        if deleted is not None:
            self.deleted = deleted
        if description is not None:
            self.description = description
        self.expression = expression
        self.id = id
        self.name = name
        if sampling_percent is not None:
            self.sampling_percent = sampling_percent
        if updated_epoch_millis is not None:
            self.updated_epoch_millis = updated_epoch_millis
        if updater_id is not None:
            self.updater_id = updater_id

    @property
    def active(self):
        """Gets the active of this SpanSamplingPolicy.  # noqa: E501

        Whether span sampling policy is active  # noqa: E501

        :return: The active of this SpanSamplingPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this SpanSamplingPolicy.

        Whether span sampling policy is active  # noqa: E501

        :param active: The active of this SpanSamplingPolicy.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def created_epoch_millis(self):
        """Gets the created_epoch_millis of this SpanSamplingPolicy.  # noqa: E501

        Created time of the span sampling policy  # noqa: E501

        :return: The created_epoch_millis of this SpanSamplingPolicy.  # noqa: E501
        :rtype: int
        """
        return self._created_epoch_millis

    @created_epoch_millis.setter
    def created_epoch_millis(self, created_epoch_millis):
        """Sets the created_epoch_millis of this SpanSamplingPolicy.

        Created time of the span sampling policy  # noqa: E501

        :param created_epoch_millis: The created_epoch_millis of this SpanSamplingPolicy.  # noqa: E501
        :type: int
        """

        self._created_epoch_millis = created_epoch_millis

    @property
    def creator_id(self):
        """Gets the creator_id of this SpanSamplingPolicy.  # noqa: E501

        Creator user of the span sampling policy  # noqa: E501

        :return: The creator_id of this SpanSamplingPolicy.  # noqa: E501
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this SpanSamplingPolicy.

        Creator user of the span sampling policy  # noqa: E501

        :param creator_id: The creator_id of this SpanSamplingPolicy.  # noqa: E501
        :type: str
        """

        self._creator_id = creator_id

    @property
    def deleted(self):
        """Gets the deleted of this SpanSamplingPolicy.  # noqa: E501

        Whether span sampling policy is soft-deleted, can be modified with delete/undelete api  # noqa: E501

        :return: The deleted of this SpanSamplingPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this SpanSamplingPolicy.

        Whether span sampling policy is soft-deleted, can be modified with delete/undelete api  # noqa: E501

        :param deleted: The deleted of this SpanSamplingPolicy.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def description(self):
        """Gets the description of this SpanSamplingPolicy.  # noqa: E501

        Span sampling policy description  # noqa: E501

        :return: The description of this SpanSamplingPolicy.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SpanSamplingPolicy.

        Span sampling policy description  # noqa: E501

        :param description: The description of this SpanSamplingPolicy.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def expression(self):
        """Gets the expression of this SpanSamplingPolicy.  # noqa: E501

        Span sampling policy expression  # noqa: E501

        :return: The expression of this SpanSamplingPolicy.  # noqa: E501
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """Sets the expression of this SpanSamplingPolicy.

        Span sampling policy expression  # noqa: E501

        :param expression: The expression of this SpanSamplingPolicy.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and expression is None:
            raise ValueError("Invalid value for `expression`, must not be `None`")  # noqa: E501

        self._expression = expression

    @property
    def id(self):
        """Gets the id of this SpanSamplingPolicy.  # noqa: E501

        Unique identifier of the span sampling policy  # noqa: E501

        :return: The id of this SpanSamplingPolicy.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SpanSamplingPolicy.

        Unique identifier of the span sampling policy  # noqa: E501

        :param id: The id of this SpanSamplingPolicy.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this SpanSamplingPolicy.  # noqa: E501

        Span sampling policy name  # noqa: E501

        :return: The name of this SpanSamplingPolicy.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SpanSamplingPolicy.

        Span sampling policy name  # noqa: E501

        :param name: The name of this SpanSamplingPolicy.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def sampling_percent(self):
        """Gets the sampling_percent of this SpanSamplingPolicy.  # noqa: E501

        Sampling percent of policy, 100 means keeping all the spans that matches the policy  # noqa: E501

        :return: The sampling_percent of this SpanSamplingPolicy.  # noqa: E501
        :rtype: int
        """
        return self._sampling_percent

    @sampling_percent.setter
    def sampling_percent(self, sampling_percent):
        """Sets the sampling_percent of this SpanSamplingPolicy.

        Sampling percent of policy, 100 means keeping all the spans that matches the policy  # noqa: E501

        :param sampling_percent: The sampling_percent of this SpanSamplingPolicy.  # noqa: E501
        :type: int
        """

        self._sampling_percent = sampling_percent

    @property
    def updated_epoch_millis(self):
        """Gets the updated_epoch_millis of this SpanSamplingPolicy.  # noqa: E501

        Last updated time of the span sampling policy  # noqa: E501

        :return: The updated_epoch_millis of this SpanSamplingPolicy.  # noqa: E501
        :rtype: int
        """
        return self._updated_epoch_millis

    @updated_epoch_millis.setter
    def updated_epoch_millis(self, updated_epoch_millis):
        """Sets the updated_epoch_millis of this SpanSamplingPolicy.

        Last updated time of the span sampling policy  # noqa: E501

        :param updated_epoch_millis: The updated_epoch_millis of this SpanSamplingPolicy.  # noqa: E501
        :type: int
        """

        self._updated_epoch_millis = updated_epoch_millis

    @property
    def updater_id(self):
        """Gets the updater_id of this SpanSamplingPolicy.  # noqa: E501

        Updater user of the span sampling policy  # noqa: E501

        :return: The updater_id of this SpanSamplingPolicy.  # noqa: E501
        :rtype: str
        """
        return self._updater_id

    @updater_id.setter
    def updater_id(self, updater_id):
        """Sets the updater_id of this SpanSamplingPolicy.

        Updater user of the span sampling policy  # noqa: E501

        :param updater_id: The updater_id of this SpanSamplingPolicy.  # noqa: E501
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
        if issubclass(SpanSamplingPolicy, dict):
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
        if not isinstance(other, SpanSamplingPolicy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SpanSamplingPolicy):
            return True

        return self.to_dict() != other.to_dict()
