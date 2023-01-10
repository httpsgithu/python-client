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


class SnowflakeConfiguration(object):
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
        'account_id': 'str',
        'metric_filter_regex': 'str',
        'password': 'str',
        'private_key': 'str',
        'role': 'str',
        'user_name': 'str',
        'warehouse': 'str'
    }

    attribute_map = {
        'account_id': 'accountID',
        'metric_filter_regex': 'metricFilterRegex',
        'password': 'password',
        'private_key': 'privateKey',
        'role': 'role',
        'user_name': 'userName',
        'warehouse': 'warehouse'
    }

    def __init__(self, account_id=None, metric_filter_regex=None, password=None, private_key=None, role=None, user_name=None, warehouse=None, _configuration=None):  # noqa: E501
        """SnowflakeConfiguration - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_id = None
        self._metric_filter_regex = None
        self._password = None
        self._private_key = None
        self._role = None
        self._user_name = None
        self._warehouse = None
        self.discriminator = None

        self.account_id = account_id
        if metric_filter_regex is not None:
            self.metric_filter_regex = metric_filter_regex
        if password is not None:
            self.password = password
        self.private_key = private_key
        if role is not None:
            self.role = role
        self.user_name = user_name
        if warehouse is not None:
            self.warehouse = warehouse

    @property
    def account_id(self):
        """Gets the account_id of this SnowflakeConfiguration.  # noqa: E501

        Snowflake AccountID  # noqa: E501

        :return: The account_id of this SnowflakeConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this SnowflakeConfiguration.

        Snowflake AccountID  # noqa: E501

        :param account_id: The account_id of this SnowflakeConfiguration.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def metric_filter_regex(self):
        """Gets the metric_filter_regex of this SnowflakeConfiguration.  # noqa: E501

        A regular expression that a metric name must match (case-insensitively) in order to be ingested  # noqa: E501

        :return: The metric_filter_regex of this SnowflakeConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._metric_filter_regex

    @metric_filter_regex.setter
    def metric_filter_regex(self, metric_filter_regex):
        """Sets the metric_filter_regex of this SnowflakeConfiguration.

        A regular expression that a metric name must match (case-insensitively) in order to be ingested  # noqa: E501

        :param metric_filter_regex: The metric_filter_regex of this SnowflakeConfiguration.  # noqa: E501
        :type: str
        """

        self._metric_filter_regex = metric_filter_regex

    @property
    def password(self):
        """Gets the password of this SnowflakeConfiguration.  # noqa: E501

        Snowflake Password  # noqa: E501

        :return: The password of this SnowflakeConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this SnowflakeConfiguration.

        Snowflake Password  # noqa: E501

        :param password: The password of this SnowflakeConfiguration.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def private_key(self):
        """Gets the private_key of this SnowflakeConfiguration.  # noqa: E501

        Snowflake Private Key  # noqa: E501

        :return: The private_key of this SnowflakeConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this SnowflakeConfiguration.

        Snowflake Private Key  # noqa: E501

        :param private_key: The private_key of this SnowflakeConfiguration.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and private_key is None:
            raise ValueError("Invalid value for `private_key`, must not be `None`")  # noqa: E501

        self._private_key = private_key

    @property
    def role(self):
        """Gets the role of this SnowflakeConfiguration.  # noqa: E501

        Role to be used while querying snowflake database  # noqa: E501

        :return: The role of this SnowflakeConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this SnowflakeConfiguration.

        Role to be used while querying snowflake database  # noqa: E501

        :param role: The role of this SnowflakeConfiguration.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def user_name(self):
        """Gets the user_name of this SnowflakeConfiguration.  # noqa: E501

        Snowflake Username  # noqa: E501

        :return: The user_name of this SnowflakeConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this SnowflakeConfiguration.

        Snowflake Username  # noqa: E501

        :param user_name: The user_name of this SnowflakeConfiguration.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and user_name is None:
            raise ValueError("Invalid value for `user_name`, must not be `None`")  # noqa: E501

        self._user_name = user_name

    @property
    def warehouse(self):
        """Gets the warehouse of this SnowflakeConfiguration.  # noqa: E501

        Warehouse to be used while querying snowflake database  # noqa: E501

        :return: The warehouse of this SnowflakeConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._warehouse

    @warehouse.setter
    def warehouse(self, warehouse):
        """Sets the warehouse of this SnowflakeConfiguration.

        Warehouse to be used while querying snowflake database  # noqa: E501

        :param warehouse: The warehouse of this SnowflakeConfiguration.  # noqa: E501
        :type: str
        """

        self._warehouse = warehouse

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
        if issubclass(SnowflakeConfiguration, dict):
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
        if not isinstance(other, SnowflakeConfiguration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SnowflakeConfiguration):
            return True

        return self.to_dict() != other.to_dict()
