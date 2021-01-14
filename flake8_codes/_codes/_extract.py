# built-in
from typing import Dict
from importlib import import_module

from ._default import extract_default
from ._registry import registry


ALIASES = {
    'flake8_bugbear': 'bugbear',
    'flake8_logging_format': 'logging_format',
}


def _register_all():
    import_module('._adhoc', package=__package__)
    import_module('._default', package=__package__)
    import_module('._hardcoded', package=__package__)
    import_module('._renamed', package=__package__)


_register_all()


def extract(name) -> Dict[str, str]:
    name = name.replace('-', '_')
    name = ALIASES.get(name, name)

    # use ad-hoc extractor if available
    extractor = registry.get(name=name)
    if extractor is not None:
        return extractor()

    # try to extract by default algorithm
    return extract_default(name)
