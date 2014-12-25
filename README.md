JumpByLines
===========

A Sublime Text 3 Plugin to jump by a specified number of lines

Example keymap
```
    {
        "keys": ["ctrl+alt+down"],
        "command": "jump_by_lines",
        "args": {"direction": "forward", "by": 20}
    },

    {
        "keys": ["ctrl+alt+up"],
        "command": "jump_by_lines",
        "args": {"direction": "backward", "by": 20}
    },
```