"""
All configurations for pytagimg
"""


from pytconf import Config, ParamCreator


class ConfigRemoveFolders(Config):
    """
    Parameters for the remove folder tool
    """
    filenames = ParamCreator.create_str(
    )
