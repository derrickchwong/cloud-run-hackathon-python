
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
from fastapi import Request, FastAPI

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
logger = logging.getLogger(__name__)

app = FastAPI()
moves = ['F', 'L', 'R']

@app.get("/")
def index():
    return "Let the battle begin!"

@app.post('/')
def move(request: Request):
    # request.get_data()
    print(request)
    print(request.json())
    return moves[random.randrange(len(moves))]
    st = data['arena']['state']
    my = st['https://cloud-run-hackathon-python-ujmnd5v4va-uc.a.run.app']
    x = my['x']
    y = my['y']
    dir = my['direction']
    wasHit = my['wasHit']
    logger.info(my)

    line = [{'x': st[i]['x'], 'y': st[i]['y'], 'direction': st[i]['direction'],} for i in st if st[i]['x'] == x or st[i]['y'] == y]

    if wasHit:
        return moves[random.randrange(len(moves))]
    elif dir == 'E':
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
