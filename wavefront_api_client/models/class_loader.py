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


class ClassLoader(object):
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
        'defined_packages': 'list[Package]',
        'name': 'str',
        'parent': 'ClassLoader',
        'registered_as_parallel_capable': 'bool',
        'unnamed_module': 'Module'
    }

    attribute_map = {
        'defined_packages': 'definedPackages',
        'name': 'name',
        'parent': 'parent',
        'registered_as_parallel_capable': 'registeredAsParallelCapable',
        'unnamed_module': 'unnamedModule'
    }

    def __init__(self, defined_packages=None, name=None, parent=None, registered_as_parallel_capable=None, unnamed_module=None, _configuration=None):  # noqa: E501
        """ClassLoader - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._defined_packages = None
        self._name = None
        self._parent = None
        self._registered_as_parallel_capable = None
        self._unnamed_module = None
        self.discriminator = None

        if defined_packages is not None:
            self.defined_packages = defined_packages
        if name is not None:
            self.name = name
        if parent is not None:
            self.parent = parent
        if registered_as_parallel_capable is not None:
            self.registered_as_parallel_capable = registered_as_parallel_capable
        if unnamed_module is not None:
            self.unnamed_module = unnamed_module

    @property
    def defined_packages(self):
        """Gets the defined_packages of this ClassLoader.  # noqa: E501


        :return: The defined_packages of this ClassLoader.  # noqa: E501
        :rtype: list[Package]
        """
        return self._defined_packages

    @defined_packages.setter
    def defined_packages(self, defined_packages):
        """Sets the defined_packages of this ClassLoader.


        :param defined_packages: The defined_packages of this ClassLoader.  # noqa: E501
        :type: list[Package]
        """

        self._defined_packages = defined_packages

    @property
    def name(self):
        """Gets the name of this ClassLoader.  # noqa: E501


        :return: The name of this ClassLoader.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClassLoader.


        :param name: The name of this ClassLoader.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def parent(self):
        """Gets the parent of this ClassLoader.  # noqa: E501


        :return: The parent of this ClassLoader.  # noqa: E501
        :rtype: ClassLoader
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this ClassLoader.


        :param parent: The parent of this ClassLoader.  # noqa: E501
        :type: ClassLoader
        """

        self._parent = parent

    @property
    def registered_as_parallel_capable(self):
        """Gets the registered_as_parallel_capable of this ClassLoader.  # noqa: E501


        :return: The registered_as_parallel_capable of this ClassLoader.  # noqa: E501
        :rtype: bool
        """
        return self._registered_as_parallel_capable

    @registered_as_parallel_capable.setter
    def registered_as_parallel_capable(self, registered_as_parallel_capable):
        """Sets the registered_as_parallel_capable of this ClassLoader.


        :param registered_as_parallel_capable: The registered_as_parallel_capable of this ClassLoader.  # noqa: E501
        :type: bool
        """

        self._registered_as_parallel_capable = registered_as_parallel_capable

    @property
    def unnamed_module(self):
        """Gets the unnamed_module of this ClassLoader.  # noqa: E501


        :return: The unnamed_module of this ClassLoader.  # noqa: E501
        :rtype: Module
        """
        return self._unnamed_module

    @unnamed_module.setter
    def unnamed_module(self, unnamed_module):
        """Sets the unnamed_module of this ClassLoader.


        :param unnamed_module: The unnamed_module of this ClassLoader.  # noqa: E501
        :type: Module
        """

        self._unnamed_module = unnamed_module

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
        if issubclass(ClassLoader, dict):
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
        if not isinstance(other, ClassLoader):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClassLoader):
            return True

        return self.to_dict() != other.to_dict()
