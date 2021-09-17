"""
The default group of operations that pytagimg has
"""

import os  # for walk, getcwd, symlink, listdir, unlink, mkdir
import os.path  # for join, expanduser, realpath, abspath, islink, isdir, isfile

import pylogconf.core
from pytconf import register_endpoint, get_free_args, register_main, config_arg_parse_and_launch

from pytagimg.configs import ConfigSymlinkInstall, ConfigRemoveFolders
from pytagimg.static import APP_NAME, VERSION_STR


def debug(msg):
    """debug function for the symlink install operation"""
    if ConfigSymlinkInstall.debug:
        print(msg)


def do_install(source, target):
    """install a single item"""
    if ConfigSymlinkInstall.force:
        if os.path.islink(target):
            os.unlink(target)
    if ConfigSymlinkInstall.doit:
        debug(f"symlinking [{source}], [{target}]")
        os.symlink(source, target)


def file_gen(root_folder: str, recurse: bool):
    """generate all files in a folder"""
    if recurse:
        for root, directories, files in os.walk(root_folder):
            yield root, directories, files
    else:
        directories = []
        files = []
        for file in os.listdir(root_folder):
            full = os.path.join(root_folder, file)
            if os.path.isdir(full):
                directories.append(file)
            if os.path.isfile(full):
                files.append(file)
        yield root_folder, directories, files


@register_endpoint(
    description="Install symlinks to things in a folder",
    configs=[
        ConfigSymlinkInstall,
    ],
)
def symlink_install() -> None:
    cwd = os.getcwd()
    if os.path.isdir(ConfigSymlinkInstall.target_folder):
        for file in os.listdir(ConfigSymlinkInstall.target_folder):
            full = os.path.join(ConfigSymlinkInstall.target_folder, file)
            if os.path.islink(full):
                link_target = os.path.realpath(full)
                if link_target.startswith(cwd):
                    if ConfigSymlinkInstall.doit:
                        debug(f"unlinking [{full}]")
                        os.unlink(full)
    else:
        os.mkdir(ConfigSymlinkInstall.target_folder)
    for root, directories, files in file_gen(ConfigSymlinkInstall.source_folder, ConfigSymlinkInstall.recurse):
        for file in files:
            source = os.path.abspath(os.path.join(root, file))
            target = os.path.join(ConfigSymlinkInstall.target_folder, file)
            do_install(source, target)
        for directory in directories:
            source = os.path.abspath(os.path.join(root, directory))
            target = os.path.join(ConfigSymlinkInstall.target_folder, directory)
            do_install(source, target)


@register_endpoint(
    description="Remove folders",
    configs=[
        ConfigRemoveFolders,
    ],
)
def remove_folders() -> None:
    result = []
    for f in get_free_args():
        r = os.path.splitext(os.sep.join(f.split(os.sep)[1:]))[0]
        result.append(r)
    print(' '.join(result), end='')


@register_main(
    main_description="pytagimg will help you tag images",
    app_name=APP_NAME,
    version=VERSION_STR,
)
def main():
    pylogconf.core.setup()
    config_arg_parse_and_launch()


if __name__ == '__main__':
    main()
