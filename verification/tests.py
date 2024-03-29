"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[
                    [1, 2, 10, 150],
                    [10, 2, 1000, 2],
                    [1, 120, 1, 1000]
                ]],
            "answer": '''\
[[ 1,   2,   10,  150],
 [10,   2, 1000,    2],
 [ 1, 120,    1, 1000]]''',
        },
        {
            "input": [[
                    [1, 10, 100, -1000]
                ]],
            "answer": "[[1, 10, 100, -1000]]",
        },
        {
            "input": [[
                    [1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1],
                ]],
            "answer": '''\
[[1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1]]''',
        },
        {
            "input": [[
                    [1, 1, -1, 1, 1],
                    [1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1]
                ]],
            "answer": '''\
[[1, 1, -1, 1, 1],
 [1, 1,  1, 1, 1],
 [1, 1,  1, 1, 1]]''',
        },
    ],
    "Extra": [
        {
            "input": [[
                    [1, 1, -1, 1, 1],
                    [1, 1, 1.3, 1, 1],
                    [1, 1, 1, 1, 1]
                ]],
            "answer": '''\
[[1, 1,  -1, 1, 1],
 [1, 1, 1.3, 1, 1],
 [1, 1,   1, 1, 1]]''',
        },
        {
            "input": [[
                    [1, 10, 100, 1000],
                    [10, 100, 1000, 100],
                    [100, 1000, 100, 10],
                    [1000, 100, 10, 1]
                ]],
            "answer": '''\
[[   1,   10,  100, 1000],
 [  10,  100, 1000,  100],
 [ 100, 1000,  100,   10],
 [1000,  100,   10,    1]]''',
        },
        {
            "input": [[
                    [1, -10, 100, 1000],
                    [10.1, 100, -1000, 1000],
                    [100, 1000, 100, 1000],
                    [1000, 100, 10.1, -1000]
                ]],
            "answer": '''\
[[   1,  -10,   100,  1000],
 [10.1,  100, -1000,  1000],
 [ 100, 1000,   100,  1000],
 [1000,  100,  10.1, -1000]]''',
        },
    ]
}
