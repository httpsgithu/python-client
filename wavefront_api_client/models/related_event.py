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


class RelatedEvent(object):
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
        'alert_tags': 'list[str]',
        'annotations': 'dict(str, str)',
        'can_close': 'bool',
        'can_delete': 'bool',
        'computed_hlps': 'list[SourceLabelPair]',
        'created_at': 'int',
        'created_epoch_millis': 'int',
        'creator_id': 'str',
        'creator_type': 'list[str]',
        'dimensions': 'dict(str, list[str])',
        'end_time': 'int',
        'hosts': 'list[str]',
        'id': 'str',
        'is_ephemeral': 'bool',
        'is_user_event': 'bool',
        'metrics_used': 'list[str]',
        'name': 'str',
        'related_data': 'RelatedData',
        'running_state': 'str',
        'similarity_score': 'float',
        'start_time': 'int',
        'summarized_events': 'int',
        'table': 'str',
        'tags': 'list[str]',
        'updated_at': 'int',
        'updated_epoch_millis': 'int',
        'updater_id': 'str'
    }

    attribute_map = {
        'alert_tags': 'alertTags',
        'annotations': 'annotations',
        'can_close': 'canClose',
        'can_delete': 'canDelete',
        'computed_hlps': 'computedHlps',
        'created_at': 'createdAt',
        'created_epoch_millis': 'createdEpochMillis',
        'creator_id': 'creatorId',
        'creator_type': 'creatorType',
        'dimensions': 'dimensions',
        'end_time': 'endTime',
        'hosts': 'hosts',
        'id': 'id',
        'is_ephemeral': 'isEphemeral',
        'is_user_event': 'isUserEvent',
        'metrics_used': 'metricsUsed',
        'name': 'name',
        'related_data': 'relatedData',
        'running_state': 'runningState',
        'similarity_score': 'similarityScore',
        'start_time': 'startTime',
        'summarized_events': 'summarizedEvents',
        'table': 'table',
        'tags': 'tags',
        'updated_at': 'updatedAt',
        'updated_epoch_millis': 'updatedEpochMillis',
        'updater_id': 'updaterId'
    }

    def __init__(self, alert_tags=None, annotations=None, can_close=None, can_delete=None, computed_hlps=None, created_at=None, created_epoch_millis=None, creator_id=None, creator_type=None, dimensions=None, end_time=None, hosts=None, id=None, is_ephemeral=None, is_user_event=None, metrics_used=None, name=None, related_data=None, running_state=None, similarity_score=None, start_time=None, summarized_events=None, table=None, tags=None, updated_at=None, updated_epoch_millis=None, updater_id=None, _configuration=None):  # noqa: E501
        """RelatedEvent - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._alert_tags = None
        self._annotations = None
        self._can_close = None
        self._can_delete = None
        self._computed_hlps = None
        self._created_at = None
        self._created_epoch_millis = None
        self._creator_id = None
        self._creator_type = None
        self._dimensions = None
        self._end_time = None
        self._hosts = None
        self._id = None
        self._is_ephemeral = None
        self._is_user_event = None
        self._metrics_used = None
        self._name = None
        self._related_data = None
        self._running_state = None
        self._similarity_score = None
        self._start_time = None
        self._summarized_events = None
        self._table = None
        self._tags = None
        self._updated_at = None
        self._updated_epoch_millis = None
        self._updater_id = None
        self.discriminator = None

        if alert_tags is not None:
            self.alert_tags = alert_tags
        self.annotations = annotations
        if can_close is not None:
            self.can_close = can_close
        if can_delete is not None:
            self.can_delete = can_delete
        if computed_hlps is not None:
            self.computed_hlps = computed_hlps
        if created_at is not None:
            self.created_at = created_at
        if created_epoch_millis is not None:
            self.created_epoch_millis = created_epoch_millis
        if creator_id is not None:
            self.creator_id = creator_id
        if creator_type is not None:
            self.creator_type = creator_type
        if dimensions is not None:
            self.dimensions = dimensions
        if end_time is not None:
            self.end_time = end_time
        if hosts is not None:
            self.hosts = hosts
        if id is not None:
            self.id = id
        if is_ephemeral is not None:
            self.is_ephemeral = is_ephemeral
        if is_user_event is not None:
            self.is_user_event = is_user_event
        if metrics_used is not None:
            self.metrics_used = metrics_used
        self.name = name
        if related_data is not None:
            self.related_data = related_data
        if running_state is not None:
            self.running_state = running_state
        if similarity_score is not None:
            self.similarity_score = similarity_score
        self.start_time = start_time
        if summarized_events is not None:
            self.summarized_events = summarized_events
        if table is not None:
            self.table = table
        if tags is not None:
            self.tags = tags
        if updated_at is not None:
            self.updated_at = updated_at
        if updated_epoch_millis is not None:
            self.updated_epoch_millis = updated_epoch_millis
        if updater_id is not None:
            self.updater_id = updater_id

    @property
    def alert_tags(self):
        """Gets the alert_tags of this RelatedEvent.  # noqa: E501

        The list of tags on the alert which created this event.  # noqa: E501

        :return: The alert_tags of this RelatedEvent.  # noqa: E501
        :rtype: list[str]
        """
        return self._alert_tags

    @alert_tags.setter
    def alert_tags(self, alert_tags):
        """Sets the alert_tags of this RelatedEvent.

        The list of tags on the alert which created this event.  # noqa: E501

        :param alert_tags: The alert_tags of this RelatedEvent.  # noqa: E501
        :type: list[str]
        """

        self._alert_tags = alert_tags

    @property
    def annotations(self):
        """Gets the annotations of this RelatedEvent.  # noqa: E501

        A string->string map of additional annotations on the event  # noqa: E501

        :return: The annotations of this RelatedEvent.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this RelatedEvent.

        A string->string map of additional annotations on the event  # noqa: E501

        :param annotations: The annotations of this RelatedEvent.  # noqa: E501
        :type: dict(str, str)
        """
        if self._configuration.client_side_validation and annotations is None:
            raise ValueError("Invalid value for `annotations`, must not be `None`")  # noqa: E501

        self._annotations = annotations

    @property
    def can_close(self):
        """Gets the can_close of this RelatedEvent.  # noqa: E501


        :return: The can_close of this RelatedEvent.  # noqa: E501
        :rtype: bool
        """
        return self._can_close

    @can_close.setter
    def can_close(self, can_close):
        """Sets the can_close of this RelatedEvent.


        :param can_close: The can_close of this RelatedEvent.  # noqa: E501
        :type: bool
        """

        self._can_close = can_close

    @property
    def can_delete(self):
        """Gets the can_delete of this RelatedEvent.  # noqa: E501


        :return: The can_delete of this RelatedEvent.  # noqa: E501
        :rtype: bool
        """
        return self._can_delete

    @can_delete.setter
    def can_delete(self, can_delete):
        """Sets the can_delete of this RelatedEvent.


        :param can_delete: The can_delete of this RelatedEvent.  # noqa: E501
        :type: bool
        """

        self._can_delete = can_delete

    @property
    def computed_hlps(self):
        """Gets the computed_hlps of this RelatedEvent.  # noqa: E501

        All the host/label/tags of the event.  # noqa: E501

        :return: The computed_hlps of this RelatedEvent.  # noqa: E501
        :rtype: list[SourceLabelPair]
        """
        return self._computed_hlps

    @computed_hlps.setter
    def computed_hlps(self, computed_hlps):
        """Sets the computed_hlps of this RelatedEvent.

        All the host/label/tags of the event.  # noqa: E501

        :param computed_hlps: The computed_hlps of this RelatedEvent.  # noqa: E501
        :type: list[SourceLabelPair]
        """

        self._computed_hlps = computed_hlps

    @property
    def created_at(self):
        """Gets the created_at of this RelatedEvent.  # noqa: E501


        :return: The created_at of this RelatedEvent.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this RelatedEvent.


        :param created_at: The created_at of this RelatedEvent.  # noqa: E501
        :type: int
        """

        self._created_at = created_at

    @property
    def created_epoch_millis(self):
        """Gets the created_epoch_millis of this RelatedEvent.  # noqa: E501


        :return: The created_epoch_millis of this RelatedEvent.  # noqa: E501
        :rtype: int
        """
        return self._created_epoch_millis

    @created_epoch_millis.setter
    def created_epoch_millis(self, created_epoch_millis):
        """Sets the created_epoch_millis of this RelatedEvent.


        :param created_epoch_millis: The created_epoch_millis of this RelatedEvent.  # noqa: E501
        :type: int
        """

        self._created_epoch_millis = created_epoch_millis

    @property
    def creator_id(self):
        """Gets the creator_id of this RelatedEvent.  # noqa: E501


        :return: The creator_id of this RelatedEvent.  # noqa: E501
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this RelatedEvent.


        :param creator_id: The creator_id of this RelatedEvent.  # noqa: E501
        :type: str
        """

        self._creator_id = creator_id

    @property
    def creator_type(self):
        """Gets the creator_type of this RelatedEvent.  # noqa: E501


        :return: The creator_type of this RelatedEvent.  # noqa: E501
        :rtype: list[str]
        """
        return self._creator_type

    @creator_type.setter
    def creator_type(self, creator_type):
        """Sets the creator_type of this RelatedEvent.


        :param creator_type: The creator_type of this RelatedEvent.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["USER", "ALERT", "SYSTEM"]  # noqa: E501
        if (self._configuration.client_side_validation and
                not set(creator_type).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `creator_type` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(creator_type) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._creator_type = creator_type

    @property
    def dimensions(self):
        """Gets the dimensions of this RelatedEvent.  # noqa: E501

        A string-><list of strings> map of additional dimension info on the event  # noqa: E501

        :return: The dimensions of this RelatedEvent.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this RelatedEvent.

        A string-><list of strings> map of additional dimension info on the event  # noqa: E501

        :param dimensions: The dimensions of this RelatedEvent.  # noqa: E501
        :type: dict(str, list[str])
        """

        self._dimensions = dimensions

    @property
    def end_time(self):
        """Gets the end_time of this RelatedEvent.  # noqa: E501

        End time of the event, in epoch millis.  Set to startTime + 1 for an instantaneous event  # noqa: E501

        :return: The end_time of this RelatedEvent.  # noqa: E501
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this RelatedEvent.

        End time of the event, in epoch millis.  Set to startTime + 1 for an instantaneous event  # noqa: E501

        :param end_time: The end_time of this RelatedEvent.  # noqa: E501
        :type: int
        """

        self._end_time = end_time

    @property
    def hosts(self):
        """Gets the hosts of this RelatedEvent.  # noqa: E501

        A list of sources/hosts affected by the event  # noqa: E501

        :return: The hosts of this RelatedEvent.  # noqa: E501
        :rtype: list[str]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this RelatedEvent.

        A list of sources/hosts affected by the event  # noqa: E501

        :param hosts: The hosts of this RelatedEvent.  # noqa: E501
        :type: list[str]
        """

        self._hosts = hosts

    @property
    def id(self):
        """Gets the id of this RelatedEvent.  # noqa: E501


        :return: The id of this RelatedEvent.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RelatedEvent.


        :param id: The id of this RelatedEvent.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def is_ephemeral(self):
        """Gets the is_ephemeral of this RelatedEvent.  # noqa: E501

        Whether the event is an artificial event generated by a literal expression or alert backtesting, i.e. not stored in the Wavefront backend  # noqa: E501

        :return: The is_ephemeral of this RelatedEvent.  # noqa: E501
        :rtype: bool
        """
        return self._is_ephemeral

    @is_ephemeral.setter
    def is_ephemeral(self, is_ephemeral):
        """Sets the is_ephemeral of this RelatedEvent.

        Whether the event is an artificial event generated by a literal expression or alert backtesting, i.e. not stored in the Wavefront backend  # noqa: E501

        :param is_ephemeral: The is_ephemeral of this RelatedEvent.  # noqa: E501
        :type: bool
        """

        self._is_ephemeral = is_ephemeral

    @property
    def is_user_event(self):
        """Gets the is_user_event of this RelatedEvent.  # noqa: E501

        Whether this event was created by a user, versus the system.  Default: system  # noqa: E501

        :return: The is_user_event of this RelatedEvent.  # noqa: E501
        :rtype: bool
        """
        return self._is_user_event

    @is_user_event.setter
    def is_user_event(self, is_user_event):
        """Sets the is_user_event of this RelatedEvent.

        Whether this event was created by a user, versus the system.  Default: system  # noqa: E501

        :param is_user_event: The is_user_event of this RelatedEvent.  # noqa: E501
        :type: bool
        """

        self._is_user_event = is_user_event

    @property
    def metrics_used(self):
        """Gets the metrics_used of this RelatedEvent.  # noqa: E501

        A list of metrics affected by the event  # noqa: E501

        :return: The metrics_used of this RelatedEvent.  # noqa: E501
        :rtype: list[str]
        """
        return self._metrics_used

    @metrics_used.setter
    def metrics_used(self, metrics_used):
        """Sets the metrics_used of this RelatedEvent.

        A list of metrics affected by the event  # noqa: E501

        :param metrics_used: The metrics_used of this RelatedEvent.  # noqa: E501
        :type: list[str]
        """

        self._metrics_used = metrics_used

    @property
    def name(self):
        """Gets the name of this RelatedEvent.  # noqa: E501

        The name of the event.  If 'annotations.prettyName' is present, 'name' will be equivalent to that value  # noqa: E501

        :return: The name of this RelatedEvent.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RelatedEvent.

        The name of the event.  If 'annotations.prettyName' is present, 'name' will be equivalent to that value  # noqa: E501

        :param name: The name of this RelatedEvent.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def related_data(self):
        """Gets the related_data of this RelatedEvent.  # noqa: E501

        Data concerning how this event is related to the event in the request  # noqa: E501

        :return: The related_data of this RelatedEvent.  # noqa: E501
        :rtype: RelatedData
        """
        return self._related_data

    @related_data.setter
    def related_data(self, related_data):
        """Sets the related_data of this RelatedEvent.

        Data concerning how this event is related to the event in the request  # noqa: E501

        :param related_data: The related_data of this RelatedEvent.  # noqa: E501
        :type: RelatedData
        """

        self._related_data = related_data

    @property
    def running_state(self):
        """Gets the running_state of this RelatedEvent.  # noqa: E501


        :return: The running_state of this RelatedEvent.  # noqa: E501
        :rtype: str
        """
        return self._running_state

    @running_state.setter
    def running_state(self, running_state):
        """Sets the running_state of this RelatedEvent.


        :param running_state: The running_state of this RelatedEvent.  # noqa: E501
        :type: str
        """
        allowed_values = ["ONGOING", "PENDING", "ENDED"]  # noqa: E501
        if (self._configuration.client_side_validation and
                running_state not in allowed_values):
            raise ValueError(
                "Invalid value for `running_state` ({0}), must be one of {1}"  # noqa: E501
                .format(running_state, allowed_values)
            )

        self._running_state = running_state

    @property
    def similarity_score(self):
        """Gets the similarity_score of this RelatedEvent.  # noqa: E501

        similarity score  # noqa: E501

        :return: The similarity_score of this RelatedEvent.  # noqa: E501
        :rtype: float
        """
        return self._similarity_score

    @similarity_score.setter
    def similarity_score(self, similarity_score):
        """Sets the similarity_score of this RelatedEvent.

        similarity score  # noqa: E501

        :param similarity_score: The similarity_score of this RelatedEvent.  # noqa: E501
        :type: float
        """

        self._similarity_score = similarity_score

    @property
    def start_time(self):
        """Gets the start_time of this RelatedEvent.  # noqa: E501

        Start time of the event, in epoch millis.  If the JSON value is missing or set to 0, startTime will be set to the current time  # noqa: E501

        :return: The start_time of this RelatedEvent.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this RelatedEvent.

        Start time of the event, in epoch millis.  If the JSON value is missing or set to 0, startTime will be set to the current time  # noqa: E501

        :param start_time: The start_time of this RelatedEvent.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and start_time is None:
            raise ValueError("Invalid value for `start_time`, must not be `None`")  # noqa: E501

        self._start_time = start_time

    @property
    def summarized_events(self):
        """Gets the summarized_events of this RelatedEvent.  # noqa: E501

        In some event queries, multiple events that occur nearly simultaneously are summarized under a single event.  This value specifies the number of events summarized under this one  # noqa: E501

        :return: The summarized_events of this RelatedEvent.  # noqa: E501
        :rtype: int
        """
        return self._summarized_events

    @summarized_events.setter
    def summarized_events(self, summarized_events):
        """Sets the summarized_events of this RelatedEvent.

        In some event queries, multiple events that occur nearly simultaneously are summarized under a single event.  This value specifies the number of events summarized under this one  # noqa: E501

        :param summarized_events: The summarized_events of this RelatedEvent.  # noqa: E501
        :type: int
        """

        self._summarized_events = summarized_events

    @property
    def table(self):
        """Gets the table of this RelatedEvent.  # noqa: E501

        The customer to which the event belongs  # noqa: E501

        :return: The table of this RelatedEvent.  # noqa: E501
        :rtype: str
        """
        return self._table

    @table.setter
    def table(self, table):
        """Sets the table of this RelatedEvent.

        The customer to which the event belongs  # noqa: E501

        :param table: The table of this RelatedEvent.  # noqa: E501
        :type: str
        """

        self._table = table

    @property
    def tags(self):
        """Gets the tags of this RelatedEvent.  # noqa: E501

        A list of event tags  # noqa: E501

        :return: The tags of this RelatedEvent.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this RelatedEvent.

        A list of event tags  # noqa: E501

        :param tags: The tags of this RelatedEvent.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def updated_at(self):
        """Gets the updated_at of this RelatedEvent.  # noqa: E501


        :return: The updated_at of this RelatedEvent.  # noqa: E501
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this RelatedEvent.


        :param updated_at: The updated_at of this RelatedEvent.  # noqa: E501
        :type: int
        """

        self._updated_at = updated_at

    @property
    def updated_epoch_millis(self):
        """Gets the updated_epoch_millis of this RelatedEvent.  # noqa: E501


        :return: The updated_epoch_millis of this RelatedEvent.  # noqa: E501
        :rtype: int
        """
        return self._updated_epoch_millis

    @updated_epoch_millis.setter
    def updated_epoch_millis(self, updated_epoch_millis):
        """Sets the updated_epoch_millis of this RelatedEvent.


        :param updated_epoch_millis: The updated_epoch_millis of this RelatedEvent.  # noqa: E501
        :type: int
        """

        self._updated_epoch_millis = updated_epoch_millis

    @property
    def updater_id(self):
        """Gets the updater_id of this RelatedEvent.  # noqa: E501


        :return: The updater_id of this RelatedEvent.  # noqa: E501
        :rtype: str
        """
        return self._updater_id

    @updater_id.setter
    def updater_id(self, updater_id):
        """Sets the updater_id of this RelatedEvent.


        :param updater_id: The updater_id of this RelatedEvent.  # noqa: E501
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
        if issubclass(RelatedEvent, dict):
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
        if not isinstance(other, RelatedEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RelatedEvent):
            return True

        return self.to_dict() != other.to_dict()
