# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.body import Body  # noqa: E501
from swagger_server.models.body1 import Body1  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCommonController(BaseTestCase):
    """CommonController integration test stubs"""

    def test_audio_post(self):
        """Test case for audio_post

        Upload user's recorded audio
        """
        body = Body1()
        response = self.client.open(
            '/BBT-Tech-S/To-Love-Camgirl/1.0.3/audio',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_info_post(self):
        """Test case for info_post

        Upload user's basic information
        """
        body = Body()
        response = self.client.open(
            '/BBT-Tech-S/To-Love-Camgirl/1.0.3/info',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_report_get(self):
        """Test case for report_get

        Get a random report based on user's information
        """
        response = self.client.open(
            '/BBT-Tech-S/To-Love-Camgirl/1.0.3/report',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_report_picture_get(self):
        """Test case for report_picture_get

        Get a picture of generated report
        """
        response = self.client.open(
            '/BBT-Tech-S/To-Love-Camgirl/1.0.3/report/picture',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_text_get(self):
        """Test case for text_get

        Get a random piece of text based on user's information
        """
        response = self.client.open(
            '/BBT-Tech-S/To-Love-Camgirl/1.0.3/text',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
