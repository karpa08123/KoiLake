import iwlib
import os
import subprocess
from libqtile import bar, layout, hook, extension, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen, KeyChord
from libqtile.lazy import lazy
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration, PowerLineDecoration, BorderDecoration

def power():
    qtile.cmd_spawn("sh -c ~/.config/rofi/scripts/powermenu_t2")


def init_topBar():
    return [
            Screen(
                top=bar.Bar([
                    widget.Spacer(
                                length=15,
                                background='282738'
                     ),

                    widget.Image(
                                filename='~/Images/koiIconInvert.png',
                                background='282738',
                                mouse_callbacks={"Button1":power},
                                margin=2
                    ),

                    widget.Image(
                                filename='~/.config/qtile/Assets/waveL.png',
                                background='282738',
                    ),

                    widget.Spacer(
                                length=-3
                    ),


                    widget.GroupBox(
                                borderwidth=3,
                                highlight_method='block',
                                active='#CAA9E0',
                                block_highlight_text_color="#91B1F0",
                                highlight_color='#4B427E',
                                inactive='#353446',
                                foreground='#ffffff',
                                background='#303446',
                                this_current_screen_border='#353446',
                                this_screen_border='#353446',
                                other_current_screen_border='#353446',
                                other_screen_border='#353446',
                                urgent_border='#353446',
                                rounded=True,
                                disable_drag=True
                    ),
                    
                    widget.Image(
                                filename='~/.config/qtile/Assets/slashL.png',
                                background='303446',
                    ),
                    
                    widget.Spacer(
                                length=-3
                    ),
                    widget.CurrentLayoutIcon(
                                background='303446'
                    ),

                    widget.Image(
                                filename='~/.config/qtile/Assets/circR.png',
                                background='303446',
                    ),
                    
                    widget.Spacer(
                                length=-3
                    ),


                    widget.WindowTabs(
                                background='282738'
                    ),

                    widget.Image(
                                filename='~/.config/qtile/Assets/circL.png',
                                background='282738',
                    ),
                    
                    widget.Spacer(
                                length=-3
                    ),
                    widget.KeyboardLayout(
                                configured_keyboards=['us','es'],
                                background='303446',
                                foreground='ffffff'
                    ),

                    widget.Systray(
                                background='303446'
                    ),

                    widget.Image(
                                filename='~/.config/qtile/Assets/slashR.png',
                                background='303446',
                    ),
                    
                    widget.Spacer(
                                length=-3
                    ),

                    widget.WiFiIcon(
                                interface='wlan0',
                                background='303446',
                                inactive_colour='303446',
                                active_colour='CAA9E0'
                    ),

                    widget.Wlan (
                                format='{essid}',
                                background='303446',
                    ),

                    widget.Spacer(
                                length=5,
                                background='303446'
                    ),

                    widget.BatteryIcon(
                                theme_path='~/.config/qtile/Assets/Battery/',
                                background='303446',
                                scale=1
                    ),

                    widget.Battery(
                                background='303446',
                                format='{percent:2.0%}',
                    ),

                    widget.Spacer(
                                length=6,
                                background='303446'
                    ),

                    widget.Volume(
                                background='303446',
                    ),

                    widget.Image(
                                filename='~/.config/qtile/Assets/waveR.png',
                                background='303446',
                    ),
                    
                    widget.Spacer(
                                length=-3
                    ),

                    widget.Clock(
                                format="󰃭 %d/%b - 󰥔 %H:%M",
                                background='282738',
                    ),

                    widget.Spacer(
                                length=6,
                                background='282738'
                    ),
                  ],
                
                24,
                border_color='#353446',
                border_width=[0,0,0,0],
                margin=[5,60,5,60],
            ),
        ),
    ]

screens = init_topBar()
