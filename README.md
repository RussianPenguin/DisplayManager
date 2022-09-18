Display hotplug management

Rearrange monitors by EDID, not output name. You can use same configuration for hdmi, dp and other types of connection.

Install service

1. Install modules ```pip install -r requirements.txt```

2. Edit display_hotplug.service and set correct path
3. Put display_hotplug.service to ~/.config/systemd/user/
4. Run ```systemctl --user enable --now display_hotplug```

Create config

1. ```python -m hotplug --create```
2. Edit file and place xrandr command using script args ```${0}```, ```${1}```, etc.
3. Enjoy

