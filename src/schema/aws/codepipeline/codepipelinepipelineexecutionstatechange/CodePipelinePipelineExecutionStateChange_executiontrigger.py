# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum


class CodePipelinePipelineExecutionStateChange_executiontrigger(object):
    _types = {"trigger_type": "str", "trigger_detail": "str"}

    _attribute_map = {
        "trigger_type": "trigger-type",
        "trigger_detail": "trigger-detail",
    }

    def __init__(self, trigger_type=None, trigger_detail=None):  # noqa: E501
        self._trigger_type = None
        self._trigger_detail = None
        self.discriminator = None
        self.trigger_type = trigger_type
        self.trigger_detail = trigger_detail

    @property
    def trigger_type(self):

        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):

        self._trigger_type = trigger_type

    @property
    def trigger_detail(self):

        return self._trigger_detail

    @trigger_detail.setter
    def trigger_detail(self, trigger_detail):

        self._trigger_detail = trigger_detail

    def to_dict(self):
        result = {}

        for attr, _ in six.iteritems(self._types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(CodePipelinePipelineExecutionStateChange_executiontrigger, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(
            other, CodePipelinePipelineExecutionStateChange_executiontrigger
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
