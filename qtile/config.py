from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook
import subprocess
import os

import sys
from os.path import expanduser, exists, normpath, getctime
sys.path.append(expanduser('~/.config/qtile/src'))

#---------------------- Define programs ----------------------#
mod         = "mod4"                       # Sets mod key to SUPER/WINDOWS
alt         = "mod1"                       # Sets the alt key to left-alt key
myTerm      = "kitty"                    # My terminal of choice
myTerm2     = "alacritty"
#myTerm2     = "alacritty --config-file /home/pio/.config/iSettings/alacritty/alacritty.toml"
myBrowser   = "firefox"                   # My browser of choice
myEditor    = "kitty -e nvim"            # My editor of choice
myLauncher  = "rofi -show drun"            # My launcher of choice
#myLauncher  = "rofi -show drun -config ~/.config/iSettings/themes/nordico/rofi/launcher.rasi"
myExplorer  = "thunar"


#---------------------- Define useful functions ----------------------#

# Allows you to input a name when adding treetab section.
@lazy.layout.function
def add_treetab_section(layout):
    prompt = qtile.widgets_map["prompt"]
    prompt.start_input("Section name: ", layout.cmd_add_section)

# A function for hide/show all the windows in a group
@lazy.function
def minimize_all(qtile):
    for win in qtile.current_group.windows:
        if hasattr(win, "toggle_minimize"):
            win.toggle_minimize()

# A function for toggling between MAX and MONADTALL layouts
@lazy.function
def maximize_by_switching_layout(qtile):
    current_layout_name = qtile.current_group.layout.name
    if current_layout_name == 'monadtall':
        qtile.current_group.layout = 'max'
    elif current_layout_name == 'max':
        qtile.current_group.layout = 'monadtall'


keys = [
    # The essentials
    Key([mod], "Return", lazy.spawn(myTerm), desc="Terminal"),
    #Key([mod, "shift"], "Return", lazy.spawn("alacritty"), desc="Terminal"),
    Key([mod, "shift"], "Return", lazy.spawn(myTerm2), desc="Terminal"),
    Key([mod], "d", lazy.spawn(myLauncher), desc='Run Launcher'),
    Key([mod], "w", lazy.spawn(myBrowser), desc='Web browser'),
    Key([mod], "e", lazy.spawn(myExplorer), desc='Nautilus'),
    Key([mod], "b", lazy.hide_show_bar(position='all'), desc="Toggles the bar to show/hide"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([], "Print", lazy.spawn("/home/pio/.bin/maimshot"), desc="Screenshot menu"),
    #Key([mod, alt], "x", lazy.spawn("/home/pio/.bin/pmenu"), desc="Logout menu"),
    Key([mod, alt], "x", lazy.spawn("/home/pio/.config/iSettings/rofi/powermenu.sh"), desc="Logout menu"),
    
    # Window management
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h",
        lazy.layout.shuffle_left(),
        lazy.layout.move_left().when(layout=["treetab"]),
        desc="Move window to the left/move tab left in treetab"),

    Key([mod, "shift"], "l",
        lazy.layout.shuffle_right(),
        lazy.layout.move_right().when(layout=["treetab"]),
        desc="Move window to the right/move tab right in treetab"),

    Key([mod, "shift"], "j",
        lazy.layout.shuffle_down(),
        lazy.layout.section_down().when(layout=["treetab"]),
        desc="Move window down/move down a section in treetab"
    ),
    Key([mod, "shift"], "k",
        lazy.layout.shuffle_up(),
        lazy.layout.section_up().when(layout=["treetab"]),
        desc="Move window downup/move up a section in treetab"
    ),

    Key([mod, "shift"], "left",
        lazy.layout.shuffle_left(),
        lazy.layout.move_left().when(layout=["treetab"]),
        desc="Move window to the left/move tab left in treetab"),

    Key([mod, "shift"], "right",
        lazy.layout.shuffle_right(),
        lazy.layout.move_right().when(layout=["treetab"]),
        desc="Move window to the right/move tab right in treetab"),

    Key([mod, "shift"], "down",
        lazy.layout.shuffle_down(),
        lazy.layout.section_down().when(layout=["treetab"]),
        desc="Move window down/move down a section in treetab"
    ),
    Key([mod, "shift"], "up",
        lazy.layout.shuffle_up(),
        lazy.layout.section_up().when(layout=["treetab"]),
        desc="Move window downup/move up a section in treetab"
    ),


    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "space", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),

    # Grow/shrink windows left/right.
    # This is mainly for the 'monadtall' and 'monadwide' layouts
    # although it does also work in the 'bsp' and 'columns' layouts.
    Key([mod], "equal",
        lazy.layout.grow_left().when(layout=["bsp", "columns"]),
        lazy.layout.grow().when(layout=["monadtall", "monadwide"]),
        desc="Grow window to the left"
    ),
    Key([mod], "minus",
        lazy.layout.grow_right().when(layout=["bsp", "columns"]),
        lazy.layout.shrink().when(layout=["monadtall", "monadwide"]),
        desc="Grow window to the left"
    ),

    # Grow windows up, down, left, right.  Only works in certain layouts.
    # Works in 'bsp' and 'columns' layout.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.reset(), desc="Reset all window sizes"),
    Key([mod], "m", lazy.layout.maximize(), desc='Toggle between min and max sizes'),
    Key([mod], "t", lazy.window.toggle_floating(), desc='toggle floating'),
    Key([mod], "f", maximize_by_switching_layout(), lazy.window.toggle_fullscreen(), desc='toggle fullscreen'),
    Key([mod, "shift"], "m", minimize_all(), desc="Toggle hide/show all windows on current group"),

    # Switch focus of monitors
    # Key([mod], "period", lazy.next_screen(), desc='Move focus to next monitor'),
    # Key([mod], "comma", lazy.prev_screen(), desc='Move focus to prev monitor'),


    # Volume & brightness controls
    Key([], "XF86AudioRaiseVolume", lazy.spawn("volume up"), desc="Increase volume"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("volume down"), desc="Decrease volume"),
    Key([], "XF86AudioMute", lazy.spawn("volume mute"), desc="Toggle mute"),
    Key([], "XF86MonBrightnessUp", lazy.spawn("backlight up"), desc="Increase brightness"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("backlight down"), desc="Decrease brightness"),
]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group {i.name}",
            ),
            # mod + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc=f"Switch to & move focused window to group {i.name}",
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layout_theme = {
    "border_width": 0,
    "margin": 20,
}

layouts = [
     layout.MonadTall(**layout_theme),
     layout.Columns(**layout_theme),
     layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),    
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="JetBrainsMono Nerd Font Mono",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()


# helper func for statusbar
# def get_media_title_and_bar():
#     title = subprocess.getoutput("playerctl metadata --format '{{title}}'")
#     if title == "No players found":
#         return ""
#     if title == "No player could handle this command":
#         return ""

#     try:
#         position = float(subprocess.getoutput("playerctl position"))
#         length_str = subprocess.getoutput("playerctl metadata mpris:length")
#         length = int(length_str) / 1_000_000 if length_str.isdigit() else 0

#         if length == 0:
#             return title

#         percent = position / length
#         bar_length = 20
#         filled = int(percent * bar_length)
#         empty = bar_length - filled

#         bar = "■" * filled + "▯" * empty

#         return f"🎵 {title}"

#     except:
#         return title


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.TextBox(
                    text="",  # Arch Linux logo (Nerd Font)
                    font="JetBrainsMono Nerd Font",  # Must support Nerd Font glyphs
                    fontsize=18,
                    padding=20,
                ),
                widget.GroupBox(
                    active="#cdd6f4",
                    fontsize=20,
                    inactive="#6c7086",
                    highlight_method="block",
                    this_current_screen_border="#89b4fa",
                    other_screen_border="#585b70",
                    padding=5,
                    visible_groups=["1", "2", "3", "4", "5"],
                ),
                widget.Spacer(length=12),
                widget.Spacer(),
                # widget.GenPollText(
                #     update_interval=2,
                #     fontsize=15,
                #     foreground="#ffffff",
                #     func=get_media_title_and_bar,
                # ),
                widget.Spacer(),
                widget.Systray(),
                # widget.Battery(
                #     format="{char} {percent:2.0%}",
                #     # font="Noto Color Emoji",  # emoji-supporting font
                #     fontsize=18,
                #     charge_char="⚡",
                #     discharge_char="",
                #     empty_char="☠",
                #     full_char="✔",
                #     show_short_text=False,
                #     update_interval=30,
                #     # padding=10,
                # ),
                widget.Clock(
                    format="%a %H:%M",
                    fontsize=18,
                    padding=12,
                ),
                widget.TextBox(
                    text="⏻",
                    fontsize=20,
                    padding=10,
                    mouse_callbacks={
                        "Button1": lazy.spawn(
                            "/home/pio/.config/rofi/powermenu/launcher.sh"
                        )
                    },
                ),
                widget.Spacer(10),
            ],
            35,  # Bar Height
            background="#1a161c",
            margin=[10, 20, 0, 20],
            # background="#1a161c0",
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
