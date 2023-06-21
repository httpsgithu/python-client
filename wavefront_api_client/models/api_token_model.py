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


class ApiTokenModel(object):
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
        'account': 'str',
        'account_type': 'str',
        'created_epoch_millis': 'int',
        'customer': 'str',
        'date_generated': 'int',
        'id': 'str',
        'last_used': 'int',
        'name': 'str'
    }

    attribute_map = {
        'account': 'account',
        'account_type': 'accountType',
        'created_epoch_millis': 'createdEpochMillis',
        'customer': 'customer',
        'date_generated': 'dateGenerated',
        'id': 'id',
        'last_used': 'lastUsed',
        'name': 'name'
    }

    def __init__(self, account=None, account_type=None, created_epoch_millis=None, customer=None, date_generated=None, id=None, last_used=None, name=None, _configuration=None):  # noqa: E501
        """ApiTokenModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account = None
        self._account_type = None
        self._created_epoch_millis = None
        self._customer = None
        self._date_generated = None
        self._id = None
        self._last_used = None
        self._name = None
        self.discriminator = None

        if account is not None:
            self.account = account
        if account_type is not None:
            self.account_type = account_type
        if created_epoch_millis is not None:
            self.created_epoch_millis = created_epoch_millis
        if customer is not None:
            self.customer = customer
        if date_generated is not None:
            self.date_generated = date_generated
        if id is not None:
            self.id = id
        if last_used is not None:
            self.last_used = last_used
        if name is not None:
            self.name = name

    @property
    def account(self):
        """Gets the account of this ApiTokenModel.  # noqa: E501

        The account who generated this token.  # noqa: E501

        :return: The account of this ApiTokenModel.  # noqa: E501
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this ApiTokenModel.

        The account who generated this token.  # noqa: E501

        :param account: The account of this ApiTokenModel.  # noqa: E501
        :type: str
        """

        self._account = account

    @property
    def account_type(self):
        """Gets the account_type of this ApiTokenModel.  # noqa: E501

        The user or service account generated this token.  # noqa: E501

        :return: The account_type of this ApiTokenModel.  # noqa: E501
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this ApiTokenModel.

        The user or service account generated this token.  # noqa: E501

        :param account_type: The account_type of this ApiTokenModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["USER_ACCOUNT", "SERVICE_ACCOUNT", "INACTIVE_SERVICE_ACCOUNT", "CSP_USER_ACCOUNT", "CSP_AUTHORIZED_USER_ACCOUNT", "CSP_SERVICE_ACCOUNT", "CSP_AUTHORIZED_SERVICE_ACCOUNT"]  # noqa: E501
        if (self._configuration.client_side_validation and
                account_type not in allowed_values):
            raise ValueError(
                "Invalid value for `account_type` ({0}), must be one of {1}"  # noqa: E501
                .format(account_type, allowed_values)
            )

        self._account_type = account_type

    @property
    def created_epoch_millis(self):
        """Gets the created_epoch_millis of this ApiTokenModel.  # noqa: E501


        :return: The created_epoch_millis of this ApiTokenModel.  # noqa: E501
        :rtype: int
        """
        return self._created_epoch_millis

    @created_epoch_millis.setter
    def created_epoch_millis(self, created_epoch_millis):
        """Sets the created_epoch_millis of this ApiTokenModel.


        :param created_epoch_millis: The created_epoch_millis of this ApiTokenModel.  # noqa: E501
        :type: int
        """

        self._created_epoch_millis = created_epoch_millis

    @property
    def customer(self):
        """Gets the customer of this ApiTokenModel.  # noqa: E501

        The id of the customer to which the token belongs.  # noqa: E501

        :return: The customer of this ApiTokenModel.  # noqa: E501
        :rtype: str
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this ApiTokenModel.

        The id of the customer to which the token belongs.  # noqa: E501

        :param customer: The customer of this ApiTokenModel.  # noqa: E501
        :type: str
        """

        self._customer = customer

    @property
    def date_generated(self):
        """Gets the date_generated of this ApiTokenModel.  # noqa: E501

        The generation date of the token.  # noqa: E501

        :return: The date_generated of this ApiTokenModel.  # noqa: E501
        :rtype: int
        """
        return self._date_generated

    @date_generated.setter
    def date_generated(self, date_generated):
        """Sets the date_generated of this ApiTokenModel.

        The generation date of the token.  # noqa: E501

        :param date_generated: The date_generated of this ApiTokenModel.  # noqa: E501
        :type: int
        """

        self._date_generated = date_generated

    @property
    def id(self):
        """Gets the id of this ApiTokenModel.  # noqa: E501

        The unique identifier of the token.  # noqa: E501

        :return: The id of this ApiTokenModel.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiTokenModel.

        The unique identifier of the token.  # noqa: E501

        :param id: The id of this ApiTokenModel.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def last_used(self):
        """Gets the last_used of this ApiTokenModel.  # noqa: E501

        The last time this token was used.  # noqa: E501

        :return: The last_used of this ApiTokenModel.  # noqa: E501
        :rtype: int
        """
        return self._last_used

    @last_used.setter
    def last_used(self, last_used):
        """Sets the last_used of this ApiTokenModel.

        The last time this token was used.  # noqa: E501

        :param last_used: The last_used of this ApiTokenModel.  # noqa: E501
        :type: int
        """

        self._last_used = last_used

    @property
    def name(self):
        """Gets the name of this ApiTokenModel.  # noqa: E501

        The name of the token.  # noqa: E501

        :return: The name of this ApiTokenModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiTokenModel.

        The name of the token.  # noqa: E501

        :param name: The name of this ApiTokenModel.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(ApiTokenModel, dict):
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
        if not isinstance(other, ApiTokenModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiTokenModel):
            return True

        return self.to_dict() != other.to_dict()
