# vpn_restart
This is a tiny python script to check the vpn status and restart it if needed(see full desciption below)

This is a tiny python3 script to check for an established VPN connection. 
If it matches it then sleeps for 60 seconds and checks again, if it does not match 
it should initiate a VPN restart command on the server then re-enter the loop all over again.
The script is a while loop set to True so it should check indefinitely.

There is also a second shell script to run once in the shell that will execute the python script into the background.
