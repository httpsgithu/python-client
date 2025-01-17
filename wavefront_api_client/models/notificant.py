# coding: utf-8

"""
    Wavefront REST API Documentation

    <p>The Wavefront REST API enables you to interact with Wavefront servers using standard REST API tools. You can use the REST API to automate commonly executed operations such as automatically tagging sources.</p><p>When you make REST API calls outside the Wavefront REST API documentation you must add the header \"Authorization: Bearer &lt;&lt;API-TOKEN&gt;&gt;\" to your HTTP requests.</p>  # noqa: E501

    OpenAPI spec version: v2
    Contact: chitimba@wavefront.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from wavefront_api_client.configuration import Configuration


class Notificant(object):
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
        'content_type': 'str',
        'created_epoch_millis': 'int',
        'creator_id': 'str',
        'custom_http_headers': 'dict(str, str)',
        'customer_id': 'str',
        'description': 'str',
        'email_subject': 'str',
        'id': 'str',
        'is_html_content': 'bool',
        'method': 'str',
        'recipient': 'str',
        'routes': 'list[AlertRoute]',
        'template': 'str',
        'title': 'str',
        'triggers': 'list[str]',
        'updated_epoch_millis': 'int',
        'updater_id': 'str'
    }

    attribute_map = {
        'content_type': 'contentType',
        'created_epoch_millis': 'createdEpochMillis',
        'creator_id': 'creatorId',
        'custom_http_headers': 'customHttpHeaders',
        'customer_id': 'customerId',
        'description': 'description',
        'email_subject': 'emailSubject',
        'id': 'id',
        'is_html_content': 'isHtmlContent',
        'method': 'method',
        'recipient': 'recipient',
        'routes': 'routes',
        'template': 'template',
        'title': 'title',
        'triggers': 'triggers',
        'updated_epoch_millis': 'updatedEpochMillis',
        'updater_id': 'updaterId'
    }

    def __init__(self, content_type=None, created_epoch_millis=None, creator_id=None, custom_http_headers=None, customer_id=None, description=None, email_subject=None, id=None, is_html_content=None, method=None, recipient=None, routes=None, template=None, title=None, triggers=None, updated_epoch_millis=None, updater_id=None, _configuration=None):  # noqa: E501
        """Notificant - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._content_type = None
        self._created_epoch_millis = None
        self._creator_id = None
        self._custom_http_headers = None
        self._customer_id = None
        self._description = None
        self._email_subject = None
        self._id = None
        self._is_html_content = None
        self._method = None
        self._recipient = None
        self._routes = None
        self._template = None
        self._title = None
        self._triggers = None
        self._updated_epoch_millis = None
        self._updater_id = None
        self.discriminator = None

        if content_type is not None:
            self.content_type = content_type
        if created_epoch_millis is not None:
            self.created_epoch_millis = created_epoch_millis
        if creator_id is not None:
            self.creator_id = creator_id
        if custom_http_headers is not None:
            self.custom_http_headers = custom_http_headers
        if customer_id is not None:
            self.customer_id = customer_id
        self.description = description
        if email_subject is not None:
            self.email_subject = email_subject
        if id is not None:
            self.id = id
        if is_html_content is not None:
            self.is_html_content = is_html_content
        self.method = method
        self.recipient = recipient
        if routes is not None:
            self.routes = routes
        self.template = template
        self.title = title
        self.triggers = triggers
        if updated_epoch_millis is not None:
            self.updated_epoch_millis = updated_epoch_millis
        if updater_id is not None:
            self.updater_id = updater_id

    @property
    def content_type(self):
        """Gets the content_type of this Notificant.  # noqa: E501

        The value of the Content-Type header of the webhook POST request.  # noqa: E501

        :return: The content_type of this Notificant.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this Notificant.

        The value of the Content-Type header of the webhook POST request.  # noqa: E501

        :param content_type: The content_type of this Notificant.  # noqa: E501
        :type: str
        """
        allowed_values = ["application/json", "text/html", "text/plain", "application/x-www-form-urlencoded", ""]  # noqa: E501
        if (self._configuration.client_side_validation and
                content_type not in allowed_values):
            raise ValueError(
                "Invalid value for `content_type` ({0}), must be one of {1}"  # noqa: E501
                .format(content_type, allowed_values)
            )

        self._content_type = content_type

    @property
    def created_epoch_millis(self):
        """Gets the created_epoch_millis of this Notificant.  # noqa: E501


        :return: The created_epoch_millis of this Notificant.  # noqa: E501
        :rtype: int
        """
        return self._created_epoch_millis

    @created_epoch_millis.setter
    def created_epoch_millis(self, created_epoch_millis):
        """Sets the created_epoch_millis of this Notificant.


        :param created_epoch_millis: The created_epoch_millis of this Notificant.  # noqa: E501
        :type: int
        """

        self._created_epoch_millis = created_epoch_millis

    @property
    def creator_id(self):
        """Gets the creator_id of this Notificant.  # noqa: E501


        :return: The creator_id of this Notificant.  # noqa: E501
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this Notificant.


        :param creator_id: The creator_id of this Notificant.  # noqa: E501
        :type: str
        """

        self._creator_id = creator_id

    @property
    def custom_http_headers(self):
        """Gets the custom_http_headers of this Notificant.  # noqa: E501

        A string->string map specifying the custom HTTP header key / value pairs that will be sent in the requests of this web hook  # noqa: E501

        :return: The custom_http_headers of this Notificant.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._custom_http_headers

    @custom_http_headers.setter
    def custom_http_headers(self, custom_http_headers):
        """Sets the custom_http_headers of this Notificant.

        A string->string map specifying the custom HTTP header key / value pairs that will be sent in the requests of this web hook  # noqa: E501

        :param custom_http_headers: The custom_http_headers of this Notificant.  # noqa: E501
        :type: dict(str, str)
        """

        self._custom_http_headers = custom_http_headers

    @property
    def customer_id(self):
        """Gets the customer_id of this Notificant.  # noqa: E501


        :return: The customer_id of this Notificant.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this Notificant.


        :param customer_id: The customer_id of this Notificant.  # noqa: E501
        :type: str
        """

        self._customer_id = customer_id

    @property
    def description(self):
        """Gets the description of this Notificant.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this Notificant.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Notificant.

        Description  # noqa: E501

        :param description: The description of this Notificant.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def email_subject(self):
        """Gets the email_subject of this Notificant.  # noqa: E501

        The subject title of an email notification target  # noqa: E501

        :return: The email_subject of this Notificant.  # noqa: E501
        :rtype: str
        """
        return self._email_subject

    @email_subject.setter
    def email_subject(self, email_subject):
        """Sets the email_subject of this Notificant.

        The subject title of an email notification target  # noqa: E501

        :param email_subject: The email_subject of this Notificant.  # noqa: E501
        :type: str
        """

        self._email_subject = email_subject

    @property
    def id(self):
        """Gets the id of this Notificant.  # noqa: E501


        :return: The id of this Notificant.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Notificant.


        :param id: The id of this Notificant.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def is_html_content(self):
        """Gets the is_html_content of this Notificant.  # noqa: E501

        Determine whether the email alert target content is sent as html or text.  # noqa: E501

        :return: The is_html_content of this Notificant.  # noqa: E501
        :rtype: bool
        """
        return self._is_html_content

    @is_html_content.setter
    def is_html_content(self, is_html_content):
        """Sets the is_html_content of this Notificant.

        Determine whether the email alert target content is sent as html or text.  # noqa: E501

        :param is_html_content: The is_html_content of this Notificant.  # noqa: E501
        :type: bool
        """

        self._is_html_content = is_html_content

    @property
    def method(self):
        """Gets the method of this Notificant.  # noqa: E501

        The notification method used for notification target.  # noqa: E501

        :return: The method of this Notificant.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this Notificant.

        The notification method used for notification target.  # noqa: E501

        :param method: The method of this Notificant.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and method is None:
            raise ValueError("Invalid value for `method`, must not be `None`")  # noqa: E501
        allowed_values = ["WEBHOOK", "EMAIL", "PAGERDUTY"]  # noqa: E501
        if (self._configuration.client_side_validation and
                method not in allowed_values):
            raise ValueError(
                "Invalid value for `method` ({0}), must be one of {1}"  # noqa: E501
                .format(method, allowed_values)
            )

        self._method = method

    @property
    def recipient(self):
        """Gets the recipient of this Notificant.  # noqa: E501

        The end point for the notification target.EMAIL: email address.  PAGERDUTY: PagerDuty routing Key.  WEBHOOK: URL end point  # noqa: E501

        :return: The recipient of this Notificant.  # noqa: E501
        :rtype: str
        """
        return self._recipient

    @recipient.setter
    def recipient(self, recipient):
        """Sets the recipient of this Notificant.

        The end point for the notification target.EMAIL: email address.  PAGERDUTY: PagerDuty routing Key.  WEBHOOK: URL end point  # noqa: E501

        :param recipient: The recipient of this Notificant.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and recipient is None:
            raise ValueError("Invalid value for `recipient`, must not be `None`")  # noqa: E501

        self._recipient = recipient

    @property
    def routes(self):
        """Gets the routes of this Notificant.  # noqa: E501

        List of routing targets that this notificant will notify.  # noqa: E501

        :return: The routes of this Notificant.  # noqa: E501
        :rtype: list[AlertRoute]
        """
        return self._routes

    @routes.setter
    def routes(self, routes):
        """Sets the routes of this Notificant.

        List of routing targets that this notificant will notify.  # noqa: E501

        :param routes: The routes of this Notificant.  # noqa: E501
        :type: list[AlertRoute]
        """

        self._routes = routes

    @property
    def template(self):
        """Gets the template of this Notificant.  # noqa: E501

        A mustache template that will form the body of the POST request, email and summary of the PagerDuty.  # noqa: E501

        :return: The template of this Notificant.  # noqa: E501
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this Notificant.

        A mustache template that will form the body of the POST request, email and summary of the PagerDuty.  # noqa: E501

        :param template: The template of this Notificant.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and template is None:
            raise ValueError("Invalid value for `template`, must not be `None`")  # noqa: E501

        self._template = template

    @property
    def title(self):
        """Gets the title of this Notificant.  # noqa: E501

        Title  # noqa: E501

        :return: The title of this Notificant.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Notificant.

        Title  # noqa: E501

        :param title: The title of this Notificant.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def triggers(self):
        """Gets the triggers of this Notificant.  # noqa: E501

        A list of occurrences on which this webhook will be fired.  Valid values are ALERT_OPENED, ALERT_UPDATED, ALERT_RESOLVED, ALERT_MAINTENANCE, ALERT_SNOOZED  # noqa: E501

        :return: The triggers of this Notificant.  # noqa: E501
        :rtype: list[str]
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        """Sets the triggers of this Notificant.

        A list of occurrences on which this webhook will be fired.  Valid values are ALERT_OPENED, ALERT_UPDATED, ALERT_RESOLVED, ALERT_MAINTENANCE, ALERT_SNOOZED  # noqa: E501

        :param triggers: The triggers of this Notificant.  # noqa: E501
        :type: list[str]
        """
        if self._configuration.client_side_validation and triggers is None:
            raise ValueError("Invalid value for `triggers`, must not be `None`")  # noqa: E501
        allowed_values = ["ALERT_OPENED", "ALERT_UPDATED", "ALERT_RESOLVED", "ALERT_MAINTENANCE", "ALERT_SNOOZED", "ALERT_INVALID", "ALERT_NO_LONGER_INVALID", "ALERT_TESTING", "ALERT_RETRIGGERED", "ALERT_NO_DATA", "ALERT_NO_DATA_RESOLVED", "ALERT_NO_DATA_MAINTENANCE", "ALERT_SEVERITY_UPDATE", "ALERT_NOTIFICATION_PREVIEW"]  # noqa: E501
        if (self._configuration.client_side_validation and
                not set(triggers).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `triggers` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(triggers) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._triggers = triggers

    @property
    def updated_epoch_millis(self):
        """Gets the updated_epoch_millis of this Notificant.  # noqa: E501


        :return: The updated_epoch_millis of this Notificant.  # noqa: E501
        :rtype: int
        """
        return self._updated_epoch_millis

    @updated_epoch_millis.setter
    def updated_epoch_millis(self, updated_epoch_millis):
        """Sets the updated_epoch_millis of this Notificant.


        :param updated_epoch_millis: The updated_epoch_millis of this Notificant.  # noqa: E501
        :type: int
        """

        self._updated_epoch_millis = updated_epoch_millis

    @property
    def updater_id(self):
        """Gets the updater_id of this Notificant.  # noqa: E501


        :return: The updater_id of this Notificant.  # noqa: E501
        :rtype: str
        """
        return self._updater_id

    @updater_id.setter
    def updater_id(self, updater_id):
        """Sets the updater_id of this Notificant.


        :param updater_id: The updater_id of this Notificant.  # noqa: E501
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
        if issubclass(Notificant, dict):
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
        if not isinstance(other, Notificant):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Notificant):
            return True

        return self.to_dict() != other.to_dict()
