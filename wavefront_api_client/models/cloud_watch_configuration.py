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


class CloudWatchConfiguration(object):
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
        'base_credentials': 'AWSBaseCredentials',
        'instance_selection_tags': 'dict(str, str)',
        'instance_selection_tags_expr': 'str',
        'metric_filter_regex': 'str',
        'namespaces': 'list[str]',
        'point_tag_filter_regex': 'str',
        's3_bucket_name_filter_regex': 'str',
        'thread_distribution_in_mins': 'int',
        'volume_selection_tags': 'dict(str, str)',
        'volume_selection_tags_expr': 'str'
    }

    attribute_map = {
        'base_credentials': 'baseCredentials',
        'instance_selection_tags': 'instanceSelectionTags',
        'instance_selection_tags_expr': 'instanceSelectionTagsExpr',
        'metric_filter_regex': 'metricFilterRegex',
        'namespaces': 'namespaces',
        'point_tag_filter_regex': 'pointTagFilterRegex',
        's3_bucket_name_filter_regex': 's3BucketNameFilterRegex',
        'thread_distribution_in_mins': 'threadDistributionInMins',
        'volume_selection_tags': 'volumeSelectionTags',
        'volume_selection_tags_expr': 'volumeSelectionTagsExpr'
    }

    def __init__(self, base_credentials=None, instance_selection_tags=None, instance_selection_tags_expr=None, metric_filter_regex=None, namespaces=None, point_tag_filter_regex=None, s3_bucket_name_filter_regex=None, thread_distribution_in_mins=None, volume_selection_tags=None, volume_selection_tags_expr=None, _configuration=None):  # noqa: E501
        """CloudWatchConfiguration - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._base_credentials = None
        self._instance_selection_tags = None
        self._instance_selection_tags_expr = None
        self._metric_filter_regex = None
        self._namespaces = None
        self._point_tag_filter_regex = None
        self._s3_bucket_name_filter_regex = None
        self._thread_distribution_in_mins = None
        self._volume_selection_tags = None
        self._volume_selection_tags_expr = None
        self.discriminator = None

        if base_credentials is not None:
            self.base_credentials = base_credentials
        if instance_selection_tags is not None:
            self.instance_selection_tags = instance_selection_tags
        if instance_selection_tags_expr is not None:
            self.instance_selection_tags_expr = instance_selection_tags_expr
        if metric_filter_regex is not None:
            self.metric_filter_regex = metric_filter_regex
        if namespaces is not None:
            self.namespaces = namespaces
        if point_tag_filter_regex is not None:
            self.point_tag_filter_regex = point_tag_filter_regex
        if s3_bucket_name_filter_regex is not None:
            self.s3_bucket_name_filter_regex = s3_bucket_name_filter_regex
        if thread_distribution_in_mins is not None:
            self.thread_distribution_in_mins = thread_distribution_in_mins
        if volume_selection_tags is not None:
            self.volume_selection_tags = volume_selection_tags
        if volume_selection_tags_expr is not None:
            self.volume_selection_tags_expr = volume_selection_tags_expr

    @property
    def base_credentials(self):
        """Gets the base_credentials of this CloudWatchConfiguration.  # noqa: E501


        :return: The base_credentials of this CloudWatchConfiguration.  # noqa: E501
        :rtype: AWSBaseCredentials
        """
        return self._base_credentials

    @base_credentials.setter
    def base_credentials(self, base_credentials):
        """Sets the base_credentials of this CloudWatchConfiguration.


        :param base_credentials: The base_credentials of this CloudWatchConfiguration.  # noqa: E501
        :type: AWSBaseCredentials
        """

        self._base_credentials = base_credentials

    @property
    def instance_selection_tags(self):
        """Gets the instance_selection_tags of this CloudWatchConfiguration.  # noqa: E501

        A string->string map of allow list of AWS instance tag-value pairs (in AWS).  If the instance's AWS tags match this allow list, CloudWatch data about this instance is ingested.  Multiple entries are OR'ed  # noqa: E501

        :return: The instance_selection_tags of this CloudWatchConfiguration.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._instance_selection_tags

    @instance_selection_tags.setter
    def instance_selection_tags(self, instance_selection_tags):
        """Sets the instance_selection_tags of this CloudWatchConfiguration.

        A string->string map of allow list of AWS instance tag-value pairs (in AWS).  If the instance's AWS tags match this allow list, CloudWatch data about this instance is ingested.  Multiple entries are OR'ed  # noqa: E501

        :param instance_selection_tags: The instance_selection_tags of this CloudWatchConfiguration.  # noqa: E501
        :type: dict(str, str)
        """

        self._instance_selection_tags = instance_selection_tags

    @property
    def instance_selection_tags_expr(self):
        """Gets the instance_selection_tags_expr of this CloudWatchConfiguration.  # noqa: E501

        A string expressing the allow list of AWS instance tag-value pairs.  If the instance's AWS tags match this allow list, CloudWatch data about this instance is ingested.  Multiple entries are OR'ed and also OR'ed with entries from instanceSelectionTags.  Key-value pairs in the string are separated by commas and in the form k=v.  Example: \"k1=v1, k1=v2, k3=v3\".  # noqa: E501

        :return: The instance_selection_tags_expr of this CloudWatchConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._instance_selection_tags_expr

    @instance_selection_tags_expr.setter
    def instance_selection_tags_expr(self, instance_selection_tags_expr):
        """Sets the instance_selection_tags_expr of this CloudWatchConfiguration.

        A string expressing the allow list of AWS instance tag-value pairs.  If the instance's AWS tags match this allow list, CloudWatch data about this instance is ingested.  Multiple entries are OR'ed and also OR'ed with entries from instanceSelectionTags.  Key-value pairs in the string are separated by commas and in the form k=v.  Example: \"k1=v1, k1=v2, k3=v3\".  # noqa: E501

        :param instance_selection_tags_expr: The instance_selection_tags_expr of this CloudWatchConfiguration.  # noqa: E501
        :type: str
        """

        self._instance_selection_tags_expr = instance_selection_tags_expr

    @property
    def metric_filter_regex(self):
        """Gets the metric_filter_regex of this CloudWatchConfiguration.  # noqa: E501

        A regular expression that a CloudWatch metric name must match (case-insensitively) in order to be ingested  # noqa: E501

        :return: The metric_filter_regex of this CloudWatchConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._metric_filter_regex

    @metric_filter_regex.setter
    def metric_filter_regex(self, metric_filter_regex):
        """Sets the metric_filter_regex of this CloudWatchConfiguration.

        A regular expression that a CloudWatch metric name must match (case-insensitively) in order to be ingested  # noqa: E501

        :param metric_filter_regex: The metric_filter_regex of this CloudWatchConfiguration.  # noqa: E501
        :type: str
        """

        self._metric_filter_regex = metric_filter_regex

    @property
    def namespaces(self):
        """Gets the namespaces of this CloudWatchConfiguration.  # noqa: E501

        A list of namespace that limit what we query from CloudWatch.  # noqa: E501

        :return: The namespaces of this CloudWatchConfiguration.  # noqa: E501
        :rtype: list[str]
        """
        return self._namespaces

    @namespaces.setter
    def namespaces(self, namespaces):
        """Sets the namespaces of this CloudWatchConfiguration.

        A list of namespace that limit what we query from CloudWatch.  # noqa: E501

        :param namespaces: The namespaces of this CloudWatchConfiguration.  # noqa: E501
        :type: list[str]
        """

        self._namespaces = namespaces

    @property
    def point_tag_filter_regex(self):
        """Gets the point_tag_filter_regex of this CloudWatchConfiguration.  # noqa: E501

        A regular expression that AWS tag key name must match (case-insensitively) in order to be ingested  # noqa: E501

        :return: The point_tag_filter_regex of this CloudWatchConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._point_tag_filter_regex

    @point_tag_filter_regex.setter
    def point_tag_filter_regex(self, point_tag_filter_regex):
        """Sets the point_tag_filter_regex of this CloudWatchConfiguration.

        A regular expression that AWS tag key name must match (case-insensitively) in order to be ingested  # noqa: E501

        :param point_tag_filter_regex: The point_tag_filter_regex of this CloudWatchConfiguration.  # noqa: E501
        :type: str
        """

        self._point_tag_filter_regex = point_tag_filter_regex

    @property
    def s3_bucket_name_filter_regex(self):
        """Gets the s3_bucket_name_filter_regex of this CloudWatchConfiguration.  # noqa: E501

        A regular expression that a AWS S3 Bucket name must match (case-insensitively) in order to be ingested  # noqa: E501

        :return: The s3_bucket_name_filter_regex of this CloudWatchConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._s3_bucket_name_filter_regex

    @s3_bucket_name_filter_regex.setter
    def s3_bucket_name_filter_regex(self, s3_bucket_name_filter_regex):
        """Sets the s3_bucket_name_filter_regex of this CloudWatchConfiguration.

        A regular expression that a AWS S3 Bucket name must match (case-insensitively) in order to be ingested  # noqa: E501

        :param s3_bucket_name_filter_regex: The s3_bucket_name_filter_regex of this CloudWatchConfiguration.  # noqa: E501
        :type: str
        """

        self._s3_bucket_name_filter_regex = s3_bucket_name_filter_regex

    @property
    def thread_distribution_in_mins(self):
        """Gets the thread_distribution_in_mins of this CloudWatchConfiguration.  # noqa: E501

        ThreadDistributionInMins  # noqa: E501

        :return: The thread_distribution_in_mins of this CloudWatchConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._thread_distribution_in_mins

    @thread_distribution_in_mins.setter
    def thread_distribution_in_mins(self, thread_distribution_in_mins):
        """Sets the thread_distribution_in_mins of this CloudWatchConfiguration.

        ThreadDistributionInMins  # noqa: E501

        :param thread_distribution_in_mins: The thread_distribution_in_mins of this CloudWatchConfiguration.  # noqa: E501
        :type: int
        """

        self._thread_distribution_in_mins = thread_distribution_in_mins

    @property
    def volume_selection_tags(self):
        """Gets the volume_selection_tags of this CloudWatchConfiguration.  # noqa: E501

        A string->string map of allow list of AWS volume tag-value pairs (in AWS).  If the volume's AWS tags match this allow list, CloudWatch data about this volume is ingested.  Multiple entries are OR'ed  # noqa: E501

        :return: The volume_selection_tags of this CloudWatchConfiguration.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._volume_selection_tags

    @volume_selection_tags.setter
    def volume_selection_tags(self, volume_selection_tags):
        """Sets the volume_selection_tags of this CloudWatchConfiguration.

        A string->string map of allow list of AWS volume tag-value pairs (in AWS).  If the volume's AWS tags match this allow list, CloudWatch data about this volume is ingested.  Multiple entries are OR'ed  # noqa: E501

        :param volume_selection_tags: The volume_selection_tags of this CloudWatchConfiguration.  # noqa: E501
        :type: dict(str, str)
        """

        self._volume_selection_tags = volume_selection_tags

    @property
    def volume_selection_tags_expr(self):
        """Gets the volume_selection_tags_expr of this CloudWatchConfiguration.  # noqa: E501

        A string expressing the allow list of AWS volume tag-value pairs.  If the volume's AWS tags match this allow list, CloudWatch data about this volume is ingested.  Multiple entries are OR'ed and also OR'ed with entries from volumeSelectionTags.  Key-value pairs in the string are separated by commas and in the form k=v.  Example: \"k1=v1, k1=v2, k3=v3\".  # noqa: E501

        :return: The volume_selection_tags_expr of this CloudWatchConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._volume_selection_tags_expr

    @volume_selection_tags_expr.setter
    def volume_selection_tags_expr(self, volume_selection_tags_expr):
        """Sets the volume_selection_tags_expr of this CloudWatchConfiguration.

        A string expressing the allow list of AWS volume tag-value pairs.  If the volume's AWS tags match this allow list, CloudWatch data about this volume is ingested.  Multiple entries are OR'ed and also OR'ed with entries from volumeSelectionTags.  Key-value pairs in the string are separated by commas and in the form k=v.  Example: \"k1=v1, k1=v2, k3=v3\".  # noqa: E501

        :param volume_selection_tags_expr: The volume_selection_tags_expr of this CloudWatchConfiguration.  # noqa: E501
        :type: str
        """

        self._volume_selection_tags_expr = volume_selection_tags_expr

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
        if issubclass(CloudWatchConfiguration, dict):
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
        if not isinstance(other, CloudWatchConfiguration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CloudWatchConfiguration):
            return True

        return self.to_dict() != other.to_dict()
