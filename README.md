# Repository Coverage



| Name                                                         |    Stmts |     Miss |   Branch |   BrPart |     Cover |   Missing |
|------------------------------------------------------------- | -------: | -------: | -------: | -------: | --------: | --------: |
| simple\_banking/\_\_init\_\_.py                              |        0 |        0 |        0 |        0 |    100.0% |           |
| simple\_banking/cli/\_\_init\_\_.py                          |        1 |        1 |        0 |        0 |      0.0% |         1 |
| simple\_banking/cli/main.py                                  |       30 |       30 |        4 |        0 |      0.0% |      3-56 |
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
| simple\_banking/core/use\_cases/register\_new\_client.py     |       42 |        9 |        6 |        2 |     72.9% |48-56, 82, 91 |
| simple\_banking/database/\_\_init\_\_.py                     |        3 |        0 |        0 |        0 |    100.0% |           |
| simple\_banking/database/base.py                             |       12 |        0 |        0 |        0 |    100.0% |           |
| simple\_banking/database/file\_system/\_\_init\_\_.py        |        0 |        0 |        0 |        0 |    100.0% |           |
| simple\_banking/database/file\_system/impl.py                |       41 |       27 |        6 |        0 |     29.8% |22-28, 34-36, 45-58, 62-84 |
| simple\_banking/database/in\_memory/\_\_init\_\_.py          |        0 |        0 |        0 |        0 |    100.0% |           |
| simple\_banking/database/in\_memory/impl.py                  |       22 |        3 |        2 |        1 |     83.3% |     44-46 |
|                                                    **TOTAL** |  **212** |   **73** |   **22** |    **3** | **62.4%** |           |


## Setup coverage badge

Below are examples of the badges you can use in your main branch `README` file.

### Direct image

[![Coverage badge](https://github.com/Tomperez98/simple-banking/raw/python-coverage-comment-action-data/badge.svg)](https://github.com/Tomperez98/simple-banking/tree/python-coverage-comment-action-data)

This is the one to use if your repository is private or if you don't want to customize anything.



## What is that?

This branch is part of the
[python-coverage-comment-action](https://github.com/marketplace/actions/python-coverage-comment)
GitHub Action. All the files in this branch are automatically generated and may be
overwritten at any moment.