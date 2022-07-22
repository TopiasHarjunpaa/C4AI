# C4AI

Description to be added.


![GitHub Actions](https://github.com/TopiasHarjunpaa/C4AI/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/TopiasHarjunpaa/C4AI/branch/main/graph/badge.svg?token=56BPEV86O7)](https://codecov.io/gh/TopiasHarjunpaa/C4AI)


## Releases

To be added.

## Documentation

- [Project definition document](https://github.com/TopiasHarjunpaa/C4AI/blob/main/documentation/definitions.md)
- [Project implementation document](https://github.com/TopiasHarjunpaa/C4AI/blob/main/documentation/implementation.md)
- [Testing document](https://github.com/TopiasHarjunpaa/C4AI/blob/main/documentation/testing.md)
- [User instructions](https://github.com/TopiasHarjunpaa/C4AI/blob/main/documentation/instructions.md)

## Reports and hours

- [Week 1](https://github.com/TopiasHarjunpaa/C4AI/blob/main/documentation/weekly_report_1.md)
- [Week 2 (placeholder)](https://github.com/TopiasHarjunpaa/C4AI/blob/main/documentation/weekly_report_2.md)
- [Week 3 (placeholder)](https://github.com/TopiasHarjunpaa/C4AI/blob/main/documentation/weekly_report_3.md)
- [Week 4 (placeholder)](https://github.com/TopiasHarjunpaa/C4AI/blob/main/documentation/weekly_report_4.md)
- [Week 5 (placeholder)](https://github.com/TopiasHarjunpaa/C4AI/blob/main/documentation/weekly_report_5.md)
- [Week 6 (placeholder)](https://github.com/TopiasHarjunpaa/C4AI/blob/main/documentation/weekly_report_6.md)
- [Hours](https://github.com/TopiasHarjunpaa/C4AI/blob/main/documentation/hours.md)

## Assembly instructions

Start by cloning the repository:

```
$ git clone git@github.com:TopiasHarjunpaa/C4AI.git
$ cd C4AI
```

Install dependencies

```
$ poetry install
```

Start the program using the command:

```
$ poetry run invoke start
```

## Other commands

#### Testing:

Tests can be executed using the command:

```
poetry run invoke test
```

Coverage report can be generated using the command:

```
poetry run invoke coverage-report
```

Report will be generated into the folder named `htmlcov`. Coverage report can be also found from [Codecov (placeholder)]()


#### Pylint:

Style checks can be executed using the command:

```
poetry run invoke lint
```