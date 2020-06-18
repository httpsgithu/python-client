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


class ExternalLink(object):
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
        'id': 'str',
        'is_log_integration': 'bool',
        'metric_filter_regex': 'str',
        'name': 'str',
        'point_tag_filter_regexes': 'dict(str, str)',
        'source_filter_regex': 'str',
        'template': 'str',
        'updated_epoch_millis': 'int',
        'updater_id': 'str'
    }

    attribute_map = {
        'created_epoch_millis': 'createdEpochMillis',
        'creator_id': 'creatorId',
        'description': 'description',
        'id': 'id',
        'is_log_integration': 'isLogIntegration',
        'metric_filter_regex': 'metricFilterRegex',
        'name': 'name',
        'point_tag_filter_regexes': 'pointTagFilterRegexes',
        'source_filter_regex': 'sourceFilterRegex',
        'template': 'template',
        'updated_epoch_millis': 'updatedEpochMillis',
        'updater_id': 'updaterId'
    }

    def __init__(self, created_epoch_millis=None, creator_id=None, description=None, id=None, is_log_integration=None, metric_filter_regex=None, name=None, point_tag_filter_regexes=None, source_filter_regex=None, template=None, updated_epoch_millis=None, updater_id=None):  # noqa: E501
        """ExternalLink - a model defined in Swagger"""  # noqa: E501

        self._created_epoch_millis = None
        self._creator_id = None
        self._description = None
        self._id = None
        self._is_log_integration = None
        self._metric_filter_regex = None
        self._name = None
        self._point_tag_filter_regexes = None
        self._source_filter_regex = None
        self._template = None
        self._updated_epoch_millis = None
        self._updater_id = None
        self.discriminator = None

        if created_epoch_millis is not None:
            self.created_epoch_millis = created_epoch_millis
        if creator_id is not None:
            self.creator_id = creator_id
        self.description = description
        if id is not None:
            self.id = id
        if is_log_integration is not None:
            self.is_log_integration = is_log_integration
        if metric_filter_regex is not None:
            self.metric_filter_regex = metric_filter_regex
        self.name = name
        if point_tag_filter_regexes is not None:
            self.point_tag_filter_regexes = point_tag_filter_regexes
        if source_filter_regex is not None:
            self.source_filter_regex = source_filter_regex
        self.template = template
        if updated_epoch_millis is not None:
            self.updated_epoch_millis = updated_epoch_millis
        if updater_id is not None:
            self.updater_id = updater_id

    @property
    def created_epoch_millis(self):
        """Gets the created_epoch_millis of this ExternalLink.  # noqa: E501


        :return: The created_epoch_millis of this ExternalLink.  # noqa: E501
        :rtype: int
        """
        return self._created_epoch_millis

    @created_epoch_millis.setter
    def created_epoch_millis(self, created_epoch_millis):
        """Sets the created_epoch_millis of this ExternalLink.


        :param created_epoch_millis: The created_epoch_millis of this ExternalLink.  # noqa: E501
        :type: int
        """

        self._created_epoch_millis = created_epoch_millis

    @property
    def creator_id(self):
        """Gets the creator_id of this ExternalLink.  # noqa: E501


        :return: The creator_id of this ExternalLink.  # noqa: E501
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this ExternalLink.


        :param creator_id: The creator_id of this ExternalLink.  # noqa: E501
        :type: str
        """

        self._creator_id = creator_id

    @property
    def description(self):
        """Gets the description of this ExternalLink.  # noqa: E501

        Human-readable description for this external link  # noqa: E501

        :return: The description of this ExternalLink.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ExternalLink.

        Human-readable description for this external link  # noqa: E501

        :param description: The description of this ExternalLink.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def id(self):
        """Gets the id of this ExternalLink.  # noqa: E501


        :return: The id of this ExternalLink.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExternalLink.


        :param id: The id of this ExternalLink.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def is_log_integration(self):
        """Gets the is_log_integration of this ExternalLink.  # noqa: E501

        Whether this is a \"Log Integration\" subType of external link  # noqa: E501

        :return: The is_log_integration of this ExternalLink.  # noqa: E501
        :rtype: bool
        """
        return self._is_log_integration

    @is_log_integration.setter
    def is_log_integration(self, is_log_integration):
        """Sets the is_log_integration of this ExternalLink.

        Whether this is a \"Log Integration\" subType of external link  # noqa: E501

        :param is_log_integration: The is_log_integration of this ExternalLink.  # noqa: E501
        :type: bool
        """

        self._is_log_integration = is_log_integration

    @property
    def metric_filter_regex(self):
        """Gets the metric_filter_regex of this ExternalLink.  # noqa: E501

        Controls whether a link displayed in the context menu of a highlighted series.  If present, the metric name of the highlighted series must match this regular expression in order for the link to be displayed  # noqa: E501

        :return: The metric_filter_regex of this ExternalLink.  # noqa: E501
        :rtype: str
        """
        return self._metric_filter_regex

    @metric_filter_regex.setter
    def metric_filter_regex(self, metric_filter_regex):
        """Sets the metric_filter_regex of this ExternalLink.

        Controls whether a link displayed in the context menu of a highlighted series.  If present, the metric name of the highlighted series must match this regular expression in order for the link to be displayed  # noqa: E501

        :param metric_filter_regex: The metric_filter_regex of this ExternalLink.  # noqa: E501
        :type: str
        """

        self._metric_filter_regex = metric_filter_regex

    @property
    def name(self):
        """Gets the name of this ExternalLink.  # noqa: E501

        Name of the external link.  Will be displayed in context (right-click) menus on charts  # noqa: E501

        :return: The name of this ExternalLink.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ExternalLink.

        Name of the external link.  Will be displayed in context (right-click) menus on charts  # noqa: E501

        :param name: The name of this ExternalLink.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def point_tag_filter_regexes(self):
        """Gets the point_tag_filter_regexes of this ExternalLink.  # noqa: E501

        Controls whether a link displayed in the context menu of a highlighted series.  This is a map from string to regular expression. The highlighted series must contain point tags whose keys are present in the keys of this map and whose values match the regular expressions associated with those keys in order for the link to be displayed  # noqa: E501

        :return: The point_tag_filter_regexes of this ExternalLink.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._point_tag_filter_regexes

    @point_tag_filter_regexes.setter
    def point_tag_filter_regexes(self, point_tag_filter_regexes):
        """Sets the point_tag_filter_regexes of this ExternalLink.

        Controls whether a link displayed in the context menu of a highlighted series.  This is a map from string to regular expression. The highlighted series must contain point tags whose keys are present in the keys of this map and whose values match the regular expressions associated with those keys in order for the link to be displayed  # noqa: E501

        :param point_tag_filter_regexes: The point_tag_filter_regexes of this ExternalLink.  # noqa: E501
        :type: dict(str, str)
        """

        self._point_tag_filter_regexes = point_tag_filter_regexes

    @property
    def source_filter_regex(self):
        """Gets the source_filter_regex of this ExternalLink.  # noqa: E501

        Controls whether a link displayed in the context menu of a highlighted series.  If present, the source name of the highlighted series must match this regular expression in order for the link to be displayed  # noqa: E501

        :return: The source_filter_regex of this ExternalLink.  # noqa: E501
        :rtype: str
        """
        return self._source_filter_regex

    @source_filter_regex.setter
    def source_filter_regex(self, source_filter_regex):
        """Sets the source_filter_regex of this ExternalLink.

        Controls whether a link displayed in the context menu of a highlighted series.  If present, the source name of the highlighted series must match this regular expression in order for the link to be displayed  # noqa: E501

        :param source_filter_regex: The source_filter_regex of this ExternalLink.  # noqa: E501
        :type: str
        """

        self._source_filter_regex = source_filter_regex

    @property
    def template(self):
        """Gets the template of this ExternalLink.  # noqa: E501

        The mustache template for this link.  This template must expand to a full URL, including scheme, origin, etc  # noqa: E501

        :return: The template of this ExternalLink.  # noqa: E501
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this ExternalLink.

        The mustache template for this link.  This template must expand to a full URL, including scheme, origin, etc  # noqa: E501

        :param template: The template of this ExternalLink.  # noqa: E501
        :type: str
        """
        if template is None:
            raise ValueError("Invalid value for `template`, must not be `None`")  # noqa: E501

        self._template = template

    @property
    def updated_epoch_millis(self):
        """Gets the updated_epoch_millis of this ExternalLink.  # noqa: E501


        :return: The updated_epoch_millis of this ExternalLink.  # noqa: E501
        :rtype: int
        """
        return self._updated_epoch_millis

    @updated_epoch_millis.setter
    def updated_epoch_millis(self, updated_epoch_millis):
        """Sets the updated_epoch_millis of this ExternalLink.


        :param updated_epoch_millis: The updated_epoch_millis of this ExternalLink.  # noqa: E501
        :type: int
        """

        self._updated_epoch_millis = updated_epoch_millis

    @property
    def updater_id(self):
        """Gets the updater_id of this ExternalLink.  # noqa: E501


        :return: The updater_id of this ExternalLink.  # noqa: E501
        :rtype: str
        """
        return self._updater_id

    @updater_id.setter
    def updater_id(self, updater_id):
        """Sets the updater_id of this ExternalLink.


        :param updater_id: The updater_id of this ExternalLink.  # noqa: E501
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
        if issubclass(ExternalLink, dict):
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
        if not isinstance(other, ExternalLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
