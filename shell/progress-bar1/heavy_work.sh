#!/bin/bash

source progress_bar.sh

tasks_in_total=10
for current_task in $(seq $tasks_in_total) 
    do
    sleep 0.2 #simulate the task running
    mkdir teste    
    show_progress $current_task $tasks_in_total
done
# while [ $tasks_in_total > 0 ]
#     do
#     $tasks_in_total - 1
#     source teste.sh
#     show_progress $current_task $tasks_in_total
# done