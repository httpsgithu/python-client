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


class IngestionPolicyMetadata(object):
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
        'customer': 'str',
        'ingestion_policy_id': 'str',
        'usage_in_billing_period': 'int'
    }

    attribute_map = {
        'customer': 'customer',
        'ingestion_policy_id': 'ingestionPolicyId',
        'usage_in_billing_period': 'usageInBillingPeriod'
    }

    def __init__(self, customer=None, ingestion_policy_id=None, usage_in_billing_period=None, _configuration=None):  # noqa: E501
        """IngestionPolicyMetadata - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._customer = None
        self._ingestion_policy_id = None
        self._usage_in_billing_period = None
        self.discriminator = None

        if customer is not None:
            self.customer = customer
        if ingestion_policy_id is not None:
            self.ingestion_policy_id = ingestion_policy_id
        if usage_in_billing_period is not None:
            self.usage_in_billing_period = usage_in_billing_period

    @property
    def customer(self):
        """Gets the customer of this IngestionPolicyMetadata.  # noqa: E501

        ID of the customer to which the ingestion policy metadata belongs  # noqa: E501

        :return: The customer of this IngestionPolicyMetadata.  # noqa: E501
        :rtype: str
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this IngestionPolicyMetadata.

        ID of the customer to which the ingestion policy metadata belongs  # noqa: E501

        :param customer: The customer of this IngestionPolicyMetadata.  # noqa: E501
        :type: str
        """

        self._customer = customer

    @property
    def ingestion_policy_id(self):
        """Gets the ingestion_policy_id of this IngestionPolicyMetadata.  # noqa: E501

        The unique ID for the ingestion policy to which the metadata belongs  # noqa: E501

        :return: The ingestion_policy_id of this IngestionPolicyMetadata.  # noqa: E501
        :rtype: str
        """
        return self._ingestion_policy_id

    @ingestion_policy_id.setter
    def ingestion_policy_id(self, ingestion_policy_id):
        """Sets the ingestion_policy_id of this IngestionPolicyMetadata.

        The unique ID for the ingestion policy to which the metadata belongs  # noqa: E501

        :param ingestion_policy_id: The ingestion_policy_id of this IngestionPolicyMetadata.  # noqa: E501
        :type: str
        """

        self._ingestion_policy_id = ingestion_policy_id

    @property
    def usage_in_billing_period(self):
        """Gets the usage_in_billing_period of this IngestionPolicyMetadata.  # noqa: E501

        ingestion policy usage in billing period  # noqa: E501

        :return: The usage_in_billing_period of this IngestionPolicyMetadata.  # noqa: E501
        :rtype: int
        """
        return self._usage_in_billing_period

    @usage_in_billing_period.setter
    def usage_in_billing_period(self, usage_in_billing_period):
        """Sets the usage_in_billing_period of this IngestionPolicyMetadata.

        ingestion policy usage in billing period  # noqa: E501

        :param usage_in_billing_period: The usage_in_billing_period of this IngestionPolicyMetadata.  # noqa: E501
        :type: int
        """

        self._usage_in_billing_period = usage_in_billing_period

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
        if issubclass(IngestionPolicyMetadata, dict):
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
        if not isinstance(other, IngestionPolicyMetadata):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IngestionPolicyMetadata):
            return True

        return self.to_dict() != other.to_dict()
