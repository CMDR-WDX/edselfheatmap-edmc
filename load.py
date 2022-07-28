import tkinter
import requests

_plugin_name = "eliteheatmap"

#
# WARNING!!!!
#
# Make sure this is the same Port as on the Heatmap Server

SERVER_PORT = 8000


def plugin_app(parent: tkinter.Frame) -> tkinter.Frame:
    return parent


def plugin_start3(_path: str) -> str:
    return _plugin_name


def journal_entry(_cmdr: str, _beta: bool, _system: str, _station: str, entry: dict[str, any], _state: dict):
    # Only cares about FSD Jumps
    if entry["event"] != "FSDJump":
        return

    sysname = entry["StarSystem"]
    [x, y, z] = entry["StarPos"]

    jsonData = dict([
        ("systemName", sysname),
        ("x", x),
        ("y", y),
        ("z", z),
    ])

    requests.post("http://localhost:"+str(SERVER_PORT), json=jsonData)
