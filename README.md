## BlockList.de   
  www.blocklist.de 

### Overview
www.blocklist.de is a free and voluntary service provided by a Fraud/Abuse-specialist, whose servers are often attacked via SSH-, Mail-Login-, FTP-, Webserver- and other services. 
The mission is to report any and all attacks to the respective abuse departments of the infected PCs/servers, to ensure that the responsible provider can inform 
their customer about the infection and disable the attacker. 
We report more than 70,000 attacks every 12 hours in real time using Whois (abuse-mailbox, abuse@, security@, email, remarks), the Ripe-Abuse-Finder and
the contact-database from abusix.org so we may find the abuse-address assigned to the offending host. 
Our reports are based on X-Arf (Network Abuse Reporting 2.0), so the abuse-department of the provider for the attacking host may parse our reports automatically. 

#### BlockList.de IP feed
This feed includes

  | Type        | Description  |
| ------------- |:-------------:|
| ssh      | All IP addresses which have been reported within the last 48 hours as having run attacks on the service SSH.  |
| mail      | All IP addresses which have been reported within the last 48 hours as having run attacks on the service Mail, Postfix.     |
| apache | All IP addresses which have been reported within the last 48 hours as having run attacks on the service Apache, Apache-DDOS, RFI-Attacks.       |
| imap | All IP addresses which have been reported within the last 48 hours for attacks on the Service imap, sasl, pop3.....       |
| ftp | All IP addresses which have been reported within the last 48 hours for attacks on the Service FTP.  |
| sip  | All IP addresses that tried to login in a SIP-, VOIP- or Asterisk-Server and are inclueded in the IPs-List from http://www.infiltrated.net/ (Twitter).  |
| bots | All IP addresses which have been reported within the last 48 hours as having run attacks attacks on the RFI-Attacks, REG-Bots, IRC-Bots or BadBots . |
| strongips | All IPs which are older then 2 month and have more then 5.000 attacks. |
| bruteforcelogin |  All IPs which attacks Joomlas, Wordpress and other Web-Logins with Brute-Force Logins |

### Using the BlockList.de feed API
 The BlockList.de feed API is found on github at

https://github.com/dnif/enrich-blocklistde

#### Getting started with BlockList.de feed API

1. #####    Login to your AD, A10 containers  
   ACCESS DNIF CONTAINER VIA SSH : [Click To Know How](https://dnif.it/docs/guides/tutorials/access-dnif-container-via-ssh.html)
2. #####    Move to the ‘/dnif/<Deployment-key/enrichment_plugins’ folder path.
```
$cd /dnif/CnxxxxxxxxxxxxV8/enrichment_plugins/
```
3. #####   Clone using the following command  
```  
git clone https://github.com/dnif/enrich-blocklistde.git blocklistde
```
### API feed output structure
  | Fields        | Description  |
| ------------- |:-------------:|
| EvtType      | An IP |
| EvtName      | The IOC      |
| IntelRef | Feed Name      |
| IntelRefURL | Feed URL      |
| ThreatType | DNIF Feed Identification Name |      

An example of API feed output
```
{'EvtType': 'IPv4', 
'EvtName': '108.62.60.117',
'AddFields': {
 'IntelRef': ['BLOCKLIST'],
'IntelRefURL': ['http://lists.blocklist.de/lists/all.txt'],
'ThreatType': ['blacklist']}}
```
