#!/usr/bin/env python3

import connexion
import logging

from swagger_server import encoder

def main():
    logging.basicConfig(filename='log.log',level=logging.INFO)
    logging.info("Server started.")
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.app.secret_key = "super_secret_key"
    app.add_api('swagger.yaml', arguments={'title': 'To Love Webcasts'}, pythonic_params=True)
    app.run(port=8080)


if __name__ == '__main__':
    main()
