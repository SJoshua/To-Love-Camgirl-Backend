# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InlineResponse2001(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, name: str=None, _property: str=None, score: int=None, description: str=None, content: str=None, url: str=None):  # noqa: E501
        """InlineResponse2001 - a model defined in Swagger

        :param name: The name of this InlineResponse2001.  # noqa: E501
        :type name: str
        :param _property: The _property of this InlineResponse2001.  # noqa: E501
        :type _property: str
        :param score: The score of this InlineResponse2001.  # noqa: E501
        :type score: int
        :param description: The description of this InlineResponse2001.  # noqa: E501
        :type description: str
        :param content: The content of this InlineResponse2001.  # noqa: E501
        :type content: str
        :param url: The url of this InlineResponse2001.  # noqa: E501
        :type url: str
        """
        self.swagger_types = {
            'name': str,
            '_property': str,
            'score': int,
            'description': str,
            'content': str,
            'url': str
        }

        self.attribute_map = {
            'name': 'name',
            '_property': 'property',
            'score': 'score',
            'description': 'description',
            'content': 'content',
            'url': 'url'
        }
        self._name = name
        self.__property = _property
        self._score = score
        self._description = description
        self._content = content
        self._url = url

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2001':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_1 of this InlineResponse2001.  # noqa: E501
        :rtype: InlineResponse2001
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this InlineResponse2001.


        :return: The name of this InlineResponse2001.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this InlineResponse2001.


        :param name: The name of this InlineResponse2001.
        :type name: str
        """

        self._name = name

    @property
    def _property(self) -> str:
        """Gets the _property of this InlineResponse2001.


        :return: The _property of this InlineResponse2001.
        :rtype: str
        """
        return self.__property

    @_property.setter
    def _property(self, _property: str):
        """Sets the _property of this InlineResponse2001.


        :param _property: The _property of this InlineResponse2001.
        :type _property: str
        """

        self.__property = _property

    @property
    def score(self) -> int:
        """Gets the score of this InlineResponse2001.


        :return: The score of this InlineResponse2001.
        :rtype: int
        """
        return self._score

    @score.setter
    def score(self, score: int):
        """Sets the score of this InlineResponse2001.


        :param score: The score of this InlineResponse2001.
        :type score: int
        """

        self._score = score

    @property
    def description(self) -> str:
        """Gets the description of this InlineResponse2001.


        :return: The description of this InlineResponse2001.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this InlineResponse2001.


        :param description: The description of this InlineResponse2001.
        :type description: str
        """

        self._description = description

    @property
    def content(self) -> str:
        """Gets the content of this InlineResponse2001.


        :return: The content of this InlineResponse2001.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content: str):
        """Sets the content of this InlineResponse2001.


        :param content: The content of this InlineResponse2001.
        :type content: str
        """

        self._content = content

    @property
    def url(self) -> str:
        """Gets the url of this InlineResponse2001.


        :return: The url of this InlineResponse2001.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url: str):
        """Sets the url of this InlineResponse2001.


        :param url: The url of this InlineResponse2001.
        :type url: str
        """

        self._url = url
