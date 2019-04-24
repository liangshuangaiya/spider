#!/usr/bin/python3

import json


if __name__ == '__main__':
    data = "[{a: 1, b: 2, c: 3, d: 4, e: 5}]"
    dataJ = json.dumps(data)
    print(dataJ)
    dataD = json.loads(dataJ)
    print(dataD)
