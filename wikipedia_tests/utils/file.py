from pathlib import Path

import wikipedia_tests


def path(file) -> str:
    return str(Path(wikipedia_tests.__file__).parent.parent.joinpath(file))
