visualize_algorithms
====================

visualize algorithms,use django rest + d3 + algorithms


algorithms
---

Base on [algorithms](https://github.com/nryoung/algorithms), trans them
to yield vitual, so we can check very step.

Api
---

GET /api/v1/:algorithms_name

DATA
    type: json
    params:
        seq: [1,2,3,8,2]

RETURN
    type: json
        steps:[
            [],
            [],
            [],
            ...
        ]

### GET /api/v1/bubble_sort
