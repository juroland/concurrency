#!/bin/bash
trace-cmd record -e 'sched_wakeup*' -e sched_switch -e 'sched_migrate*' -c -F $PYTHON_BIN_PATH multithread_fib.py
