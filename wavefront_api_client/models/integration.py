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


class Integration(object):
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
        'alerts': 'list[IntegrationAlert]',
        'alias_integrations': 'list[IntegrationAlias]',
        'alias_of': 'str',
        'base_url': 'str',
        'created_epoch_millis': 'int',
        'creator_id': 'str',
        'dashboards': 'list[IntegrationDashboard]',
        'deleted': 'bool',
        'description': 'str',
        'have_metric_dropdown': 'bool',
        'hidden': 'bool',
        'icon': 'str',
        'id': 'str',
        'metrics': 'IntegrationMetrics',
        'metrics_docs': 'str',
        'name': 'str',
        'overview': 'str',
        'setup': 'str',
        'status': 'IntegrationStatus',
        'updated_epoch_millis': 'int',
        'updater_id': 'str',
        'version': 'str'
    }

    attribute_map = {
        'alerts': 'alerts',
        'alias_integrations': 'aliasIntegrations',
        'alias_of': 'aliasOf',
        'base_url': 'baseUrl',
        'created_epoch_millis': 'createdEpochMillis',
        'creator_id': 'creatorId',
        'dashboards': 'dashboards',
        'deleted': 'deleted',
        'description': 'description',
        'have_metric_dropdown': 'haveMetricDropdown',
        'hidden': 'hidden',
        'icon': 'icon',
        'id': 'id',
        'metrics': 'metrics',
        'metrics_docs': 'metricsDocs',
        'name': 'name',
        'overview': 'overview',
        'setup': 'setup',
        'status': 'status',
        'updated_epoch_millis': 'updatedEpochMillis',
        'updater_id': 'updaterId',
        'version': 'version'
    }

    def __init__(self, alerts=None, alias_integrations=None, alias_of=None, base_url=None, created_epoch_millis=None, creator_id=None, dashboards=None, deleted=None, description=None, have_metric_dropdown=None, hidden=None, icon=None, id=None, metrics=None, metrics_docs=None, name=None, overview=None, setup=None, status=None, updated_epoch_millis=None, updater_id=None, version=None, _configuration=None):  # noqa: E501
        """Integration - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._alerts = None
        self._alias_integrations = None
        self._alias_of = None
        self._base_url = None
        self._created_epoch_millis = None
        self._creator_id = None
        self._dashboards = None
        self._deleted = None
        self._description = None
        self._have_metric_dropdown = None
        self._hidden = None
        self._icon = None
        self._id = None
        self._metrics = None
        self._metrics_docs = None
        self._name = None
        self._overview = None
        self._setup = None
        self._status = None
        self._updated_epoch_millis = None
        self._updater_id = None
        self._version = None
        self.discriminator = None

        if alerts is not None:
            self.alerts = alerts
        if alias_integrations is not None:
            self.alias_integrations = alias_integrations
        if alias_of is not None:
            self.alias_of = alias_of
        if base_url is not None:
            self.base_url = base_url
        if created_epoch_millis is not None:
            self.created_epoch_millis = created_epoch_millis
        if creator_id is not None:
            self.creator_id = creator_id
        if dashboards is not None:
            self.dashboards = dashboards
        if deleted is not None:
            self.deleted = deleted
        self.description = description
        self.have_metric_dropdown = have_metric_dropdown
        self.hidden = hidden
        self.icon = icon
        if id is not None:
            self.id = id
        if metrics is not None:
            self.metrics = metrics
        if metrics_docs is not None:
            self.metrics_docs = metrics_docs
        self.name = name
        if overview is not None:
            self.overview = overview
        if setup is not None:
            self.setup = setup
        if status is not None:
            self.status = status
        if updated_epoch_millis is not None:
            self.updated_epoch_millis = updated_epoch_millis
        if updater_id is not None:
            self.updater_id = updater_id
        self.version = version

    @property
    def alerts(self):
        """Gets the alerts of this Integration.  # noqa: E501

        A list of alerts belonging to this integration  # noqa: E501

        :return: The alerts of this Integration.  # noqa: E501
        :rtype: list[IntegrationAlert]
        """
        return self._alerts

    @alerts.setter
    def alerts(self, alerts):
        """Sets the alerts of this Integration.

        A list of alerts belonging to this integration  # noqa: E501

        :param alerts: The alerts of this Integration.  # noqa: E501
        :type: list[IntegrationAlert]
        """

        self._alerts = alerts

    @property
    def alias_integrations(self):
        """Gets the alias_integrations of this Integration.  # noqa: E501

        If set, a list of objects describing integrations that alias this one.  # noqa: E501

        :return: The alias_integrations of this Integration.  # noqa: E501
        :rtype: list[IntegrationAlias]
        """
        return self._alias_integrations

    @alias_integrations.setter
    def alias_integrations(self, alias_integrations):
        """Sets the alias_integrations of this Integration.

        If set, a list of objects describing integrations that alias this one.  # noqa: E501

        :param alias_integrations: The alias_integrations of this Integration.  # noqa: E501
        :type: list[IntegrationAlias]
        """

        self._alias_integrations = alias_integrations

    @property
    def alias_of(self):
        """Gets the alias_of of this Integration.  # noqa: E501

        If set, designates this integration as an alias integration, of the integration whose id is specified.  # noqa: E501

        :return: The alias_of of this Integration.  # noqa: E501
        :rtype: str
        """
        return self._alias_of

    @alias_of.setter
    def alias_of(self, alias_of):
        """Sets the alias_of of this Integration.

        If set, designates this integration as an alias integration, of the integration whose id is specified.  # noqa: E501

        :param alias_of: The alias_of of this Integration.  # noqa: E501
        :type: str
        """

        self._alias_of = alias_of

    @property
    def base_url(self):
        """Gets the base_url of this Integration.  # noqa: E501

        Base URL for this integration's assets  # noqa: E501

        :return: The base_url of this Integration.  # noqa: E501
        :rtype: str
        """
        return self._base_url

    @base_url.setter
    def base_url(self, base_url):
        """Sets the base_url of this Integration.

        Base URL for this integration's assets  # noqa: E501

        :param base_url: The base_url of this Integration.  # noqa: E501
        :type: str
        """

        self._base_url = base_url

    @property
    def created_epoch_millis(self):
        """Gets the created_epoch_millis of this Integration.  # noqa: E501


        :return: The created_epoch_millis of this Integration.  # noqa: E501
        :rtype: int
        """
        return self._created_epoch_millis

    @created_epoch_millis.setter
    def created_epoch_millis(self, created_epoch_millis):
        """Sets the created_epoch_millis of this Integration.


        :param created_epoch_millis: The created_epoch_millis of this Integration.  # noqa: E501
        :type: int
        """

        self._created_epoch_millis = created_epoch_millis

    @property
    def creator_id(self):
        """Gets the creator_id of this Integration.  # noqa: E501


        :return: The creator_id of this Integration.  # noqa: E501
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this Integration.


        :param creator_id: The creator_id of this Integration.  # noqa: E501
        :type: str
        """

        self._creator_id = creator_id

    @property
    def dashboards(self):
        """Gets the dashboards of this Integration.  # noqa: E501

        A list of dashboards belonging to this integration  # noqa: E501

        :return: The dashboards of this Integration.  # noqa: E501
        :rtype: list[IntegrationDashboard]
        """
        return self._dashboards

    @dashboards.setter
    def dashboards(self, dashboards):
        """Sets the dashboards of this Integration.

        A list of dashboards belonging to this integration  # noqa: E501

        :param dashboards: The dashboards of this Integration.  # noqa: E501
        :type: list[IntegrationDashboard]
        """

        self._dashboards = dashboards

    @property
    def deleted(self):
        """Gets the deleted of this Integration.  # noqa: E501


        :return: The deleted of this Integration.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this Integration.


        :param deleted: The deleted of this Integration.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def description(self):
        """Gets the description of this Integration.  # noqa: E501

        Integration description  # noqa: E501

        :return: The description of this Integration.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Integration.

        Integration description  # noqa: E501

        :param description: The description of this Integration.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def have_metric_dropdown(self):
        """Gets the have_metric_dropdown of this Integration.  # noqa: E501

        Integration have metric dropdown or not  # noqa: E501

        :return: The have_metric_dropdown of this Integration.  # noqa: E501
        :rtype: bool
        """
        return self._have_metric_dropdown

    @have_metric_dropdown.setter
    def have_metric_dropdown(self, have_metric_dropdown):
        """Sets the have_metric_dropdown of this Integration.

        Integration have metric dropdown or not  # noqa: E501

        :param have_metric_dropdown: The have_metric_dropdown of this Integration.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and have_metric_dropdown is None:
            raise ValueError("Invalid value for `have_metric_dropdown`, must not be `None`")  # noqa: E501

        self._have_metric_dropdown = have_metric_dropdown

    @property
    def hidden(self):
        """Gets the hidden of this Integration.  # noqa: E501

        Integration is hidden or not  # noqa: E501

        :return: The hidden of this Integration.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this Integration.

        Integration is hidden or not  # noqa: E501

        :param hidden: The hidden of this Integration.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and hidden is None:
            raise ValueError("Invalid value for `hidden`, must not be `None`")  # noqa: E501

        self._hidden = hidden

    @property
    def icon(self):
        """Gets the icon of this Integration.  # noqa: E501

        URI path to the integration icon  # noqa: E501

        :return: The icon of this Integration.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this Integration.

        URI path to the integration icon  # noqa: E501

        :param icon: The icon of this Integration.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and icon is None:
            raise ValueError("Invalid value for `icon`, must not be `None`")  # noqa: E501

        self._icon = icon

    @property
    def id(self):
        """Gets the id of this Integration.  # noqa: E501


        :return: The id of this Integration.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Integration.


        :param id: The id of this Integration.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def metrics(self):
        """Gets the metrics of this Integration.  # noqa: E501


        :return: The metrics of this Integration.  # noqa: E501
        :rtype: IntegrationMetrics
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this Integration.


        :param metrics: The metrics of this Integration.  # noqa: E501
        :type: IntegrationMetrics
        """

        self._metrics = metrics

    @property
    def metrics_docs(self):
        """Gets the metrics_docs of this Integration.  # noqa: E501

        Metric Preview File Name  # noqa: E501

        :return: The metrics_docs of this Integration.  # noqa: E501
        :rtype: str
        """
        return self._metrics_docs

    @metrics_docs.setter
    def metrics_docs(self, metrics_docs):
        """Sets the metrics_docs of this Integration.

        Metric Preview File Name  # noqa: E501

        :param metrics_docs: The metrics_docs of this Integration.  # noqa: E501
        :type: str
        """

        self._metrics_docs = metrics_docs

    @property
    def name(self):
        """Gets the name of this Integration.  # noqa: E501

        Integration name  # noqa: E501

        :return: The name of this Integration.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Integration.

        Integration name  # noqa: E501

        :param name: The name of this Integration.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def overview(self):
        """Gets the overview of this Integration.  # noqa: E501

        Descriptive text giving an overview of integration functionality  # noqa: E501

        :return: The overview of this Integration.  # noqa: E501
        :rtype: str
        """
        return self._overview

    @overview.setter
    def overview(self, overview):
        """Sets the overview of this Integration.

        Descriptive text giving an overview of integration functionality  # noqa: E501

        :param overview: The overview of this Integration.  # noqa: E501
        :type: str
        """

        self._overview = overview

    @property
    def setup(self):
        """Gets the setup of this Integration.  # noqa: E501

        How the integration will be set-up  # noqa: E501

        :return: The setup of this Integration.  # noqa: E501
        :rtype: str
        """
        return self._setup

    @setup.setter
    def setup(self, setup):
        """Sets the setup of this Integration.

        How the integration will be set-up  # noqa: E501

        :param setup: The setup of this Integration.  # noqa: E501
        :type: str
        """

        self._setup = setup

    @property
    def status(self):
        """Gets the status of this Integration.  # noqa: E501


        :return: The status of this Integration.  # noqa: E501
        :rtype: IntegrationStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Integration.


        :param status: The status of this Integration.  # noqa: E501
        :type: IntegrationStatus
        """

        self._status = status

    @property
    def updated_epoch_millis(self):
        """Gets the updated_epoch_millis of this Integration.  # noqa: E501


        :return: The updated_epoch_millis of this Integration.  # noqa: E501
        :rtype: int
        """
        return self._updated_epoch_millis

    @updated_epoch_millis.setter
    def updated_epoch_millis(self, updated_epoch_millis):
        """Sets the updated_epoch_millis of this Integration.


        :param updated_epoch_millis: The updated_epoch_millis of this Integration.  # noqa: E501
        :type: int
        """

        self._updated_epoch_millis = updated_epoch_millis

    @property
    def updater_id(self):
        """Gets the updater_id of this Integration.  # noqa: E501


        :return: The updater_id of this Integration.  # noqa: E501
        :rtype: str
        """
        return self._updater_id

    @updater_id.setter
    def updater_id(self, updater_id):
        """Sets the updater_id of this Integration.


        :param updater_id: The updater_id of this Integration.  # noqa: E501
        :type: str
        """

        self._updater_id = updater_id

    @property
    def version(self):
        """Gets the version of this Integration.  # noqa: E501

        Integration version string  # noqa: E501

        :return: The version of this Integration.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Integration.

        Integration version string  # noqa: E501

        :param version: The version of this Integration.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

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
        if issubclass(Integration, dict):
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
        if not isinstance(other, Integration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Integration):
            return True

        return self.to_dict() != other.to_dict()
