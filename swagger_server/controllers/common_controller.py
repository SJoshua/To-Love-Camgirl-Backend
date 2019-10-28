import connexion
import random
import base64
import flask
import six

from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

from swagger_server.models.body import Body  # noqa: E501
from swagger_server.models.body1 import Body1  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server import util
from swagger_server import data


def audio_post(body):  # noqa: E501
    """Upload user's recorded audio

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    gender = flask.session.get("gender")
    if gender not in ["male", "female", "unknown"]:
        return '', 401

    if connexion.request.is_json:
        body = Body1.from_dict(connexion.request.get_json())  # noqa: E501
        if body.id:
            flask.session["id"] = random.randint(0, len(data.report_list[gender]) - 1)
            return '', 200
    
    return '', 405


def info_post(body):  # noqa: E501
    """Upload user's basic information

    This API **must** be called before others. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body.from_dict(connexion.request.get_json())  # noqa: E501
        if not body.name or body.gender not in ["male", "female", "unknown"]:
            return '', 405
        flask.session["name"] = body.name
        flask.session["gender"] = body.gender
        return '', 200
    else:
        return '', 405


def report_get():  # noqa: E501
    """Get a random report based on user's information

     # noqa: E501


    :rtype: InlineResponse2001
    """
    name = flask.session.get("name")
    gender = flask.session.get("gender")
    id = flask.session.get("id")
    if not name or not id or not (0 <= id < len(data.report_list[gender])) or gender not in ["male", "female", "unknown"]:
        return '', 401
    raw = data.report_list[gender][id]
    return {
        "name": name,
        "property": raw[0],
        "score": raw[1],
        "description": raw[2],
        "content": raw[3],
        "url": data.base_url + raw[4]
    }, 200

def report_picture_get():  # noqa: E501
    """Get a picture of generated report

     # noqa: E501


    :rtype: InlineResponse2002
    """

    name = flask.session.get("name")
    gender = flask.session.get("gender")
    id = flask.session.get("id")
    if not name or gender not in ["male", "female", "unknown"] or not id or not (0 <= id < len(data.report_list[gender])):
        return '', 401
    raw = data.report_list[gender][id]
    
    img = "./template.jpg"
    font = "./font.ttf"
    color = "#7d9998"
    heart = Image.open("heart.png")

    image = Image.open(img)
    draw = ImageDraw.Draw(image)
    width = image.size[0]
    font_1 = ImageFont.truetype(font, 32)
    font_2 = ImageFont.truetype(font, 28)

    text_width = font_1.getsize(name)[0]
    draw.text(((width - text_width) / 2, 414), name, color, font_1)
    draw.text((300, 566), raw[0], color, font_1)
    image.paste(heart, (300, 644), mask = heart)
    for i in range(1, raw[1]):
        image.paste(heart, (300 + 50 * i, 644), mask = heart)
    draw.text((300, 715), raw[2], color, font_1)
    (text_2, text_3) = raw[3].split("\n")
    text_width = font_2.getsize(text_2)[0]
    draw.text(((width - text_width) / 2, 829), text_2, color, font_2)
    text_width = font_2.getsize(text_3)[0]
    draw.text((650 - text_width, 884), text_3, color, font_2)

    image.save("output.png", "png")

    img_buffer = BytesIO()
    image.save(img_buffer, format='PNG')
    byte_data = img_buffer.getvalue()
    return {
        "image": "data:image/png;base64," + base64.b64encode(byte_data)
    }, 200

def text_get():  # noqa: E501
    """Get a random piece of text based on user's information

     # noqa: E501


    :rtype: InlineResponse200
    """
    gender = flask.session.get("gender")
    if gender not in ["male", "female", "unknown"]:
        return '', 401
    return data.text_list[random.randint(0, len(data.text_list) - 1)], 200
