THE CLI is built from field Q&A , and CLI way keeps the easy and simple consumption. 
Trying to avoid the module dependcy, i create this under python virtualenv and add
module search path to my env folder. 

Here is to introduce the example for example understanding 

# generate numbers of DFW rules for testing 
this is 2 dimensions idea to create the number of rules. 
If you want to create 250 rules, you can use command which is like 

python dfw.py gen -vsmip 192.168.0.96 -vsmuser admin -vsmpass password -mul 1 -base 250

the number of rules will be 1 x 250 under same section 

if you specify -mul 2 -base 250 in above clu, it creates 500 rules to dfw firewall 

# dump current dfw rules for human analysis 

python dfw.py qry -vsmip 192.168.0.96 -vsmuser admin -vsmpass password

# reset dfw rules to default 

python dfw.py reset -vsmip 192.168.0.96 -vsmuser admin -vsmpass password
