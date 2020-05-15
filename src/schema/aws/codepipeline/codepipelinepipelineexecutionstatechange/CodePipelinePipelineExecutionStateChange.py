# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum
from schema.aws.codepipeline.codepipelinepipelineexecutionstatechange.CodePipelinePipelineExecutionStateChange_executiontrigger import CodePipelinePipelineExecutionStateChange_executiontrigger  # noqa: F401,E501

class CodePipelinePipelineExecutionStateChange(object):


    _types = {
        'pipeline': 'str',
        'execution_id': 'str',
        'state': 'str',
        'version': 'str',
        'execution_trigger': 'CodePipelinePipelineExecutionStateChange_executiontrigger'
    }

    _attribute_map = {
        'pipeline': 'pipeline',
        'execution_id': 'execution-id',
        'state': 'state',
        'version': 'version',
        'execution_trigger': 'execution-trigger'
    }

    def __init__(self, pipeline=None, execution_id=None, state=None, version=None, execution_trigger=None):  # noqa: E501
        self._pipeline = None
        self._execution_id = None
        self._state = None
        self._version = None
        self._execution_trigger = None
        self.discriminator = None
        self.pipeline = pipeline
        self.execution_id = execution_id
        self.state = state
        self.version = version
        self.execution_trigger = execution_trigger


    @property
    def pipeline(self):

        return self._pipeline

    @pipeline.setter
    def pipeline(self, pipeline):


        self._pipeline = pipeline


    @property
    def execution_id(self):

        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):


        self._execution_id = execution_id


    @property
    def state(self):

        return self._state

    @state.setter
    def state(self, state):


        self._state = state


    @property
    def version(self):

        return self._version

    @version.setter
    def version(self, version):


        self._version = version


    @property
    def execution_trigger(self):

        return self._execution_trigger

    @execution_trigger.setter
    def execution_trigger(self, execution_trigger):


        self._execution_trigger = execution_trigger

    def to_dict(self):
        result = {}

        for attr, _ in six.iteritems(self._types):
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
        if issubclass(CodePipelinePipelineExecutionStateChange, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, CodePipelinePipelineExecutionStateChange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

