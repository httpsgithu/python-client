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


class IngestionPolicyMapping(object):
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
        'accounts': 'list[str]',
        'groups': 'list[str]',
        'ingestion_policy_id': 'str'
    }

    attribute_map = {
        'accounts': 'accounts',
        'groups': 'groups',
        'ingestion_policy_id': 'ingestionPolicyId'
    }

    def __init__(self, accounts=None, groups=None, ingestion_policy_id=None, _configuration=None):  # noqa: E501
        """IngestionPolicyMapping - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._accounts = None
        self._groups = None
        self._ingestion_policy_id = None
        self.discriminator = None

        if accounts is not None:
            self.accounts = accounts
        if groups is not None:
            self.groups = groups
        self.ingestion_policy_id = ingestion_policy_id

    @property
    def accounts(self):
        """Gets the accounts of this IngestionPolicyMapping.  # noqa: E501

        The list of accounts that should be linked/unlinked to/from the ingestion policy  # noqa: E501

        :return: The accounts of this IngestionPolicyMapping.  # noqa: E501
        :rtype: list[str]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this IngestionPolicyMapping.

        The list of accounts that should be linked/unlinked to/from the ingestion policy  # noqa: E501

        :param accounts: The accounts of this IngestionPolicyMapping.  # noqa: E501
        :type: list[str]
        """

        self._accounts = accounts

    @property
    def groups(self):
        """Gets the groups of this IngestionPolicyMapping.  # noqa: E501

        The list of groups that should be linked/unlinked to/from the ingestion policy  # noqa: E501

        :return: The groups of this IngestionPolicyMapping.  # noqa: E501
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this IngestionPolicyMapping.

        The list of groups that should be linked/unlinked to/from the ingestion policy  # noqa: E501

        :param groups: The groups of this IngestionPolicyMapping.  # noqa: E501
        :type: list[str]
        """

        self._groups = groups

    @property
    def ingestion_policy_id(self):
        """Gets the ingestion_policy_id of this IngestionPolicyMapping.  # noqa: E501

        The unique identifier of the ingestion policy  # noqa: E501

        :return: The ingestion_policy_id of this IngestionPolicyMapping.  # noqa: E501
        :rtype: str
        """
        return self._ingestion_policy_id

    @ingestion_policy_id.setter
    def ingestion_policy_id(self, ingestion_policy_id):
        """Sets the ingestion_policy_id of this IngestionPolicyMapping.

        The unique identifier of the ingestion policy  # noqa: E501

        :param ingestion_policy_id: The ingestion_policy_id of this IngestionPolicyMapping.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and ingestion_policy_id is None:
            raise ValueError("Invalid value for `ingestion_policy_id`, must not be `None`")  # noqa: E501

        self._ingestion_policy_id = ingestion_policy_id

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
        if issubclass(IngestionPolicyMapping, dict):
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
        if not isinstance(other, IngestionPolicyMapping):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IngestionPolicyMapping):
            return True

        return self.to_dict() != other.to_dict()
