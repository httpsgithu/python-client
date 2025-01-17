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


class AppDynamicsConfiguration(object):
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
        'app_filter_regex': 'list[str]',
        'controller_name': 'str',
        'enable_app_infra_metrics': 'bool',
        'enable_backend_metrics': 'bool',
        'enable_business_trx_metrics': 'bool',
        'enable_error_metrics': 'bool',
        'enable_individual_node_metrics': 'bool',
        'enable_overall_perf_metrics': 'bool',
        'enable_rollup': 'bool',
        'enable_service_endpoint_metrics': 'bool',
        'encrypted_password': 'str',
        'user_name': 'str'
    }

    attribute_map = {
        'app_filter_regex': 'appFilterRegex',
        'controller_name': 'controllerName',
        'enable_app_infra_metrics': 'enableAppInfraMetrics',
        'enable_backend_metrics': 'enableBackendMetrics',
        'enable_business_trx_metrics': 'enableBusinessTrxMetrics',
        'enable_error_metrics': 'enableErrorMetrics',
        'enable_individual_node_metrics': 'enableIndividualNodeMetrics',
        'enable_overall_perf_metrics': 'enableOverallPerfMetrics',
        'enable_rollup': 'enableRollup',
        'enable_service_endpoint_metrics': 'enableServiceEndpointMetrics',
        'encrypted_password': 'encryptedPassword',
        'user_name': 'userName'
    }

    def __init__(self, app_filter_regex=None, controller_name=None, enable_app_infra_metrics=None, enable_backend_metrics=None, enable_business_trx_metrics=None, enable_error_metrics=None, enable_individual_node_metrics=None, enable_overall_perf_metrics=None, enable_rollup=None, enable_service_endpoint_metrics=None, encrypted_password=None, user_name=None, _configuration=None):  # noqa: E501
        """AppDynamicsConfiguration - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._app_filter_regex = None
        self._controller_name = None
        self._enable_app_infra_metrics = None
        self._enable_backend_metrics = None
        self._enable_business_trx_metrics = None
        self._enable_error_metrics = None
        self._enable_individual_node_metrics = None
        self._enable_overall_perf_metrics = None
        self._enable_rollup = None
        self._enable_service_endpoint_metrics = None
        self._encrypted_password = None
        self._user_name = None
        self.discriminator = None

        if app_filter_regex is not None:
            self.app_filter_regex = app_filter_regex
        self.controller_name = controller_name
        if enable_app_infra_metrics is not None:
            self.enable_app_infra_metrics = enable_app_infra_metrics
        if enable_backend_metrics is not None:
            self.enable_backend_metrics = enable_backend_metrics
        if enable_business_trx_metrics is not None:
            self.enable_business_trx_metrics = enable_business_trx_metrics
        if enable_error_metrics is not None:
            self.enable_error_metrics = enable_error_metrics
        if enable_individual_node_metrics is not None:
            self.enable_individual_node_metrics = enable_individual_node_metrics
        if enable_overall_perf_metrics is not None:
            self.enable_overall_perf_metrics = enable_overall_perf_metrics
        if enable_rollup is not None:
            self.enable_rollup = enable_rollup
        if enable_service_endpoint_metrics is not None:
            self.enable_service_endpoint_metrics = enable_service_endpoint_metrics
        self.encrypted_password = encrypted_password
        self.user_name = user_name

    @property
    def app_filter_regex(self):
        """Gets the app_filter_regex of this AppDynamicsConfiguration.  # noqa: E501

        List of regular expressions that a application name must match (case-insensitively) in order to be ingested.  # noqa: E501

        :return: The app_filter_regex of this AppDynamicsConfiguration.  # noqa: E501
        :rtype: list[str]
        """
        return self._app_filter_regex

    @app_filter_regex.setter
    def app_filter_regex(self, app_filter_regex):
        """Sets the app_filter_regex of this AppDynamicsConfiguration.

        List of regular expressions that a application name must match (case-insensitively) in order to be ingested.  # noqa: E501

        :param app_filter_regex: The app_filter_regex of this AppDynamicsConfiguration.  # noqa: E501
        :type: list[str]
        """

        self._app_filter_regex = app_filter_regex

    @property
    def controller_name(self):
        """Gets the controller_name of this AppDynamicsConfiguration.  # noqa: E501

        Name of the SaaS controller.  # noqa: E501

        :return: The controller_name of this AppDynamicsConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._controller_name

    @controller_name.setter
    def controller_name(self, controller_name):
        """Sets the controller_name of this AppDynamicsConfiguration.

        Name of the SaaS controller.  # noqa: E501

        :param controller_name: The controller_name of this AppDynamicsConfiguration.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and controller_name is None:
            raise ValueError("Invalid value for `controller_name`, must not be `None`")  # noqa: E501

        self._controller_name = controller_name

    @property
    def enable_app_infra_metrics(self):
        """Gets the enable_app_infra_metrics of this AppDynamicsConfiguration.  # noqa: E501

        Boolean flag to control Application Infrastructure metric injection.  # noqa: E501

        :return: The enable_app_infra_metrics of this AppDynamicsConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._enable_app_infra_metrics

    @enable_app_infra_metrics.setter
    def enable_app_infra_metrics(self, enable_app_infra_metrics):
        """Sets the enable_app_infra_metrics of this AppDynamicsConfiguration.

        Boolean flag to control Application Infrastructure metric injection.  # noqa: E501

        :param enable_app_infra_metrics: The enable_app_infra_metrics of this AppDynamicsConfiguration.  # noqa: E501
        :type: bool
        """

        self._enable_app_infra_metrics = enable_app_infra_metrics

    @property
    def enable_backend_metrics(self):
        """Gets the enable_backend_metrics of this AppDynamicsConfiguration.  # noqa: E501

        Boolean flag to control Backend metric injection.  # noqa: E501

        :return: The enable_backend_metrics of this AppDynamicsConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._enable_backend_metrics

    @enable_backend_metrics.setter
    def enable_backend_metrics(self, enable_backend_metrics):
        """Sets the enable_backend_metrics of this AppDynamicsConfiguration.

        Boolean flag to control Backend metric injection.  # noqa: E501

        :param enable_backend_metrics: The enable_backend_metrics of this AppDynamicsConfiguration.  # noqa: E501
        :type: bool
        """

        self._enable_backend_metrics = enable_backend_metrics

    @property
    def enable_business_trx_metrics(self):
        """Gets the enable_business_trx_metrics of this AppDynamicsConfiguration.  # noqa: E501

        Boolean flag to control Business Transaction metric injection.  # noqa: E501

        :return: The enable_business_trx_metrics of this AppDynamicsConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._enable_business_trx_metrics

    @enable_business_trx_metrics.setter
    def enable_business_trx_metrics(self, enable_business_trx_metrics):
        """Sets the enable_business_trx_metrics of this AppDynamicsConfiguration.

        Boolean flag to control Business Transaction metric injection.  # noqa: E501

        :param enable_business_trx_metrics: The enable_business_trx_metrics of this AppDynamicsConfiguration.  # noqa: E501
        :type: bool
        """

        self._enable_business_trx_metrics = enable_business_trx_metrics

    @property
    def enable_error_metrics(self):
        """Gets the enable_error_metrics of this AppDynamicsConfiguration.  # noqa: E501

        Boolean flag to control Error metric injection.  # noqa: E501

        :return: The enable_error_metrics of this AppDynamicsConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._enable_error_metrics

    @enable_error_metrics.setter
    def enable_error_metrics(self, enable_error_metrics):
        """Sets the enable_error_metrics of this AppDynamicsConfiguration.

        Boolean flag to control Error metric injection.  # noqa: E501

        :param enable_error_metrics: The enable_error_metrics of this AppDynamicsConfiguration.  # noqa: E501
        :type: bool
        """

        self._enable_error_metrics = enable_error_metrics

    @property
    def enable_individual_node_metrics(self):
        """Gets the enable_individual_node_metrics of this AppDynamicsConfiguration.  # noqa: E501

        Boolean flag to control Individual Node metric injection.  # noqa: E501

        :return: The enable_individual_node_metrics of this AppDynamicsConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._enable_individual_node_metrics

    @enable_individual_node_metrics.setter
    def enable_individual_node_metrics(self, enable_individual_node_metrics):
        """Sets the enable_individual_node_metrics of this AppDynamicsConfiguration.

        Boolean flag to control Individual Node metric injection.  # noqa: E501

        :param enable_individual_node_metrics: The enable_individual_node_metrics of this AppDynamicsConfiguration.  # noqa: E501
        :type: bool
        """

        self._enable_individual_node_metrics = enable_individual_node_metrics

    @property
    def enable_overall_perf_metrics(self):
        """Gets the enable_overall_perf_metrics of this AppDynamicsConfiguration.  # noqa: E501

        Boolean flag to control Overall Performance metric injection.  # noqa: E501

        :return: The enable_overall_perf_metrics of this AppDynamicsConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._enable_overall_perf_metrics

    @enable_overall_perf_metrics.setter
    def enable_overall_perf_metrics(self, enable_overall_perf_metrics):
        """Sets the enable_overall_perf_metrics of this AppDynamicsConfiguration.

        Boolean flag to control Overall Performance metric injection.  # noqa: E501

        :param enable_overall_perf_metrics: The enable_overall_perf_metrics of this AppDynamicsConfiguration.  # noqa: E501
        :type: bool
        """

        self._enable_overall_perf_metrics = enable_overall_perf_metrics

    @property
    def enable_rollup(self):
        """Gets the enable_rollup of this AppDynamicsConfiguration.  # noqa: E501

        Set this to 'false' to get separate results for all values within the time range, by default it is 'true'.  # noqa: E501

        :return: The enable_rollup of this AppDynamicsConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._enable_rollup

    @enable_rollup.setter
    def enable_rollup(self, enable_rollup):
        """Sets the enable_rollup of this AppDynamicsConfiguration.

        Set this to 'false' to get separate results for all values within the time range, by default it is 'true'.  # noqa: E501

        :param enable_rollup: The enable_rollup of this AppDynamicsConfiguration.  # noqa: E501
        :type: bool
        """

        self._enable_rollup = enable_rollup

    @property
    def enable_service_endpoint_metrics(self):
        """Gets the enable_service_endpoint_metrics of this AppDynamicsConfiguration.  # noqa: E501

        Boolean flag to control Service End point metric injection.  # noqa: E501

        :return: The enable_service_endpoint_metrics of this AppDynamicsConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._enable_service_endpoint_metrics

    @enable_service_endpoint_metrics.setter
    def enable_service_endpoint_metrics(self, enable_service_endpoint_metrics):
        """Sets the enable_service_endpoint_metrics of this AppDynamicsConfiguration.

        Boolean flag to control Service End point metric injection.  # noqa: E501

        :param enable_service_endpoint_metrics: The enable_service_endpoint_metrics of this AppDynamicsConfiguration.  # noqa: E501
        :type: bool
        """

        self._enable_service_endpoint_metrics = enable_service_endpoint_metrics

    @property
    def encrypted_password(self):
        """Gets the encrypted_password of this AppDynamicsConfiguration.  # noqa: E501

        Password for AppDynamics user.  # noqa: E501

        :return: The encrypted_password of this AppDynamicsConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._encrypted_password

    @encrypted_password.setter
    def encrypted_password(self, encrypted_password):
        """Sets the encrypted_password of this AppDynamicsConfiguration.

        Password for AppDynamics user.  # noqa: E501

        :param encrypted_password: The encrypted_password of this AppDynamicsConfiguration.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and encrypted_password is None:
            raise ValueError("Invalid value for `encrypted_password`, must not be `None`")  # noqa: E501

        self._encrypted_password = encrypted_password

    @property
    def user_name(self):
        """Gets the user_name of this AppDynamicsConfiguration.  # noqa: E501

        Username is combination of userName and the account name.  # noqa: E501

        :return: The user_name of this AppDynamicsConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this AppDynamicsConfiguration.

        Username is combination of userName and the account name.  # noqa: E501

        :param user_name: The user_name of this AppDynamicsConfiguration.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and user_name is None:
            raise ValueError("Invalid value for `user_name`, must not be `None`")  # noqa: E501

        self._user_name = user_name

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
        if issubclass(AppDynamicsConfiguration, dict):
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
        if not isinstance(other, AppDynamicsConfiguration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AppDynamicsConfiguration):
            return True

        return self.to_dict() != other.to_dict()
