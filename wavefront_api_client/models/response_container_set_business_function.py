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


class ResponseContainerSetBusinessFunction(object):
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
        'response': 'list[str]',
        'status': 'ResponseStatus'
    }

    attribute_map = {
        'response': 'response',
        'status': 'status'
    }

    def __init__(self, response=None, status=None, _configuration=None):  # noqa: E501
        """ResponseContainerSetBusinessFunction - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._response = None
        self._status = None
        self.discriminator = None

        if response is not None:
            self.response = response
        self.status = status

    @property
    def response(self):
        """Gets the response of this ResponseContainerSetBusinessFunction.  # noqa: E501


        :return: The response of this ResponseContainerSetBusinessFunction.  # noqa: E501
        :rtype: list[str]
        """
        return self._response

    @response.setter
    def response(self, response):
        """Sets the response of this ResponseContainerSetBusinessFunction.


        :param response: The response of this ResponseContainerSetBusinessFunction.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["VIEW_MONITORED_APPLICATION_SERVICE", "VIEW_MONITORED_CLUSTER", "VIEW_MONITORED_CLUSTER_TAGS", "VIEW_DASHBOARDS", "VIEW_DASHBOARDS_TAGS", "VIEW_METRIC_TIMESERIES", "VIEW_HOSTS", "VIEW_HOST_TAGS", "VIEW_AGENT_TAGS", "VIEW_EVENTS", "VIEW_EVENT_TAGS", "VIEW_ALERTS", "VIEW_ALERT_TAGS", "VIEW_REGISTERED_QUERIES", "VIEW_REGISTERED_QUERY_TAGS", "VIEW_MAINTENANCE_WINDOWS", "VIEW_NOTIFICANTS", "VIEW_CUSTOM_METRICS", "VIEW_TARGETS", "VIEW_AGENTS", "VIEW_SSH_CONFIGS", "VIEW_EXTERNAL_SERVICES", "VIEW_EXTERNAL_SERVICES_TAGS", "VIEW_EXTERNAL_LINKS", "VIEW_EXTERNAL_LINK_DIGESTS", "VIEW_EXTERNAL_LINK_TAGS", "VIEW_LOGS", "VIEW_SLOW_QUERY_PAGE", "VIEW_SAVED_SEARCHES", "VIEW_MY_MESSAGES", "VIEW_APPLICATIONS", "VIEW_ANOMALY", "SPY_ON_POINTS", "SPY_ON_ID_CREATIONS", "SPY_UNUSED_METRICS", "VIEW_SAML_SSO_SETTINGS", "VIEW_INGESTION_POLICY", "VIEW_CLUSTER_INFO", "MODIFY_MONITORED_APPLICATION_SERVICE", "MODIFY_MONITORED_CLUSTER", "MODIFY_MONITORED_CLUSTER_TAGS", "MODIFY_PRIVATE_TAGS", "MODIFY_CUSTOM_METRICS", "MODIFY_DASHBOARDS", "MODIFY_EVENTS", "MODIFY_EVENT_TAGS", "MODIFY_AGENTS", "MODIFY_AGENT_TAGS", "MODIFY_HOSTS", "MODIFY_HOST_TAGS", "MODIFY_MACHINES", "MODIFY_SSH_CONFIGS", "MODIFY_ALERTS", "MODIFY_ALERT_TAGS", "MODIFY_REGISTERED_QUERIES", "MODIFY_REGISTERED_QUERY_TAGS", "MODIFY_MAINTENANCE_WINDOWS", "MODIFY_NOTIFICANTS", "MODIFY_DASHBOARD_TAGS", "MODIFY_TARGETS", "MODIFY_EXTERNAL_SERVICES", "MODIFY_EXTERNAL_SERVICES_TAGS", "CREATE_EMBEDDED_CHARTS", "MODIFY_METRIC_VISIBILITY", "MODIFY_EXTERNAL_LINKS", "MODIFY_EXTERNAL_LINK_TAGS", "MODIFY_SAVED_SEARCHES", "MODIFY_SAVED_TRACES_SEARCH", "MODIFY_OWN_ONBOARDING_STATE", "MODIFY_APPLICATIONS", "INGESTION_POLICY_MANAGEMENT", "METRICS_POLICY_MANAGEMENT", "MODIFY_SAML_SSO_SETTINGS", "METRIC_INGESTION", "METRIC_INGESTION_LISTENER", "LOGIN", "LOGOUT", "CHANGE_PASSWORD", "SEND_FORGOTTEN_PASSWORD_EMAILS", "CHANGE_USER_PREFERENCE", "CREATE_TOKEN", "REVOKE_ALL_SESSIONS", "REVOKE_ALL_TOKENS", "REVOKE_TOKEN", "GET_TOKENS", "GET_ALL_ACCOUNTS", "GET_ALL_USERS", "GET_ALL_SERVICE_ACCOUNTS", "ADMINISTER_GROUPS", "DELETE_ACCOUNT", "INVITE_USER", "ADMINISTER_SERVICE_ACCOUNTS", "NO_REAUTH_INVITE_USER", "ADMINISTER_USER_GROUPS", "ADMINISTER_ALL_TOKENS", "ADMINISTER_CUSTOMER_PREFERENCES", "ROLES_MANAGEMENT", "VIEW_CUSTOMERS", "MODIFY_CUSTOMER", "DELETE_CUSTOMER", "SEND_UI_METRICS", "TOKEN"]  # noqa: E501
        if (self._configuration.client_side_validation and
                not set(response).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `response` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(response) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._response = response

    @property
    def status(self):
        """Gets the status of this ResponseContainerSetBusinessFunction.  # noqa: E501


        :return: The status of this ResponseContainerSetBusinessFunction.  # noqa: E501
        :rtype: ResponseStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ResponseContainerSetBusinessFunction.


        :param status: The status of this ResponseContainerSetBusinessFunction.  # noqa: E501
        :type: ResponseStatus
        """
        if self._configuration.client_side_validation and status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

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
        if issubclass(ResponseContainerSetBusinessFunction, dict):
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
        if not isinstance(other, ResponseContainerSetBusinessFunction):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResponseContainerSetBusinessFunction):
            return True

        return self.to_dict() != other.to_dict()
