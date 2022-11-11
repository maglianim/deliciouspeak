#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------
'''
Main file
'''
import os
from flask import Flask
from api import api_blueprint

app = Flask(__name__)

app.register_blueprint(api_blueprint, url_prefix="/api")

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
