from libqtile import bar
from .widgets import *
from libqtile.config import Screen
from modules.keys import terminal
import os

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(padding=3, linewidth=0, background="#2f343f"),
                widget.Image(
                    filename="~/.config/qtile/eos-c.png",
                    margin=3,
                    background="#2f343f",
                    mouse_callbacks={
                        "Button1": lambda: qtile.cmd_spawn("rofi -show combi")
                    },
                ),
                widget.Sep(padding=4, linewidth=0, background="#2f343f"),
                widget.GroupBox(
                    highlight_method="block",
                    this_screen_border="#5294e2",
                    this_current_screen_border="#5294e2",
                    active="#ffffff",
                    inactive="#848e96",
                    background="#2f343f",
                    fontsize=14,
                ),
                widget.TextBox(text="", padding=0, fontsize=34, foreground="#2f343f"),
                widget.Prompt(),
                widget.Spacer(length=5),
                widget.WindowName(foreground="#99c0de", fmt="{}", fontsize=16),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.CheckUpdates(
                    update_interval=1800,
                    distro="Arch_yay",
                    display_format="{updates} Updates",
                    foreground="#ffffff",
                    mouse_callbacks={
                        "Button1": lambda: qtile.cmd_spawn(terminal + " -e yay -Syu")
                    },
                    background="#2f343f",
                ),
                widget.Systray(icon_size=20),
                widget.Spacer(length=5),
                widget.TextBox(text="", padding=0, fontsize=34, foreground="#2f343f"),
                MyVolume(
                    fontsize=22,
                    font='Font Awesome 5 Free',
                    foreground=colors[4],
                    background='#2f343f',
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("pavucontrol")}
                ),
                widget.Volume(
                  background="#2f343f", update_interval=0.1
                ),
                widget.Spacer(length=6, background="#2f343f"),
                widget.Battery(
                    foreground="#00a9ff",
                    background="#2f343f",
                    fontsize=14,
                    format="{char} {percent:2.0%} {hour:02d}:{min:02d}h",
                    charge_char="↑",
                    discharge_char="↓",
                    update_interval=30,
                ),
                # widget.TextBox(
                #     text="",
                #     padding=0,
                #     fontsize=34,
                #     foreground="#2f343f",
                #     background="#2f343f",
                # ),
                # widget.TextBox(text="", padding=0, fontsize=34, foreground="#2f343f"),
                widget.Spacer(length=6, background="#2f343f"),
                widget.Clock(
                    format="%Y-%m-%d %a %H:%M %p",
                    background="#2f343f",
                    foreground="#9bd689",
                    fontsize=14,
                ),
                widget.TextBox(
                    text="",
                    padding=0,
                    fontsize=34,
                    foreground="#404552",
                    background="#2f343f",
                ),
                widget.TextBox(
                    text="",
                    mouse_callbacks={
                        "Button1": lambda: qtile.cmd_spawn(
                            os.path.expanduser("~/.config/rofi/powermenu.sh")
                        )
                    },
                    foreground="#e39378",
                    fontsize=16,
                ),
                widget.Spacer(length=8),
            ],
            36,  # height in px
            background="#404552",  # background color
            margin=[8, 8, 0, 8],
        ),

        wallpaper='~/.config/qtile/wallpapers/mountains.jpg',
        wallpaper_mode='fill'
    ),
]
