import boto3
import urllib2

ec2 = boto3.client('ec2')
volume_response = ec2.create_volume(Size=10, AvailabilityZone='us-east-1a', VolumeType='gp2');
instanceid = urllib2.urlopen('http://169.254.169.254/latest/meta-data/instance-id').read().decode()

attach_volume_response = ec2.attach_volume(VolumeId=volume_response['VolumeId'],InstanceId=instanceid,Device='/dev/xvdh')

# lsblk
# sudo mkfs -t ext4 /dev/xvdh
# sudo mkdir mounting_point
# sudo mount /dev/xvdh mounting_point/
# cd mounting_point
# sudo chmod go+rw .

