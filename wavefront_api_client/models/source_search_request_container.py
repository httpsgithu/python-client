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


class SourceSearchRequestContainer(object):
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
        'cursor': 'str',
        'include_obsolete': 'bool',
        'limit': 'int',
        'query': 'list[SearchQuery]',
        'sort_sources_ascending': 'bool'
    }

    attribute_map = {
        'cursor': 'cursor',
        'include_obsolete': 'includeObsolete',
        'limit': 'limit',
        'query': 'query',
        'sort_sources_ascending': 'sortSourcesAscending'
    }

    def __init__(self, cursor=None, include_obsolete=None, limit=None, query=None, sort_sources_ascending=None, _configuration=None):  # noqa: E501
        """SourceSearchRequestContainer - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cursor = None
        self._include_obsolete = None
        self._limit = None
        self._query = None
        self._sort_sources_ascending = None
        self.discriminator = None

        if cursor is not None:
            self.cursor = cursor
        if include_obsolete is not None:
            self.include_obsolete = include_obsolete
        if limit is not None:
            self.limit = limit
        if query is not None:
            self.query = query
        if sort_sources_ascending is not None:
            self.sort_sources_ascending = sort_sources_ascending

    @property
    def cursor(self):
        """Gets the cursor of this SourceSearchRequestContainer.  # noqa: E501

        The id (exclusive) from which search results resume returning.  Users should supply an entity 'id' to this property.  Its main purpose is to resume where a previous search left off because of the 'limit' parameter.  If a user supplies the last id in a set of results to cursor, while keeping the query the same, the system will return the next page of results  # noqa: E501

        :return: The cursor of this SourceSearchRequestContainer.  # noqa: E501
        :rtype: str
        """
        return self._cursor

    @cursor.setter
    def cursor(self, cursor):
        """Sets the cursor of this SourceSearchRequestContainer.

        The id (exclusive) from which search results resume returning.  Users should supply an entity 'id' to this property.  Its main purpose is to resume where a previous search left off because of the 'limit' parameter.  If a user supplies the last id in a set of results to cursor, while keeping the query the same, the system will return the next page of results  # noqa: E501

        :param cursor: The cursor of this SourceSearchRequestContainer.  # noqa: E501
        :type: str
        """

        self._cursor = cursor

    @property
    def include_obsolete(self):
        """Gets the include_obsolete of this SourceSearchRequestContainer.  # noqa: E501

        Whether to fetch obsolete sources.  Default: false  # noqa: E501

        :return: The include_obsolete of this SourceSearchRequestContainer.  # noqa: E501
        :rtype: bool
        """
        return self._include_obsolete

    @include_obsolete.setter
    def include_obsolete(self, include_obsolete):
        """Sets the include_obsolete of this SourceSearchRequestContainer.

        Whether to fetch obsolete sources.  Default: false  # noqa: E501

        :param include_obsolete: The include_obsolete of this SourceSearchRequestContainer.  # noqa: E501
        :type: bool
        """

        self._include_obsolete = include_obsolete

    @property
    def limit(self):
        """Gets the limit of this SourceSearchRequestContainer.  # noqa: E501

        The number of results to return.  Default: 100  # noqa: E501

        :return: The limit of this SourceSearchRequestContainer.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SourceSearchRequestContainer.

        The number of results to return.  Default: 100  # noqa: E501

        :param limit: The limit of this SourceSearchRequestContainer.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def query(self):
        """Gets the query of this SourceSearchRequestContainer.  # noqa: E501

        A list of queries by which to limit the search results  # noqa: E501

        :return: The query of this SourceSearchRequestContainer.  # noqa: E501
        :rtype: list[SearchQuery]
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this SourceSearchRequestContainer.

        A list of queries by which to limit the search results  # noqa: E501

        :param query: The query of this SourceSearchRequestContainer.  # noqa: E501
        :type: list[SearchQuery]
        """

        self._query = query

    @property
    def sort_sources_ascending(self):
        """Gets the sort_sources_ascending of this SourceSearchRequestContainer.  # noqa: E501

        Whether to sort source results ascending lexigraphically by id/sourceName.  Default: true  # noqa: E501

        :return: The sort_sources_ascending of this SourceSearchRequestContainer.  # noqa: E501
        :rtype: bool
        """
        return self._sort_sources_ascending

    @sort_sources_ascending.setter
    def sort_sources_ascending(self, sort_sources_ascending):
        """Sets the sort_sources_ascending of this SourceSearchRequestContainer.

        Whether to sort source results ascending lexigraphically by id/sourceName.  Default: true  # noqa: E501

        :param sort_sources_ascending: The sort_sources_ascending of this SourceSearchRequestContainer.  # noqa: E501
        :type: bool
        """

        self._sort_sources_ascending = sort_sources_ascending

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
        if issubclass(SourceSearchRequestContainer, dict):
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
        if not isinstance(other, SourceSearchRequestContainer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SourceSearchRequestContainer):
            return True

        return self.to_dict() != other.to_dict()
