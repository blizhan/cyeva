import numpy as np

LEV_FALSE_ALARM_RATE_CASE = {
    "1h": {
        1: [
            {"obs": [1.1, 5, 6, 0], "fct": [1.4, 10, 0, 0], "result": 0},
            {"obs": [1.1, 10, 6, 0], "fct": [1.4, 1.2, 0, 0], "result": 25},
            {"obs": [1.4, 10, 0, 0], "fct": [1.1, 1.2, 1.3, 0], "result": 50},
            {"obs": [1.4, 10, 0, 0], "fct": [1.1, 1.2, 1.3, 1], "result": 75},
            {"obs": [0, 10, 0, 0], "fct": [1.1, 1.2, 1.3, 1], "result": 100},
        ],
        2: [
            {"obs": [2.1, 1, 0, 0], "fct": [2.2, 0, 10, 0], "result": 0},
            {"obs": [2.1, 0, 0, 0], "fct": [2.2, 2.4, 10, 0], "result": 25},
            {"obs": [2.1, 0, 10, 0], "fct": [2.2, 2.4, 2.2, 0], "result": 50},
            {"obs": [2.2, 0, 10, 0], "fct": [2.1, 2.4, 2.2, 3], "result": 75},
            {"obs": [0, 0, 10, 0], "fct": [2.1, 2.4, 2.2, 3], "result": 100},
        ],
    }
}