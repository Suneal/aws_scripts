import boto3
import urllib2
import time

ec2 = boto3.client('ec2')

ip_address= str(urllib2.urlopen('http://ip.42.pl/raw').read())

instanceid = urllib2.urlopen('http://' + ip_address + '/latest/meta-data/instance-id').read().decode()
region = urllib2.urlopen('http://' + ip_address + '/latest/meta-data/placement/availability-zone/').read().decode()
string_region = region.encode('utf-8')
volume_response = ec2.create_volume(Size=10, AvailabilityZone=string_region, VolumeType='gp2');

time.sleep(30) # Giving time for volume to be available
attach_volume_response = ec2.attach_volume(VolumeId=volume_response['VolumeId'],InstanceId=instanceid,Device='/dev/xvdh')

# lsblk
# sudo mkfs -t ext4 /dev/xvdh
# sudo mkdir mounting_point
# sudo mount /dev/xvdh mounting_point/
# cd mounting_point
# sudo chmod go+rw .


