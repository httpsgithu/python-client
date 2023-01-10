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


class ResponseContainerListUserApiToken(object):
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
        'response': 'list[UserApiToken]',
        'status': 'ResponseStatus'
    }

    attribute_map = {
        'response': 'response',
        'status': 'status'
    }

    def __init__(self, response=None, status=None, _configuration=None):  # noqa: E501
        """ResponseContainerListUserApiToken - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._response = None
        self._status = None
        self.discriminator = None

        if response is not None:
            self.response = response
        self.status = status

    @property
    def response(self):
        """Gets the response of this ResponseContainerListUserApiToken.  # noqa: E501


        :return: The response of this ResponseContainerListUserApiToken.  # noqa: E501
        :rtype: list[UserApiToken]
        """
        return self._response

    @response.setter
    def response(self, response):
        """Sets the response of this ResponseContainerListUserApiToken.


        :param response: The response of this ResponseContainerListUserApiToken.  # noqa: E501
        :type: list[UserApiToken]
        """

        self._response = response

    @property
    def status(self):
        """Gets the status of this ResponseContainerListUserApiToken.  # noqa: E501


        :return: The status of this ResponseContainerListUserApiToken.  # noqa: E501
        :rtype: ResponseStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ResponseContainerListUserApiToken.


        :param status: The status of this ResponseContainerListUserApiToken.  # noqa: E501
        :type: ResponseStatus
        """
        if self._configuration.client_side_validation and status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

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
        if issubclass(ResponseContainerListUserApiToken, dict):
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
        if not isinstance(other, ResponseContainerListUserApiToken):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResponseContainerListUserApiToken):
            return True

        return self.to_dict() != other.to_dict()
