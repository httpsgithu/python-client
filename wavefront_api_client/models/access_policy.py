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

from wavefront_api_client.configuration import Configuration


class AccessPolicy(object):
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
        'last_updated_ms': 'int',
        'policy_rules': 'list[AccessPolicyRuleDTO]'
    }

    attribute_map = {
        'customer': 'customer',
        'last_updated_ms': 'lastUpdatedMs',
        'policy_rules': 'policyRules'
    }

    def __init__(self, customer=None, last_updated_ms=None, policy_rules=None, _configuration=None):  # noqa: E501
        """AccessPolicy - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._customer = None
        self._last_updated_ms = None
        self._policy_rules = None
        self.discriminator = None

        if customer is not None:
            self.customer = customer
        if last_updated_ms is not None:
            self.last_updated_ms = last_updated_ms
        if policy_rules is not None:
            self.policy_rules = policy_rules

    @property
    def customer(self):
        """Gets the customer of this AccessPolicy.  # noqa: E501


        :return: The customer of this AccessPolicy.  # noqa: E501
        :rtype: str
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this AccessPolicy.


        :param customer: The customer of this AccessPolicy.  # noqa: E501
        :type: str
        """

        self._customer = customer

    @property
    def last_updated_ms(self):
        """Gets the last_updated_ms of this AccessPolicy.  # noqa: E501


        :return: The last_updated_ms of this AccessPolicy.  # noqa: E501
        :rtype: int
        """
        return self._last_updated_ms

    @last_updated_ms.setter
    def last_updated_ms(self, last_updated_ms):
        """Sets the last_updated_ms of this AccessPolicy.


        :param last_updated_ms: The last_updated_ms of this AccessPolicy.  # noqa: E501
        :type: int
        """

        self._last_updated_ms = last_updated_ms

    @property
    def policy_rules(self):
        """Gets the policy_rules of this AccessPolicy.  # noqa: E501


        :return: The policy_rules of this AccessPolicy.  # noqa: E501
        :rtype: list[AccessPolicyRuleDTO]
        """
        return self._policy_rules

    @policy_rules.setter
    def policy_rules(self, policy_rules):
        """Sets the policy_rules of this AccessPolicy.


        :param policy_rules: The policy_rules of this AccessPolicy.  # noqa: E501
        :type: list[AccessPolicyRuleDTO]
        """

        self._policy_rules = policy_rules

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
        if issubclass(AccessPolicy, dict):
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
        if not isinstance(other, AccessPolicy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccessPolicy):
            return True

        return self.to_dict() != other.to_dict()
