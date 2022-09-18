from Xlib import display as display_client
import pyedid
import hashlib


def enumerate():
    display = display_client.Display()
    root = display.screen().root
    resources = root.xrandr_get_screen_resources()._data

    outputs = {}
    for output in resources['outputs']:
        output_info = display.xrandr_get_output_info(
            output, resources['config_timestamp'])._data
        output_name = output_info['name']
        props = display.xrandr_list_output_properties(output)

        for atom in props._data['atoms']:
            atom_name = display.get_atom_name(atom)
            if atom_name == 'EDID':
                edid_raw = display.xrandr_get_output_property(
                    output, atom, 0, 0, 1000)._data['value']
                edid_hash = hashlib.md5(bytes(edid_raw)[128:])
                outputs[output_name] = str(edid_hash.hexdigest())
                break

    return outputs


if __name__ == '__main__':
    print(enumerate())
