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


class IntegrationMetrics(object):
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
        'chart_objs': 'list[Chart]',
        'charts': 'list[str]',
        'display': 'list[str]',
        'pps_dimensions': 'list[str]',
        'prefixes': 'list[str]',
        'required': 'list[str]'
    }

    attribute_map = {
        'chart_objs': 'chartObjs',
        'charts': 'charts',
        'display': 'display',
        'pps_dimensions': 'ppsDimensions',
        'prefixes': 'prefixes',
        'required': 'required'
    }

    def __init__(self, chart_objs=None, charts=None, display=None, pps_dimensions=None, prefixes=None, required=None, _configuration=None):  # noqa: E501
        """IntegrationMetrics - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._chart_objs = None
        self._charts = None
        self._display = None
        self._pps_dimensions = None
        self._prefixes = None
        self._required = None
        self.discriminator = None

        if chart_objs is not None:
            self.chart_objs = chart_objs
        self.charts = charts
        self.display = display
        if pps_dimensions is not None:
            self.pps_dimensions = pps_dimensions
        self.prefixes = prefixes
        self.required = required

    @property
    def chart_objs(self):
        """Gets the chart_objs of this IntegrationMetrics.  # noqa: E501

        Chart JSONs materialized from the links in `charts`  # noqa: E501

        :return: The chart_objs of this IntegrationMetrics.  # noqa: E501
        :rtype: list[Chart]
        """
        return self._chart_objs

    @chart_objs.setter
    def chart_objs(self, chart_objs):
        """Sets the chart_objs of this IntegrationMetrics.

        Chart JSONs materialized from the links in `charts`  # noqa: E501

        :param chart_objs: The chart_objs of this IntegrationMetrics.  # noqa: E501
        :type: list[Chart]
        """

        self._chart_objs = chart_objs

    @property
    def charts(self):
        """Gets the charts of this IntegrationMetrics.  # noqa: E501

        URLs for JSON definitions of charts that display info about this integration's metrics  # noqa: E501

        :return: The charts of this IntegrationMetrics.  # noqa: E501
        :rtype: list[str]
        """
        return self._charts

    @charts.setter
    def charts(self, charts):
        """Sets the charts of this IntegrationMetrics.

        URLs for JSON definitions of charts that display info about this integration's metrics  # noqa: E501

        :param charts: The charts of this IntegrationMetrics.  # noqa: E501
        :type: list[str]
        """
        if self._configuration.client_side_validation and charts is None:
            raise ValueError("Invalid value for `charts`, must not be `None`")  # noqa: E501

        self._charts = charts

    @property
    def display(self):
        """Gets the display of this IntegrationMetrics.  # noqa: E501

        Set of metrics that are displayed in the metric panel during integration setup  # noqa: E501

        :return: The display of this IntegrationMetrics.  # noqa: E501
        :rtype: list[str]
        """
        return self._display

    @display.setter
    def display(self, display):
        """Sets the display of this IntegrationMetrics.

        Set of metrics that are displayed in the metric panel during integration setup  # noqa: E501

        :param display: The display of this IntegrationMetrics.  # noqa: E501
        :type: list[str]
        """
        if self._configuration.client_side_validation and display is None:
            raise ValueError("Invalid value for `display`, must not be `None`")  # noqa: E501

        self._display = display

    @property
    def pps_dimensions(self):
        """Gets the pps_dimensions of this IntegrationMetrics.  # noqa: E501

        For reported points belonging to this integration, these point tags are escalated to the internal point-rate counters so that reporting can be broken out by these dimensions  # noqa: E501

        :return: The pps_dimensions of this IntegrationMetrics.  # noqa: E501
        :rtype: list[str]
        """
        return self._pps_dimensions

    @pps_dimensions.setter
    def pps_dimensions(self, pps_dimensions):
        """Sets the pps_dimensions of this IntegrationMetrics.

        For reported points belonging to this integration, these point tags are escalated to the internal point-rate counters so that reporting can be broken out by these dimensions  # noqa: E501

        :param pps_dimensions: The pps_dimensions of this IntegrationMetrics.  # noqa: E501
        :type: list[str]
        """

        self._pps_dimensions = pps_dimensions

    @property
    def prefixes(self):
        """Gets the prefixes of this IntegrationMetrics.  # noqa: E501

        Set of metric prefix namespaces belonging to this integration  # noqa: E501

        :return: The prefixes of this IntegrationMetrics.  # noqa: E501
        :rtype: list[str]
        """
        return self._prefixes

    @prefixes.setter
    def prefixes(self, prefixes):
        """Sets the prefixes of this IntegrationMetrics.

        Set of metric prefix namespaces belonging to this integration  # noqa: E501

        :param prefixes: The prefixes of this IntegrationMetrics.  # noqa: E501
        :type: list[str]
        """
        if self._configuration.client_side_validation and prefixes is None:
            raise ValueError("Invalid value for `prefixes`, must not be `None`")  # noqa: E501

        self._prefixes = prefixes

    @property
    def required(self):
        """Gets the required of this IntegrationMetrics.  # noqa: E501

        Set of \"canary\" metrics that define the \"liveness\" of this integration's metric ingestion  # noqa: E501

        :return: The required of this IntegrationMetrics.  # noqa: E501
        :rtype: list[str]
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this IntegrationMetrics.

        Set of \"canary\" metrics that define the \"liveness\" of this integration's metric ingestion  # noqa: E501

        :param required: The required of this IntegrationMetrics.  # noqa: E501
        :type: list[str]
        """
        if self._configuration.client_side_validation and required is None:
            raise ValueError("Invalid value for `required`, must not be `None`")  # noqa: E501

        self._required = required

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
        if issubclass(IntegrationMetrics, dict):
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
        if not isinstance(other, IntegrationMetrics):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IntegrationMetrics):
            return True

        return self.to_dict() != other.to_dict()
