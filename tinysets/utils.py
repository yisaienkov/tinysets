"""Utils functions"""

from typing import Dict, List

__all__ = [
    'get_all_sets'
]


def get_all_sets() -> Dict[str, List[str]]:
    """
    Get all names of datasets and links to this sets

    Returns
    -------
    Dict[str, List[str]]
        Dictionary where the name of the dataset as the key and the list of
        links as the value where you can download this dataset
    """
    return {
        'LEGO Minifigures Classification': [
            "https://www.kaggle.com/ihelon/lego-minifigures-classification",
        ],
    }
