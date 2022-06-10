
# Copyright 2020 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import logging
import random
from flask import Flask, request

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
logger = logging.getLogger(__name__)

app = Flask(__name__)
moves = ['F', 'T', 'L', 'R']

@app.route("/", methods=['GET'])
def index():
    return "Let the battle begin!"

@app.route("/", methods=['POST'])
def move():
    # request.get_data()
    data = request.json
    logger.info(data['arena']['state'])
    st = data['arena']['state']
    x = st['https://cloud-run-hackathon-python-q2rcemnqbq-uc.a.run.app']['x']
    y = st['https://cloud-run-hackathon-python-q2rcemnqbq-uc.a.run.app']['y']
    dir = st['https://cloud-run-hackathon-python-q2rcemnqbq-uc.a.run.app']['direction']

    bots = []
    st = data
    for i in st:
        bot=[]
        bot['x'] = int(st[i]['x'])
        bot['y'] = int(st[i]['y'])
        bot['dir'] = st[i]['direction']
        bots.append(bot)
        
    line = [i for i in bots if i['x']==x or i['y']==y]
    if dir == 'E':
        for i in line:
            if i['x'] - 3 <= x < i['x']:
                return 'T'
    elif dir == 'N':
        for i in line:
            if i['y'] + 3 >= y > i['y']:
                return 'T'
    elif dir == 'W':
        for i in line:
            if i['x'] + 3 >= x > i['x']:
                return 'T'
    elif dir == 'S':
        for i in line:
            if i['y'] - 3 <= y < i['y']:
                return 'T'

    return moves[random.randrange(len(moves))]

if __name__ == "__main__":
  app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
  
