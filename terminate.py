import boto3
import urllib2
import time

#Cancels spot request and terminates instance
ec2 = boto3.client('ec2')
instanceid = urllib2.urlopen('http://169.254.169.254/latest/meta-data/instance-id').read().decode()
desc_instance = ec2.describe_instances(InstanceIds=[instanceid])
spot_request_id= desc_instance['Reservations'][0]['Instances'][0]['SpotInstanceRequestId']
cancel_spot_request = ec2.cancel_spot_instance_requests(SpotInstanceRequestIds=[spot_request_id,])
terminate_instance = ec2.terminate_instances(InstanceIds=[instanceid,])




