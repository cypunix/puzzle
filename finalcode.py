from flask import Flask
from flask import render_template
from flask import request
from collections import defaultdict
import boto3
import botocore
import os

app = Flask(__name__, static_url_path='/temp', static_folder='temp')

#prime number function
def is_prime(num):
# prime numbers are greater than 1
	if num <= 1:
		return "prime numbers start from >=2, please correct the value"
	if num == 2:
		return "is not a prime number"
	if num > 1:
	   # check for factors
		for i in range(2,num):
			if (num % i) == 0:
				return "is not a prime number"
			else:
	       			return "is a prime number"

@app.route('/')
def startapp():
    return render_template('web_app.html')
	       
@app.route('/create', methods=['GET','POST'])

def create():
    if request.method == 'POST':
#assign variable
        ec2_number = int(request.form['ec2'])
        name = request.form['name']
               
#run the instances:

	client = boto3.client('ec2',region_name="ap-southeast-2")
#	instances = client.run_instances(
#            ImageId='ami-a18392c2', 
#            MinCount=ec2_number,
#            MaxCount=ec2_number,
#            InstanceType="t2.micro",
#            TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name','Value':name},{'Key':'uuid','Value':'666'}]} ]
#					)
#
	response = client.describe_instances(Filters=[{'Name':'tag-key', 'Values':[name]}]
	)
#fetch instances run by the webapp with the tag-key value 'Name' - I could've taken a less common name but...
	ec2 = boto3.resource('ec2', region_name="ap-southeast-2")
	running_instances = ec2.instances.filter(
            Filters=[{'Name': 'instance-state-name', 'Values': ['running']},{'Name':'tag-key', 'Values':['Name']},{'Name':'tag-value', 'Values':[name]}])
	ec2info = defaultdict()
	for instance in running_instances:
            for tag in instance.tags:
                if 'Name' in tag['Key']:
                    name = tag['Value']
	    # Add instance info to a dictionary         
	    ec2info[instance.id] = {
	        'ID': instance.instance_id,
	        'State': instance.state['Name'],
	        'Private IP': instance.private_ip_address,
	        'Public IP': instance.public_ip_address,
	        'Launch Time': instance.launch_time,
		'ImageId': instance.image_id
	        }
	
	    attributes = ['ID', 'Public IP', 'ImageId' ]
	    all_ec2=[]
	    for instance_id, instance in ec2info.items():
	        for key in attributes:
	            print("{0}: {1}".format(key, instance[key]))
		    all_ec2.append((key, instance[key]))
            all_ec2.append((ec2_number,is_prime(int(ec2_number))))
	    return render_template('running_instances.html',filename=all_ec2,group=name)

@app.route('/delete', methods=['GET','POST'])
def delete_click():
    
    if request.method == 'POST':
        group = request.form['group']
        ec2 = boto3.resource('ec2')
        running_instances = ec2.instances.filter(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']},{'Name':'tag-key', 'Values':[group]             }])

    	    # Add instance info to a dictionary         
	return render_template('delete.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
