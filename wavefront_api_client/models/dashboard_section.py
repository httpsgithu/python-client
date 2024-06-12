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


class DashboardSection(object):
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
        'id': 'str',
        'name': 'str',
        'rows': 'list[DashboardSectionRow]',
        'section_filter': 'JsonNode'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'rows': 'rows',
        'section_filter': 'sectionFilter'
    }

    def __init__(self, id=None, name=None, rows=None, section_filter=None, _configuration=None):  # noqa: E501
        """DashboardSection - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._rows = None
        self._section_filter = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        self.rows = rows
        if section_filter is not None:
            self.section_filter = section_filter

    @property
    def id(self):
        """Gets the id of this DashboardSection.  # noqa: E501

        Id of this section  # noqa: E501

        :return: The id of this DashboardSection.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DashboardSection.

        Id of this section  # noqa: E501

        :param id: The id of this DashboardSection.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this DashboardSection.  # noqa: E501

        Name of this section  # noqa: E501

        :return: The name of this DashboardSection.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DashboardSection.

        Name of this section  # noqa: E501

        :param name: The name of this DashboardSection.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def rows(self):
        """Gets the rows of this DashboardSection.  # noqa: E501

        Rows of this section  # noqa: E501

        :return: The rows of this DashboardSection.  # noqa: E501
        :rtype: list[DashboardSectionRow]
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """Sets the rows of this DashboardSection.

        Rows of this section  # noqa: E501

        :param rows: The rows of this DashboardSection.  # noqa: E501
        :type: list[DashboardSectionRow]
        """
        if self._configuration.client_side_validation and rows is None:
            raise ValueError("Invalid value for `rows`, must not be `None`")  # noqa: E501

        self._rows = rows

    @property
    def section_filter(self):
        """Gets the section_filter of this DashboardSection.  # noqa: E501

        Display filter for conditional dashboard section  # noqa: E501

        :return: The section_filter of this DashboardSection.  # noqa: E501
        :rtype: JsonNode
        """
        return self._section_filter

    @section_filter.setter
    def section_filter(self, section_filter):
        """Sets the section_filter of this DashboardSection.

        Display filter for conditional dashboard section  # noqa: E501

        :param section_filter: The section_filter of this DashboardSection.  # noqa: E501
        :type: JsonNode
        """

        self._section_filter = section_filter

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
        if issubclass(DashboardSection, dict):
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
        if not isinstance(other, DashboardSection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DashboardSection):
            return True

        return self.to_dict() != other.to_dict()
