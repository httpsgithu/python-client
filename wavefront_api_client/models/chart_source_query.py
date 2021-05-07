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


class ChartSourceQuery(object):
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
        'disabled': 'bool',
        'name': 'str',
        'query': 'str',
        'query_type': 'str',
        'querybuilder_enabled': 'bool',
        'querybuilder_serialization': 'str',
        'scatter_plot_source': 'str',
        'secondary_axis': 'bool',
        'source_color': 'str',
        'source_description': 'str'
    }

    attribute_map = {
        'disabled': 'disabled',
        'name': 'name',
        'query': 'query',
        'query_type': 'queryType',
        'querybuilder_enabled': 'querybuilderEnabled',
        'querybuilder_serialization': 'querybuilderSerialization',
        'scatter_plot_source': 'scatterPlotSource',
        'secondary_axis': 'secondaryAxis',
        'source_color': 'sourceColor',
        'source_description': 'sourceDescription'
    }

    def __init__(self, disabled=None, name=None, query=None, query_type=None, querybuilder_enabled=None, querybuilder_serialization=None, scatter_plot_source=None, secondary_axis=None, source_color=None, source_description=None):  # noqa: E501
        """ChartSourceQuery - a model defined in Swagger"""  # noqa: E501

        self._disabled = None
        self._name = None
        self._query = None
        self._query_type = None
        self._querybuilder_enabled = None
        self._querybuilder_serialization = None
        self._scatter_plot_source = None
        self._secondary_axis = None
        self._source_color = None
        self._source_description = None
        self.discriminator = None

        if disabled is not None:
            self.disabled = disabled
        self.name = name
        self.query = query
        if query_type is not None:
            self.query_type = query_type
        if querybuilder_enabled is not None:
            self.querybuilder_enabled = querybuilder_enabled
        if querybuilder_serialization is not None:
            self.querybuilder_serialization = querybuilder_serialization
        if scatter_plot_source is not None:
            self.scatter_plot_source = scatter_plot_source
        if secondary_axis is not None:
            self.secondary_axis = secondary_axis
        if source_color is not None:
            self.source_color = source_color
        if source_description is not None:
            self.source_description = source_description

    @property
    def disabled(self):
        """Gets the disabled of this ChartSourceQuery.  # noqa: E501

        Whether the source is disabled  # noqa: E501

        :return: The disabled of this ChartSourceQuery.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this ChartSourceQuery.

        Whether the source is disabled  # noqa: E501

        :param disabled: The disabled of this ChartSourceQuery.  # noqa: E501
        :type: bool
        """

        self._disabled = disabled

    @property
    def name(self):
        """Gets the name of this ChartSourceQuery.  # noqa: E501

        Name of the source  # noqa: E501

        :return: The name of this ChartSourceQuery.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ChartSourceQuery.

        Name of the source  # noqa: E501

        :param name: The name of this ChartSourceQuery.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def query(self):
        """Gets the query of this ChartSourceQuery.  # noqa: E501

        Query expression to plot on the chart  # noqa: E501

        :return: The query of this ChartSourceQuery.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this ChartSourceQuery.

        Query expression to plot on the chart  # noqa: E501

        :param query: The query of this ChartSourceQuery.  # noqa: E501
        :type: str
        """
        if query is None:
            raise ValueError("Invalid value for `query`, must not be `None`")  # noqa: E501

        self._query = query

    @property
    def query_type(self):
        """Gets the query_type of this ChartSourceQuery.  # noqa: E501

        Query type of the source  # noqa: E501

        :return: The query_type of this ChartSourceQuery.  # noqa: E501
        :rtype: str
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type):
        """Sets the query_type of this ChartSourceQuery.

        Query type of the source  # noqa: E501

        :param query_type: The query_type of this ChartSourceQuery.  # noqa: E501
        :type: str
        """
        allowed_values = ["WQL", "PROMQL", "HYBRID"]  # noqa: E501
        if query_type not in allowed_values:
            raise ValueError(
                "Invalid value for `query_type` ({0}), must be one of {1}"  # noqa: E501
                .format(query_type, allowed_values)
            )

        self._query_type = query_type

    @property
    def querybuilder_enabled(self):
        """Gets the querybuilder_enabled of this ChartSourceQuery.  # noqa: E501

        Whether or not this source line should have the query builder enabled  # noqa: E501

        :return: The querybuilder_enabled of this ChartSourceQuery.  # noqa: E501
        :rtype: bool
        """
        return self._querybuilder_enabled

    @querybuilder_enabled.setter
    def querybuilder_enabled(self, querybuilder_enabled):
        """Sets the querybuilder_enabled of this ChartSourceQuery.

        Whether or not this source line should have the query builder enabled  # noqa: E501

        :param querybuilder_enabled: The querybuilder_enabled of this ChartSourceQuery.  # noqa: E501
        :type: bool
        """

        self._querybuilder_enabled = querybuilder_enabled

    @property
    def querybuilder_serialization(self):
        """Gets the querybuilder_serialization of this ChartSourceQuery.  # noqa: E501

        Opaque representation of the querybuilder  # noqa: E501

        :return: The querybuilder_serialization of this ChartSourceQuery.  # noqa: E501
        :rtype: str
        """
        return self._querybuilder_serialization

    @querybuilder_serialization.setter
    def querybuilder_serialization(self, querybuilder_serialization):
        """Sets the querybuilder_serialization of this ChartSourceQuery.

        Opaque representation of the querybuilder  # noqa: E501

        :param querybuilder_serialization: The querybuilder_serialization of this ChartSourceQuery.  # noqa: E501
        :type: str
        """

        self._querybuilder_serialization = querybuilder_serialization

    @property
    def scatter_plot_source(self):
        """Gets the scatter_plot_source of this ChartSourceQuery.  # noqa: E501

        For scatter plots, does this query source the X-axis or the Y-axis  # noqa: E501

        :return: The scatter_plot_source of this ChartSourceQuery.  # noqa: E501
        :rtype: str
        """
        return self._scatter_plot_source

    @scatter_plot_source.setter
    def scatter_plot_source(self, scatter_plot_source):
        """Sets the scatter_plot_source of this ChartSourceQuery.

        For scatter plots, does this query source the X-axis or the Y-axis  # noqa: E501

        :param scatter_plot_source: The scatter_plot_source of this ChartSourceQuery.  # noqa: E501
        :type: str
        """
        allowed_values = ["X", "Y"]  # noqa: E501
        if scatter_plot_source not in allowed_values:
            raise ValueError(
                "Invalid value for `scatter_plot_source` ({0}), must be one of {1}"  # noqa: E501
                .format(scatter_plot_source, allowed_values)
            )

        self._scatter_plot_source = scatter_plot_source

    @property
    def secondary_axis(self):
        """Gets the secondary_axis of this ChartSourceQuery.  # noqa: E501

        Determines if this source relates to the right hand Y-axis or not  # noqa: E501

        :return: The secondary_axis of this ChartSourceQuery.  # noqa: E501
        :rtype: bool
        """
        return self._secondary_axis

    @secondary_axis.setter
    def secondary_axis(self, secondary_axis):
        """Sets the secondary_axis of this ChartSourceQuery.

        Determines if this source relates to the right hand Y-axis or not  # noqa: E501

        :param secondary_axis: The secondary_axis of this ChartSourceQuery.  # noqa: E501
        :type: bool
        """

        self._secondary_axis = secondary_axis

    @property
    def source_color(self):
        """Gets the source_color of this ChartSourceQuery.  # noqa: E501

        The color used to draw all results from this source (auto if unset)  # noqa: E501

        :return: The source_color of this ChartSourceQuery.  # noqa: E501
        :rtype: str
        """
        return self._source_color

    @source_color.setter
    def source_color(self, source_color):
        """Sets the source_color of this ChartSourceQuery.

        The color used to draw all results from this source (auto if unset)  # noqa: E501

        :param source_color: The source_color of this ChartSourceQuery.  # noqa: E501
        :type: str
        """

        self._source_color = source_color

    @property
    def source_description(self):
        """Gets the source_description of this ChartSourceQuery.  # noqa: E501

        A description for the purpose of this source  # noqa: E501

        :return: The source_description of this ChartSourceQuery.  # noqa: E501
        :rtype: str
        """
        return self._source_description

    @source_description.setter
    def source_description(self, source_description):
        """Sets the source_description of this ChartSourceQuery.

        A description for the purpose of this source  # noqa: E501

        :param source_description: The source_description of this ChartSourceQuery.  # noqa: E501
        :type: str
        """

        self._source_description = source_description

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
        if issubclass(ChartSourceQuery, dict):
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
        if not isinstance(other, ChartSourceQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
