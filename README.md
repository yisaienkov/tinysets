# TinySets
[![PyPI version](https://badge.fury.io/py/tinysets.svg)](https://badge.fury.io/py/tinysets)

- This project contains different datasets.
- The main purpose of these sets is to quickly check the performance of
  models and algorithms.


## Table of contents
- [How to use](#how-to-use)
- [Installation](#installation)
  - [PyPI](#pypi)
- [Datasets](#datasets)
  - [LEGO Minifigures Classification](#LEGOMinifiguresClassification)


## How to use

You can see all available sets using next code:

```
>>> from tinysets import get_all_sets
>>> get_all_sets()
{'LEGO Minifigures Classification': ['https://www.kaggle.com/ihelon/lego-minifigures-classification']}'
```

## Installation

### PyPI
You can use pip to install evaluations:
```
pip install tinysets
```
You can clone and install the latest version of the library from GitHub:
```
pip install -U git+https://github.com/yisaienkov/tinysets
```

## Datasets

### LEGO Minifigures Classification

![](https://i.imgur.com/4cPQlEN.jpg)

This dataset contains pictures of various LEGO Minifigures. There are several
images in different poses and with different environments for each Minifigure in
the dataset.

Currently it contains 7 figures from the LEGO sets
[Yoda's Hut](https://www.lego.com/en-us/product/yoda-s-hut-75208),
[Spider Mech vs. Venom](https://www.lego.com/en-us/product/spider-mech-vs-venom-76115).

This dataset is available in [Kaggle Datasets](https://www.kaggle.com/ihelon/lego-minifigures-classification)
