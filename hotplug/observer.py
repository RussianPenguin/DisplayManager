from typing import Callable

import pyudev


def start_observer(callback=Callable):
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by('drm')

    def log_event(action, device):
        if device['DEVTYPE'] == 'drm_connector':
            callback()

    observer = pyudev.MonitorObserver(monitor, log_event)
    observer.start()
