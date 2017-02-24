# The script is prepared for rules generation of dfw of nsx-vsphere 
# It also can query current dfw configuration 
'''Usage:
    dfw.py gen -vsmip <nsxmgr_ip> -vsmuser <nsx_username> -vsmpass <nsx_password> -mul <multiple> -base <count>
    dfw.py qry -vsmip <nsxmgr_ip> -vsmuser <nsx_username> -vsmpass <nsx_password>
    dfw.py reset -vsmip <nsxmgr_ip> -vsmuser <nsx_username> -vsmpass <nsx_password>
'''

import sys
sys.path.insert(0,'./env/lib/python2.7/site-packages')

from docopt import docopt

if __name__ == '__main__':
    var = docopt(__doc__)

#print var

import requests,xml.dom.minidom
#requests.packages.urllib3.disable_warnings()

nsxmgr=var['<nsxmgr_ip>']
nsx_username=var['<nsx_username>']
nsx_password=var['<nsx_password>']

dfw_section="/api/4.0/firewall/globalroot-0/config/layer3sections"
dfw_conf="/api/4.0/firewall/globalroot-0/config"

def c_body(b,c):
    template=''
    template+="<section name = 'lab_rules'>"
    i=1
    j=1
    while i <= b:
	while j < c:
	    template+="""<rule disabled='false' logged='true'>
<name>test_%s</name>
<action>ALLOW</action>
<sources excluded='false'>
<source>
<value>1.1.%s.%s</value>
<type>Ipv4Address</type>
<isValid>true</isValid>
</source>
</sources>
<destinations excluded="false">
<destination>
<value>2.2.%s.%s</value>
<type>Ipv4Address</type>
<isValid>true</isValid>
</destination>
</destinations>
</rule>""" %(i,i,j,i,j)  
            j=j+1
        i=i+1
    template+="\n</section>"
    return template

def create_section():
    url="https://"+nsxmgr+dfw_section
    header={"Content-type":"application/xml"}
    conn=requests.post(url,verify=False,headers=header,auth=(nsx_username,nsx_password),data=body)
    resp=conn.text
    par=xml.dom.minidom.parseString(resp)
    result=par.toprettyxml()
    if conn.status_code == 201:
        print "The rules post is successful"
    else:
       print "the error code return is "+str(conn.status_code)
       print "the error message is "+resp

def q_rules():
    url="https://"+nsxmgr+dfw_conf
    conn=requests.get(url,verify=False,auth=(nsx_username,nsx_password))
    print conn.status_code
    resp=conn.text
    par=xml.dom.minidom.parseString(resp)
    result=par.toprettyxml()
    if conn.status_code == 201:
        print result
    else:
       print "the error code return is "+str(conn.status_code)
       print "the error message is "+resp

def reset_rules():
    url="https://"+nsxmgr+dfw_conf
    conn=requests.delete(url,verify=False,auth=(nsx_username,nsx_password))
    print conn.status_code
    resp=conn.text
    if conn.status_code == 204:
        print "The rules reset is successful"
    else:
       print "the error code return is "+str(conn.status_code)
       print "the error message is "+resp

if var['gen']==True:
    mul_b=int(var['<multiple>'])
    base_c=int(var['<count>'])
    body=c_body(mul_b,base_c)
    create_section()
elif var['qry']==True:
    q_rules()
elif var['reset']==True:
    reset_rules()
else:
    exit(1)
