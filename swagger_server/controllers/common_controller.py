import connexion
import six

from swagger_server.models.body import Body  # noqa: E501
from swagger_server.models.body1 import Body1  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server import util


def audio_post(body):  # noqa: E501
    """Upload user&#x27;s recorded audio

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body1.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def info_post(body):  # noqa: E501
    """Upload user&#x27;s basic information

    This API **must** be called before others. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def report_get():  # noqa: E501
    """Get a random report based on user&#x27;s information

     # noqa: E501


    :rtype: InlineResponse2001
    """
    return 'do some magic!'


def report_picture_get():  # noqa: E501
    """Get a picture of generated report

     # noqa: E501


    :rtype: InlineResponse2002
    """
    return 'do some magic!'


def text_get():  # noqa: E501
    """Get a random piece of text based on user&#x27;s information

     # noqa: E501


    :rtype: InlineResponse200
    """
    return 'do some magic!'
