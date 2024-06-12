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


class AzureActivityLogConfiguration(object):
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
        'base_credentials': 'AzureBaseCredentials',
        'category_filter': 'list[str]'
    }

    attribute_map = {
        'base_credentials': 'baseCredentials',
        'category_filter': 'categoryFilter'
    }

    def __init__(self, base_credentials=None, category_filter=None, _configuration=None):  # noqa: E501
        """AzureActivityLogConfiguration - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._base_credentials = None
        self._category_filter = None
        self.discriminator = None

        if base_credentials is not None:
            self.base_credentials = base_credentials
        if category_filter is not None:
            self.category_filter = category_filter

    @property
    def base_credentials(self):
        """Gets the base_credentials of this AzureActivityLogConfiguration.  # noqa: E501


        :return: The base_credentials of this AzureActivityLogConfiguration.  # noqa: E501
        :rtype: AzureBaseCredentials
        """
        return self._base_credentials

    @base_credentials.setter
    def base_credentials(self, base_credentials):
        """Sets the base_credentials of this AzureActivityLogConfiguration.


        :param base_credentials: The base_credentials of this AzureActivityLogConfiguration.  # noqa: E501
        :type: AzureBaseCredentials
        """

        self._base_credentials = base_credentials

    @property
    def category_filter(self):
        """Gets the category_filter of this AzureActivityLogConfiguration.  # noqa: E501

        A list of Azure ActivityLog categories to pull events for.Allowable values are ADMINISTRATIVE, SERVICEHEALTH, ALERT, AUTOSCALE, SECURITY  # noqa: E501

        :return: The category_filter of this AzureActivityLogConfiguration.  # noqa: E501
        :rtype: list[str]
        """
        return self._category_filter

    @category_filter.setter
    def category_filter(self, category_filter):
        """Sets the category_filter of this AzureActivityLogConfiguration.

        A list of Azure ActivityLog categories to pull events for.Allowable values are ADMINISTRATIVE, SERVICEHEALTH, ALERT, AUTOSCALE, SECURITY  # noqa: E501

        :param category_filter: The category_filter of this AzureActivityLogConfiguration.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["ADMINISTRATIVE", "SERVICEHEALTH", "ALERT", "AUTOSCALE", "SECURITY"]  # noqa: E501
        if (self._configuration.client_side_validation and
                not set(category_filter).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `category_filter` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(category_filter) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._category_filter = category_filter

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
        if issubclass(AzureActivityLogConfiguration, dict):
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
        if not isinstance(other, AzureActivityLogConfiguration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AzureActivityLogConfiguration):
            return True

        return self.to_dict() != other.to_dict()
