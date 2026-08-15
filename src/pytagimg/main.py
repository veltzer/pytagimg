"""
pytagimg.py
"""

import pylogconf.core
from pytconf import config_arg_parse_and_launch, register_endpoint, register_main

from pytagimg.static import APP_NAME, DESCRIPTION, VERSION_STR


@register_endpoint(
    description="run gui to tag images",
    configs=[
    ],
)
def run() -> None:
    pass


@register_main(
    main_description=DESCRIPTION,
    app_name=APP_NAME,
    version=VERSION_STR,
)
def main():
    pylogconf.core.setup()
    config_arg_parse_and_launch()


if __name__ == "__main__":
    main()
