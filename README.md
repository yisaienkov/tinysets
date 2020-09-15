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
  - [LEGO Minifigures Classification](#lego-minifigures-classification)
  - [Ukrainian Descriptions Of Words](#ukrainian-descriptions-of-words)


## How to use

You can see all available sets and their actual locations using the next code:

```
>>> from tinysets import get_all_sets
>>> get_all_sets()
{
    'LEGO Minifigures Classification': [
        'https://www.kaggle.com/ihelon/lego-minifigures-classification'
    ],
    'Ukrainian Descriptions Of Words': [
        'https://www.kaggle.com/ihelon/ukrainian-descriptions-of-words'
    ]
}
```

## Installation

### PyPI
You can use pip to install evaluations:
```
pip install tinysets
```
Or you can clone and install the latest version of the library from GitHub:
```
pip install -U git+https://github.com/yisaienkov/tinysets
```

## Datasets

### LEGO Minifigures Classification

![](https://i.imgur.com/4cPQlEN.jpg)

This dataset contains pictures of various LEGO Minifigures. There are several
images in different poses and with different environments for each Minifigure in
the dataset.

Currently, it contains 28 figures (more than 300 images totally) from the LEGO sets
[Yoda's Hut](https://www.lego.com/en-us/product/yoda-s-hut-75208),
[Spider Mech vs. Venom](https://www.lego.com/en-us/product/spider-mech-vs-venom-76115),
[General Grievous' Combat Speeder](https://www.lego.com/en-us/product/general-grievous-combat-speeder-75199),
[Kylo Ren's Shuttle™ Microfighter](https://www.lego.com/en-us/product/kylo-ren-s-shuttle-microfighter-75264),
[AT-ST™ Raider from The Mandalorian](https://www.lego.com/en-us/product/at-st-raider-75254),
[Molten Man Battle](https://www.lego.com/en-us/product/molten-man-battle-76128),
[Aragog's Lair](https://www.lego.com/en-us/product/aragog-s-lair-75950),
[Black Widow's Helicopter Chase](https://www.lego.com/en-us/product/black-widow-s-helicopter-chase-76162),
[Captain America: Outriders Attack](https://www.lego.com/en-us/product/captain-america-outriders-attack-76123),
[Pteranodon Chase](https://www.lego.com/en-us/product/pteranodon-chase-75926),
[Iron Man Hall of Armor](https://www.lego.com/en-us/product/iron-man-hall-of-armor-76125).

This dataset is available in [Kaggle Datasets](https://www.kaggle.com/ihelon/lego-minifigures-classification)

### Ukrainian Descriptions Of Words

![](https://i.imgur.com/UqXawPb.png)

This dataset contains descriptions of various words in simple terms by different
people. It looks like the Alias game when you need to describe the desired word
using other words so that the other player guesses your word.

Currently, it contains descriptions from 8 different people for 15 unique words.

This dataset is available in [Kaggle Datasets](https://www.kaggle.com/ihelon/ukrainian-descriptions-of-words)
