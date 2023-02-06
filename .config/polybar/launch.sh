#!/usr/bin/env bash

# Check which profile is loaded
profile=$(autorandr --current)

host=$(hostname)

# Terminate already running bar instances
polybar-msg cmd quit

case $profile in
    full)
        case $host in
            xps)
                echo "---" | tee -a /tmp/polybar1.log /tmp/polybar2.log /tmp/polybar3.log
                MONITOR=DP-2-2 polybar primary 2>&1 | tee -a /tmp/polybar1.log & disown
                MONITOR=DP-1-2 polybar secondary 2>&1 | tee -a /tmp/polybar2.log & disown
                MONITOR=eDP-1 polybar secondary 2>&1 | tee -a /tmp/polybar3.log & disown
                ;;
            *)
                echo "---" | tee -a /tmp/polybar1.log /tmp/polybar2.log
                MONITOR=HDMI2 polybar primary 2>&1 | tee -a /tmp/polybar1.log & disown
                MONITOR=eDP1 polybar secondary 2>&1 | tee -a /tmp/polybar2.log & disown
                ;;
        esac
        ;;
    dual)
        case $host in
            xps)
                echo "---" | tee -a /tmp/polybar1.log /tmp/polybar2.log
                MONITOR=DP-2-2 polybar primary 2>&1 | tee -a /tmp/polybar1.log & disown
                MONITOR=DP-1-2 polybar secondary 2>&1 | tee -a /tmp/polybar2.log & disown
                ;;
            *)
                echo "---" | tee -a /tmp/polybar1.log /tmp/polybar2.log
                MONITOR=HDMI2 polybar primary 2>&1 | tee -a /tmp/polybar1.log & disown
                MONITOR=eDP1 polybar secondary 2>&1 | tee -a /tmp/polybar2.log & disown
                ;;
        esac
        ;;
    home)
        case $host in
            xps)
                echo "---" | tee -a /tmp/polybar1.log /tmp/polybar2.log
                MONITOR=DP-3 polybar primary 2>&1 | tee -a /tmp/polybar1.log & disown
                MONITOR=eDP-1 polybar secondary 2>&1 | tee -a /tmp/polybar2.log & disown
                ;;
            *)
                echo "---" | tee -a /tmp/polybar1.log /tmp/polybar2.log
                MONITOR=HDMI2 polybar primary 2>&1 | tee -a /tmp/polybar1.log & disown
                MONITOR=eDP1 polybar secondary 2>&1 | tee -a /tmp/polybar2.log & disown
                ;;
        esac
        ;;
    *)
        case $host in
            xps)
                echo "---" | tee -a /tmp/polybar1.log
                MONITOR=eDP-1 polybar primary 2>&1 | tee -a /tmp/polybar1.log & disown
                ;;
            *)
                echo "---" | tee -a /tmp/polybar1.log
                MONITOR=eDP1 polybar primary 2>&1 | tee -a /tmp/polybar1.log & disown
                ;;
        esac
        ;;
esac


echo "Bars launched..."
