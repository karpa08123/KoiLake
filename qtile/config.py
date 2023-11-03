############################# IMPORTS ########################################
import os
import subprocess
from libqtile import bar, layout, hook, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen, KeyChord
from libqtile.lazy import lazy
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration, PowerLineDecoration

from modules.bar import *
##############################################################################

mod = "mod4"
terminal = "kitty"

################################## KEYS ######################################
# A list of available commands that can be bound to keys can be found
# at https://docs.qtile.org/en/latest/manual/config/lazy.html

#def TScreen():
#    qtile.cmd_spawn("sh -c ~/.config/rofi/scripts/monitor_layout.sh")

keys = [
    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "control"], "Up", lazy.layout.grow(), desc="Grow window"),
    Key([mod, "control"], "Down", lazy.layout.shrink(), desc="Shrink windoww"),

    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "Tab", lazy.prev_layout(), desc="Toggle between layouts in reverse"),

    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),

    Key([mod, "control"], 'q', lazy.run_extension(extension.CommandSet(
    commands={
        'shutdown': 'shutdown -P now',
        'Reboot': 'shutdown -r now',
        'LockScreen': 'i3lock -i Imágenes/Wallpapers/Unmodified/animeLighthouse.png',
        })), desc="Power option"),

   # Key([mod], "p", lazy.spawn(), desc="Change monitor layout"), #This one doesn't work
    
    #Volume control
    Key((), "XF86AudioRaiseVolume", lazy.spawn("pamixer -i 2")),
    Key((), "XF86AudioLowerVolume", lazy.spawn("pamixer -d 2")),
    Key((), "XF86AudioMute", lazy.spawn("pamixer -t")),

    #Brightness control
    Key((), "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key((), "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),

    #Print Screen
    Key((), "Print", lazy.spawn('scrot -s -f "%d-%m-%y_%H:%M:%S.png" -e "mv $f ~/Images/Screenshots"')),

    #Mic mute
    Key((), "XF86AudioMicMute", lazy.spawn("pamixer -t")), #this command is bad setted

    Key([mod], "r", lazy.spawn("rofi -show drun"), desc="Run apps"),

    KeyChord([mod], "z", [
        Key([], "f", lazy.spawn("rofi -show filebrowser"), desc="Spawn rofi in file mode"),
        Key([], "c", lazy.spawn("rofi -show calc"), desc="Spawn rofi in calculator mode")
    ]),
    
    #Lockscreen
    Key([mod], "l", lazy.spawn("i3lock -i Images/punkgirl.png"), desc="Lockscreen"),

    #change keyboard layout
    Key([mod], "space", lazy.widget["keyboardlayout"].next_keyboard(), desc="Change keyboard layout."),
    
    #Apps
    Key([mod], "e", lazy.spawn("nemo"), desc="File explorer"),

    #dmenu
    Key([mod], 'm', lazy.run_extension(extension.CommandSet(
    commands={
        'Bluetooth': 'dmenu-bluetooth prompt',
        'Wifi On': 'nmcli radio wifi on',
        'Wifi Off': 'nmcli radio wifi off'
        })))

]

############################### GROUPS #######################################
groups = []

groups_names = ["1","2","3","4","5"]

#group_labels = [">_", "@", "CHAT", "FILES", "EXTRA"]
#group_labels = ["1", "2", "3", "4", "5"]
#group_labels = ["󰘦 ", "󰖟 ", "󰚢 ", " ", " "]
group_labels = ["󰏃", "󰏃", "󰏃", "󰏃", "󰏃"]


group_layouts = ["MonadTall", "MonadTall", "MonadTall", "MonadTall", "MonadTall"]

for i in range(len(groups_names)):
    groups.append(
        Group(
            name=groups_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))

for i in groups:
    keys.extend([
            # mod1 + letter of group = switch to group
            Key([mod], i.name, lazy.group[i.name].toscreen(), desc="Switch to group {}".format(i.name),),

            # mod1 + shift + letter of group = switch to & move focused window to group
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=False), desc="Move focused window to group {}".format(i.name),),

        ]
    )

############################# LAYOUTS ########################################
layout_theme={
    'border_width':0,
    'margin':10,
}

layouts = [
    layout.MonadTall(name='MonadTall', **layout_theme),
    layout.Max(name='Max'),
    layout.Floating(name='Floating', **layout_theme),
]

widget_defaults = dict(
    font="JetBrains Mono Nerd Font",
    fontsize=12,
    padding=3,
    opacity=0.0)

extension_defaults = widget_defaults.copy()


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.disable_floating()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
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

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = 'Qtile'
