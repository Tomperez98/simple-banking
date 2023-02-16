# Repository Coverage

[Full report](https://htmlpreview.github.io/?https://github.com/Tomperez98/simple-banking/blob/python-coverage-comment-action-data/htmlcov/index.html)

| Name                                                         |    Stmts |     Miss |   Branch |   BrPart |     Cover |   Missing |
|------------------------------------------------------------- | -------: | -------: | -------: | -------: | --------: | --------: |
| simple\_banking/\_\_init\_\_.py                              |        0 |        0 |        0 |        0 |    100.0% |           |
| simple\_banking/api/\_\_init\_\_.py                          |        0 |        0 |        0 |        0 |    100.0% |           |
| simple\_banking/api/\_\_main\_\_.py                          |        2 |        2 |        0 |        0 |      0.0% |       2-4 |
| simple\_banking/api/app.py                                   |       23 |       23 |        4 |        0 |      0.0% |      2-45 |
| simple\_banking/api/models/\_\_init\_\_.py                   |        0 |        0 |        0 |        0 |    100.0% |           |
| simple\_banking/api/models/register\_new\_client.py          |        8 |        8 |        0 |        0 |      0.0% |      2-14 |
| simple\_banking/cli/\_\_init\_\_.py                          |        1 |        1 |        0 |        0 |      0.0% |         1 |
| simple\_banking/cli/main.py                                  |       32 |       32 |        4 |        0 |      0.0% |      3-59 |
| simple\_banking/core/\_\_init\_\_.py                         |        0 |        0 |        0 |        0 |    100.0% |           |
| simple\_banking/core/exceptions.py                           |        3 |        1 |        0 |        0 |     66.7% |         9 |
| simple\_banking/core/models/\_\_init\_\_.py                  |        3 |        0 |        0 |        0 |    100.0% |           |
| simple\_banking/core/models/client.py                        |       11 |        0 |        2 |        0 |    100.0% |           |
| simple\_banking/core/models/loan.py                          |       11 |        0 |        2 |        0 |    100.0% |           |
| simple\_banking/core/services/\_\_init\_\_.py                |        0 |        0 |        0 |        0 |    100.0% |           |
| simple\_banking/core/services/email/\_\_init\_\_.py          |        3 |        0 |        0 |        0 |    100.0% |           |
| simple\_banking/core/services/email/api/\_\_init\_\_.py      |        2 |        0 |        0 |        0 |    100.0% |           |
| simple\_banking/core/services/email/api/base.py              |        4 |        0 |        0 |        0 |    100.0% |           |
| simple\_banking/core/services/email/api/fake/\_\_init\_\_.py |        2 |        0 |        0 |        0 |    100.0% |           |
| simple\_banking/core/services/email/api/fake/impl.py         |        6 |        0 |        0 |        0 |    100.0% |           |
| simple\_banking/core/services/email/client.py                |       14 |        2 |        0 |        0 |     85.7% |     25-26 |
| simple\_banking/core/use\_cases/\_\_init\_\_.py              |        2 |        0 |        0 |        0 |    100.0% |           |
| simple\_banking/core/use\_cases/register\_new\_client.py     |       42 |        2 |        6 |        2 |     91.7% |    81, 90 |
| simple\_banking/database/\_\_init\_\_.py                     |        3 |        0 |        0 |        0 |    100.0% |           |
| simple\_banking/database/base.py                             |       12 |        0 |        0 |        0 |    100.0% |           |
| simple\_banking/database/file\_system/\_\_init\_\_.py        |        0 |        0 |        0 |        0 |    100.0% |           |
| simple\_banking/database/file\_system/impl.py                |       37 |       23 |        4 |        0 |     34.1% |22-28, 34-36, 44-52, 56-78 |
| simple\_banking/database/in\_memory/\_\_init\_\_.py          |        0 |        0 |        0 |        0 |    100.0% |           |
| simple\_banking/database/in\_memory/impl.py                  |       18 |        0 |        0 |        0 |    100.0% |           |
|                                                    **TOTAL** |  **239** |   **94** |   **22** |    **2** | **58.6%** |           |


## Setup coverage badge

Below are examples of the badges you can use in your main branch `README` file.

### Direct image

[![Coverage badge](https://raw.githubusercontent.com/Tomperez98/simple-banking/python-coverage-comment-action-data/badge.svg)](https://htmlpreview.github.io/?https://github.com/Tomperez98/simple-banking/blob/python-coverage-comment-action-data/htmlcov/index.html)

This is the one to use if your repository is private or if you don't want to customize anything.

### [Shields.io](https://shields.io) Json Endpoint

[![Coverage badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/Tomperez98/simple-banking/python-coverage-comment-action-data/endpoint.json)](https://htmlpreview.github.io/?https://github.com/Tomperez98/simple-banking/blob/python-coverage-comment-action-data/htmlcov/index.html)

Using this one will allow you to [customize](https://shields.io/endpoint) the look of your badge.
It won't work with private repositories. It won't be refreshed more than once per five minutes.

### [Shields.io](https://shields.io) Dynamic Badge

[![Coverage badge](https://img.shields.io/badge/dynamic/json?color=brightgreen&label=coverage&query=%24.message&url=https%3A%2F%2Fraw.githubusercontent.com%2FTomperez98%2Fsimple-banking%2Fpython-coverage-comment-action-data%2Fendpoint.json)](https://htmlpreview.github.io/?https://github.com/Tomperez98/simple-banking/blob/python-coverage-comment-action-data/htmlcov/index.html)

This one will always be the same color. It won't work for private repos. I'm not even sure why we included it.

## What is that?

This branch is part of the
[python-coverage-comment-action](https://github.com/marketplace/actions/python-coverage-comment)
GitHub Action. All the files in this branch are automatically generated and may be
overwritten at any moment.