#!/bin/bash

LOG_FILE=/home/dsi/vpn.log

CHECKER=/usr/bin/check_vpn.py

function run_checker() {
        $CHECKER 2>&1 >> $LOG_FILE &
}

run_checker
