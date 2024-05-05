#!/bin/bash
old_ps=$(ps -eo user,command); while true; do; new_ps=$(ps -eo user,command); diff <(echo "$old_ps") <(echo "$new_ps") | grep "[\>\<]" |grep -Ev "kworker|command"; old_ps=$new_ps; done

