#!/usr/bin/env bash
# Current Theme
dir="$HOME/.config/rofi/powermenu/"
theme='config'

# CMDs
uptime="$(uptime -p | sed 's/up //')"
host="$(hostname)"

# Options (ícones)
shutdown=''
reboot=''
lock=''
suspend=''
logout=''

# Rofi CMD
rofi_cmd() {
    rofi -dmenu \
        -p "Goodbye $USER" \
        -mesg "Uptime: $uptime" \
        -theme "${dir}/${theme}.rasi"
}

# Pass variables to rofi dmenu
run_rofi() {
    echo -e "$lock\n$suspend\n$logout\n$reboot\n$shutdown" | rofi_cmd
}

# Execute selected action immediately (sem confirmação)
execute_action() {
    case $1 in
        "$shutdown")
            systemctl poweroff
            ;;
        "$reboot")
            systemctl reboot
            ;;
        "$suspend")
            # Opcional: pausar música e mutar som antes de suspender
            mpc -q pause 2>/dev/null
            amixer set Master mute 2>/dev/null
            systemctl suspend
            ;;
        "$logout")
            case "$DESKTOP_SESSION" in
                openbox)
                    openbox --exit
                    ;;
                bspwm)
                    bspc quit
                    ;;
                i3)
                    i3-msg exit
                    ;;
                plasma)
                    qdbus org.kde.ksmserver /KSMServer logout 0 0 0
                    ;;
                qtile)
                    qtile cmd-obj -o cmd -f shutdown
                    ;;
                *)
                    # Fallback caso não reconheça a sessão
                    echo "Sessão desconhecida: $DESKTOP_SESSION" >&2
                    exit 1
                    ;;
            esac
            ;;
        "$lock")
            if [[ -x '/usr/bin/betterlockscreen' ]]; then
                betterlockscreen -l
            elif [[ -x '/usr/bin/i3lock' ]]; then
                i3lock -c 000000
            else
                # Último recurso bem básico
                xset s activate
            fi
            ;;
        *)
            # Caso estranho (não deveria acontecer)
            exit 1
            ;;
    esac
}

# ===============================================
# Programa principal
# ===============================================

chosen="$(run_rofi)"

# Se o usuário cancelou (ESC ou clicou fora)
[[ -z "$chosen" ]] && exit 0

execute_action "$chosen"
