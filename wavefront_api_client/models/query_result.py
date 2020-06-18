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


class QueryResult(object):
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
        'dimensions': 'list[TupleResult]',
        'error_message': 'str',
        'error_type': 'str',
        'events': 'list[QueryEvent]',
        'granularity': 'int',
        'name': 'str',
        'query': 'str',
        'spans': 'list[Span]',
        'stats': 'StatsModelInternalUse',
        'timeseries': 'list[Timeseries]',
        'trace_dimensions': 'list[TupleResult]',
        'traces': 'list[Trace]',
        'warnings': 'str'
    }

    attribute_map = {
        'dimensions': 'dimensions',
        'error_message': 'errorMessage',
        'error_type': 'errorType',
        'events': 'events',
        'granularity': 'granularity',
        'name': 'name',
        'query': 'query',
        'spans': 'spans',
        'stats': 'stats',
        'timeseries': 'timeseries',
        'trace_dimensions': 'traceDimensions',
        'traces': 'traces',
        'warnings': 'warnings'
    }

    def __init__(self, dimensions=None, error_message=None, error_type=None, events=None, granularity=None, name=None, query=None, spans=None, stats=None, timeseries=None, trace_dimensions=None, traces=None, warnings=None):  # noqa: E501
        """QueryResult - a model defined in Swagger"""  # noqa: E501

        self._dimensions = None
        self._error_message = None
        self._error_type = None
        self._events = None
        self._granularity = None
        self._name = None
        self._query = None
        self._spans = None
        self._stats = None
        self._timeseries = None
        self._trace_dimensions = None
        self._traces = None
        self._warnings = None
        self.discriminator = None

        if dimensions is not None:
            self.dimensions = dimensions
        if error_message is not None:
            self.error_message = error_message
        if error_type is not None:
            self.error_type = error_type
        if events is not None:
            self.events = events
        if granularity is not None:
            self.granularity = granularity
        if name is not None:
            self.name = name
        if query is not None:
            self.query = query
        if spans is not None:
            self.spans = spans
        if stats is not None:
            self.stats = stats
        if timeseries is not None:
            self.timeseries = timeseries
        if trace_dimensions is not None:
            self.trace_dimensions = trace_dimensions
        if traces is not None:
            self.traces = traces
        if warnings is not None:
            self.warnings = warnings

    @property
    def dimensions(self):
        """Gets the dimensions of this QueryResult.  # noqa: E501

        List of all dimension tuple results  # noqa: E501

        :return: The dimensions of this QueryResult.  # noqa: E501
        :rtype: list[TupleResult]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this QueryResult.

        List of all dimension tuple results  # noqa: E501

        :param dimensions: The dimensions of this QueryResult.  # noqa: E501
        :type: list[TupleResult]
        """

        self._dimensions = dimensions

    @property
    def error_message(self):
        """Gets the error_message of this QueryResult.  # noqa: E501

        Error message, if query execution did not finish successfully  # noqa: E501

        :return: The error_message of this QueryResult.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this QueryResult.

        Error message, if query execution did not finish successfully  # noqa: E501

        :param error_message: The error_message of this QueryResult.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

    @property
    def error_type(self):
        """Gets the error_type of this QueryResult.  # noqa: E501

        Error type, if query execution did not finish successfully  # noqa: E501

        :return: The error_type of this QueryResult.  # noqa: E501
        :rtype: str
        """
        return self._error_type

    @error_type.setter
    def error_type(self, error_type):
        """Sets the error_type of this QueryResult.

        Error type, if query execution did not finish successfully  # noqa: E501

        :param error_type: The error_type of this QueryResult.  # noqa: E501
        :type: str
        """
        allowed_values = ["N/A", "QuerySyntaxError", "QueryExecutionError", "Timeout"]  # noqa: E501
        if error_type not in allowed_values:
            raise ValueError(
                "Invalid value for `error_type` ({0}), must be one of {1}"  # noqa: E501
                .format(error_type, allowed_values)
            )

        self._error_type = error_type

    @property
    def events(self):
        """Gets the events of this QueryResult.  # noqa: E501


        :return: The events of this QueryResult.  # noqa: E501
        :rtype: list[QueryEvent]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this QueryResult.


        :param events: The events of this QueryResult.  # noqa: E501
        :type: list[QueryEvent]
        """

        self._events = events

    @property
    def granularity(self):
        """Gets the granularity of this QueryResult.  # noqa: E501

        The granularity of the returned results, in seconds  # noqa: E501

        :return: The granularity of this QueryResult.  # noqa: E501
        :rtype: int
        """
        return self._granularity

    @granularity.setter
    def granularity(self, granularity):
        """Sets the granularity of this QueryResult.

        The granularity of the returned results, in seconds  # noqa: E501

        :param granularity: The granularity of this QueryResult.  # noqa: E501
        :type: int
        """

        self._granularity = granularity

    @property
    def name(self):
        """Gets the name of this QueryResult.  # noqa: E501

        The name of this query  # noqa: E501

        :return: The name of this QueryResult.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this QueryResult.

        The name of this query  # noqa: E501

        :param name: The name of this QueryResult.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def query(self):
        """Gets the query of this QueryResult.  # noqa: E501

        The query used to obtain this result  # noqa: E501

        :return: The query of this QueryResult.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this QueryResult.

        The query used to obtain this result  # noqa: E501

        :param query: The query of this QueryResult.  # noqa: E501
        :type: str
        """

        self._query = query

    @property
    def spans(self):
        """Gets the spans of this QueryResult.  # noqa: E501


        :return: The spans of this QueryResult.  # noqa: E501
        :rtype: list[Span]
        """
        return self._spans

    @spans.setter
    def spans(self, spans):
        """Sets the spans of this QueryResult.


        :param spans: The spans of this QueryResult.  # noqa: E501
        :type: list[Span]
        """

        self._spans = spans

    @property
    def stats(self):
        """Gets the stats of this QueryResult.  # noqa: E501


        :return: The stats of this QueryResult.  # noqa: E501
        :rtype: StatsModelInternalUse
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        """Sets the stats of this QueryResult.


        :param stats: The stats of this QueryResult.  # noqa: E501
        :type: StatsModelInternalUse
        """

        self._stats = stats

    @property
    def timeseries(self):
        """Gets the timeseries of this QueryResult.  # noqa: E501


        :return: The timeseries of this QueryResult.  # noqa: E501
        :rtype: list[Timeseries]
        """
        return self._timeseries

    @timeseries.setter
    def timeseries(self, timeseries):
        """Sets the timeseries of this QueryResult.


        :param timeseries: The timeseries of this QueryResult.  # noqa: E501
        :type: list[Timeseries]
        """

        self._timeseries = timeseries

    @property
    def trace_dimensions(self):
        """Gets the trace_dimensions of this QueryResult.  # noqa: E501

        List of all tracing tuple results  # noqa: E501

        :return: The trace_dimensions of this QueryResult.  # noqa: E501
        :rtype: list[TupleResult]
        """
        return self._trace_dimensions

    @trace_dimensions.setter
    def trace_dimensions(self, trace_dimensions):
        """Sets the trace_dimensions of this QueryResult.

        List of all tracing tuple results  # noqa: E501

        :param trace_dimensions: The trace_dimensions of this QueryResult.  # noqa: E501
        :type: list[TupleResult]
        """

        self._trace_dimensions = trace_dimensions

    @property
    def traces(self):
        """Gets the traces of this QueryResult.  # noqa: E501


        :return: The traces of this QueryResult.  # noqa: E501
        :rtype: list[Trace]
        """
        return self._traces

    @traces.setter
    def traces(self, traces):
        """Sets the traces of this QueryResult.


        :param traces: The traces of this QueryResult.  # noqa: E501
        :type: list[Trace]
        """

        self._traces = traces

    @property
    def warnings(self):
        """Gets the warnings of this QueryResult.  # noqa: E501

        The warnings incurred by this query  # noqa: E501

        :return: The warnings of this QueryResult.  # noqa: E501
        :rtype: str
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        """Sets the warnings of this QueryResult.

        The warnings incurred by this query  # noqa: E501

        :param warnings: The warnings of this QueryResult.  # noqa: E501
        :type: str
        """

        self._warnings = warnings

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
        if issubclass(QueryResult, dict):
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
        if not isinstance(other, QueryResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
