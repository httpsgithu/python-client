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


class MonitoredApplicationDTO(object):
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
        'application': 'str',
        'created': 'int',
        'hidden': 'bool',
        'last_reported': 'int',
        'last_updated': 'int',
        'satisfied_latency_millis': 'int',
        'service_count': 'int',
        'status': 'str',
        'update_user_id': 'str'
    }

    attribute_map = {
        'application': 'application',
        'created': 'created',
        'hidden': 'hidden',
        'last_reported': 'lastReported',
        'last_updated': 'lastUpdated',
        'satisfied_latency_millis': 'satisfiedLatencyMillis',
        'service_count': 'serviceCount',
        'status': 'status',
        'update_user_id': 'updateUserId'
    }

    def __init__(self, application=None, created=None, hidden=None, last_reported=None, last_updated=None, satisfied_latency_millis=None, service_count=None, status=None, update_user_id=None, _configuration=None):  # noqa: E501
        """MonitoredApplicationDTO - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._application = None
        self._created = None
        self._hidden = None
        self._last_reported = None
        self._last_updated = None
        self._satisfied_latency_millis = None
        self._service_count = None
        self._status = None
        self._update_user_id = None
        self.discriminator = None

        self.application = application
        if created is not None:
            self.created = created
        if hidden is not None:
            self.hidden = hidden
        if last_reported is not None:
            self.last_reported = last_reported
        if last_updated is not None:
            self.last_updated = last_updated
        if satisfied_latency_millis is not None:
            self.satisfied_latency_millis = satisfied_latency_millis
        if service_count is not None:
            self.service_count = service_count
        if status is not None:
            self.status = status
        if update_user_id is not None:
            self.update_user_id = update_user_id

    @property
    def application(self):
        """Gets the application of this MonitoredApplicationDTO.  # noqa: E501

        Application Name of the monitored application  # noqa: E501

        :return: The application of this MonitoredApplicationDTO.  # noqa: E501
        :rtype: str
        """
        return self._application

    @application.setter
    def application(self, application):
        """Sets the application of this MonitoredApplicationDTO.

        Application Name of the monitored application  # noqa: E501

        :param application: The application of this MonitoredApplicationDTO.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and application is None:
            raise ValueError("Invalid value for `application`, must not be `None`")  # noqa: E501

        self._application = application

    @property
    def created(self):
        """Gets the created of this MonitoredApplicationDTO.  # noqa: E501

        Created epoch of monitored application  # noqa: E501

        :return: The created of this MonitoredApplicationDTO.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this MonitoredApplicationDTO.

        Created epoch of monitored application  # noqa: E501

        :param created: The created of this MonitoredApplicationDTO.  # noqa: E501
        :type: int
        """

        self._created = created

    @property
    def hidden(self):
        """Gets the hidden of this MonitoredApplicationDTO.  # noqa: E501

        Monitored application is hidden or not  # noqa: E501

        :return: The hidden of this MonitoredApplicationDTO.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this MonitoredApplicationDTO.

        Monitored application is hidden or not  # noqa: E501

        :param hidden: The hidden of this MonitoredApplicationDTO.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

    @property
    def last_reported(self):
        """Gets the last_reported of this MonitoredApplicationDTO.  # noqa: E501

        Last reported epoch of monitored application  # noqa: E501

        :return: The last_reported of this MonitoredApplicationDTO.  # noqa: E501
        :rtype: int
        """
        return self._last_reported

    @last_reported.setter
    def last_reported(self, last_reported):
        """Sets the last_reported of this MonitoredApplicationDTO.

        Last reported epoch of monitored application  # noqa: E501

        :param last_reported: The last_reported of this MonitoredApplicationDTO.  # noqa: E501
        :type: int
        """

        self._last_reported = last_reported

    @property
    def last_updated(self):
        """Gets the last_updated of this MonitoredApplicationDTO.  # noqa: E501

        Last update epoch of monitored application  # noqa: E501

        :return: The last_updated of this MonitoredApplicationDTO.  # noqa: E501
        :rtype: int
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this MonitoredApplicationDTO.

        Last update epoch of monitored application  # noqa: E501

        :param last_updated: The last_updated of this MonitoredApplicationDTO.  # noqa: E501
        :type: int
        """

        self._last_updated = last_updated

    @property
    def satisfied_latency_millis(self):
        """Gets the satisfied_latency_millis of this MonitoredApplicationDTO.  # noqa: E501

        Satisfied latency of monitored application  # noqa: E501

        :return: The satisfied_latency_millis of this MonitoredApplicationDTO.  # noqa: E501
        :rtype: int
        """
        return self._satisfied_latency_millis

    @satisfied_latency_millis.setter
    def satisfied_latency_millis(self, satisfied_latency_millis):
        """Sets the satisfied_latency_millis of this MonitoredApplicationDTO.

        Satisfied latency of monitored application  # noqa: E501

        :param satisfied_latency_millis: The satisfied_latency_millis of this MonitoredApplicationDTO.  # noqa: E501
        :type: int
        """

        self._satisfied_latency_millis = satisfied_latency_millis

    @property
    def service_count(self):
        """Gets the service_count of this MonitoredApplicationDTO.  # noqa: E501

        Number of monitored service of monitored application  # noqa: E501

        :return: The service_count of this MonitoredApplicationDTO.  # noqa: E501
        :rtype: int
        """
        return self._service_count

    @service_count.setter
    def service_count(self, service_count):
        """Sets the service_count of this MonitoredApplicationDTO.

        Number of monitored service of monitored application  # noqa: E501

        :param service_count: The service_count of this MonitoredApplicationDTO.  # noqa: E501
        :type: int
        """

        self._service_count = service_count

    @property
    def status(self):
        """Gets the status of this MonitoredApplicationDTO.  # noqa: E501

        Status of monitored application  # noqa: E501

        :return: The status of this MonitoredApplicationDTO.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MonitoredApplicationDTO.

        Status of monitored application  # noqa: E501

        :param status: The status of this MonitoredApplicationDTO.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE", "INACTIVE"]  # noqa: E501
        if (self._configuration.client_side_validation and
                status not in allowed_values):
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def update_user_id(self):
        """Gets the update_user_id of this MonitoredApplicationDTO.  # noqa: E501

        Last update user id of monitored application  # noqa: E501

        :return: The update_user_id of this MonitoredApplicationDTO.  # noqa: E501
        :rtype: str
        """
        return self._update_user_id

    @update_user_id.setter
    def update_user_id(self, update_user_id):
        """Sets the update_user_id of this MonitoredApplicationDTO.

        Last update user id of monitored application  # noqa: E501

        :param update_user_id: The update_user_id of this MonitoredApplicationDTO.  # noqa: E501
        :type: str
        """

        self._update_user_id = update_user_id

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
        if issubclass(MonitoredApplicationDTO, dict):
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
        if not isinstance(other, MonitoredApplicationDTO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MonitoredApplicationDTO):
            return True

        return self.to_dict() != other.to_dict()
