# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InlineResponse200(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, text: str=None):  # noqa: E501
        """InlineResponse200 - a model defined in Swagger

        :param text: The text of this InlineResponse200.  # noqa: E501
        :type text: str
        """
        self.swagger_types = {
            'text': str
        }

        self.attribute_map = {
            'text': 'text'
        }
        self._text = text

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse200':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200 of this InlineResponse200.  # noqa: E501
        :rtype: InlineResponse200
        """
        return util.deserialize_model(dikt, cls)

    @property
    def text(self) -> str:
        """Gets the text of this InlineResponse200.


        :return: The text of this InlineResponse200.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text: str):
        """Sets the text of this InlineResponse200.


        :param text: The text of this InlineResponse200.
        :type text: str
        """

        self._text = text
