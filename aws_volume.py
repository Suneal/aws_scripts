import boto3
import urllib2
import time
import commands
ec2 = boto3.client('ec2')

ip_address= str(urllib2.urlopen('http://ip.42.pl/raw').read())

#This didn't work for amazon instance
# instanceid = urllib2.urlopen('http://' + ip_address + '/latest/meta-data/instance-id').read().decode()

#For Amazon Linux
instanceid = commands.getstatusoutput('ec2-metadata --instance-id | cut -d " " -f 2')[1]
region = commands.getstatusoutput('ec2-metadata --availability-zone | cut -d " " -f 2')[1]


#region = urllib2.urlopen('http://' + ip_address + '/latest/meta-data/placement/availability-zone/').read().decode()
string_region = region.encode('utf-8')
volume_response = ec2.create_volume(Size=10, AvailabilityZone=string_region, VolumeType='gp2');

time.sleep(10) # Giving time for volume to be available
attach_volume_response = ec2.attach_volume(VolumeId=volume_response['VolumeId'],InstanceId=instanceid,Device='/dev/xvdh')
time.sleep(5)
# lsblk
# sudo mkfs -t ext4 /dev/xvdh
# sudo mkdir mounting_point
# sudo mount /dev/xvdh mounting_point/
# cd mounting_point
# sudo chmod go+rw .


