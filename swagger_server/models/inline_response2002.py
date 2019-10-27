# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InlineResponse2002(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, image: str=None):  # noqa: E501
        """InlineResponse2002 - a model defined in Swagger

        :param image: The image of this InlineResponse2002.  # noqa: E501
        :type image: str
        """
        self.swagger_types = {
            'image': str
        }

        self.attribute_map = {
            'image': 'image'
        }
        self._image = image

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2002':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_2 of this InlineResponse2002.  # noqa: E501
        :rtype: InlineResponse2002
        """
        return util.deserialize_model(dikt, cls)

    @property
    def image(self) -> str:
        """Gets the image of this InlineResponse2002.


        :return: The image of this InlineResponse2002.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image: str):
        """Sets the image of this InlineResponse2002.


        :param image: The image of this InlineResponse2002.
        :type image: str
        """

        self._image = image
