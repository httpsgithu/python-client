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


class MetricsPolicyWriteModel(object):
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
        'policy_rules': 'list[PolicyRuleWriteModel]',
        'updated_epoch_millis': 'int',
        'updater_id': 'str'
    }

    attribute_map = {
        'customer': 'customer',
        'policy_rules': 'policyRules',
        'updated_epoch_millis': 'updatedEpochMillis',
        'updater_id': 'updaterId'
    }

    def __init__(self, customer=None, policy_rules=None, updated_epoch_millis=None, updater_id=None, _configuration=None):  # noqa: E501
        """MetricsPolicyWriteModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._customer = None
        self._policy_rules = None
        self._updated_epoch_millis = None
        self._updater_id = None
        self.discriminator = None

        if customer is not None:
            self.customer = customer
        if policy_rules is not None:
            self.policy_rules = policy_rules
        if updated_epoch_millis is not None:
            self.updated_epoch_millis = updated_epoch_millis
        if updater_id is not None:
            self.updater_id = updater_id

    @property
    def customer(self):
        """Gets the customer of this MetricsPolicyWriteModel.  # noqa: E501

        The customer identifier of the metrics policy  # noqa: E501

        :return: The customer of this MetricsPolicyWriteModel.  # noqa: E501
        :rtype: str
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this MetricsPolicyWriteModel.

        The customer identifier of the metrics policy  # noqa: E501

        :param customer: The customer of this MetricsPolicyWriteModel.  # noqa: E501
        :type: str
        """

        self._customer = customer

    @property
    def policy_rules(self):
        """Gets the policy_rules of this MetricsPolicyWriteModel.  # noqa: E501

        The policy rules of the metrics policy  # noqa: E501

        :return: The policy_rules of this MetricsPolicyWriteModel.  # noqa: E501
        :rtype: list[PolicyRuleWriteModel]
        """
        return self._policy_rules

    @policy_rules.setter
    def policy_rules(self, policy_rules):
        """Sets the policy_rules of this MetricsPolicyWriteModel.

        The policy rules of the metrics policy  # noqa: E501

        :param policy_rules: The policy_rules of this MetricsPolicyWriteModel.  # noqa: E501
        :type: list[PolicyRuleWriteModel]
        """

        self._policy_rules = policy_rules

    @property
    def updated_epoch_millis(self):
        """Gets the updated_epoch_millis of this MetricsPolicyWriteModel.  # noqa: E501

        The date time of the metrics policy update  # noqa: E501

        :return: The updated_epoch_millis of this MetricsPolicyWriteModel.  # noqa: E501
        :rtype: int
        """
        return self._updated_epoch_millis

    @updated_epoch_millis.setter
    def updated_epoch_millis(self, updated_epoch_millis):
        """Sets the updated_epoch_millis of this MetricsPolicyWriteModel.

        The date time of the metrics policy update  # noqa: E501

        :param updated_epoch_millis: The updated_epoch_millis of this MetricsPolicyWriteModel.  # noqa: E501
        :type: int
        """

        self._updated_epoch_millis = updated_epoch_millis

    @property
    def updater_id(self):
        """Gets the updater_id of this MetricsPolicyWriteModel.  # noqa: E501

        The id of the metrics policy updater  # noqa: E501

        :return: The updater_id of this MetricsPolicyWriteModel.  # noqa: E501
        :rtype: str
        """
        return self._updater_id

    @updater_id.setter
    def updater_id(self, updater_id):
        """Sets the updater_id of this MetricsPolicyWriteModel.

        The id of the metrics policy updater  # noqa: E501

        :param updater_id: The updater_id of this MetricsPolicyWriteModel.  # noqa: E501
        :type: str
        """

        self._updater_id = updater_id

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
        if issubclass(MetricsPolicyWriteModel, dict):
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
        if not isinstance(other, MetricsPolicyWriteModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MetricsPolicyWriteModel):
            return True

        return self.to_dict() != other.to_dict()
