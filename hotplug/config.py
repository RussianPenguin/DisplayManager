from . import enumerate
from xdg import xdg_config_home
from os import path
import pathlib
import subprocess

__CONFIG_DIR = path.join(xdg_config_home(), 'display_hotplug')


def get_config_with_args():
    displays = enumerate.enumerate()
    outputs = [(id, displays[id]) for id in displays]
    outputs.sort(key=lambda item: item[1])
    return (
        path.join(__CONFIG_DIR, '_'.join([item[1] for item in outputs])),
        [item[0] for item in outputs]
    )


def load():
    config_opts = get_config_with_args()
    if not path.exists(config_opts[0]):
        return
    print(f'Load {config_opts[0]}')
    try:
        subprocess.run(['/bin/bash', config_opts[0], *config_opts[1]])
    except Exception as exc:
        print(str(exc))


def create():
    pathlib.Path(__CONFIG_DIR).mkdir(parents=True, exist_ok=True)
    config_opts = get_config_with_args()
    with open(config_opts[0], 'w') as file:
        file.write(
            '#!/usr/bin/env bash\n'
            f'# {" ".join(config_opts[1])}\n'
            '# put xrandr string here.\n'
            '# xrandr \\\n'
            '#   --output ${1} --auto --primary \\\n'
            '#   --output ${2} --left-of ${1}\n'
            '\n'
        )
    return config_opts[0]
