import boto3

# 22 Febuary 2024 - Copy the tags to an attached EBS volume from the EC2 instance


ec2 = boto3.resource(service_name='ec2')

for volume in ec2.volumes.filter(Filters=[{'Name': 'status', 'Values': ['in-use']}]):             # Attached  EBS volumes
    #print(volume.id)
    for attachment in volume.attachments:
        for insttag in ec2.Instance(attachment['InstanceId']).tags:         
            tagneeded=True
            if volume.tags:                                         
                for voltag in volume.tags:                               
                    if insttag['Key'] == voltag['Key']:
                        if insttag['Value'] == voltag['Value']:      # The Volume has both Key and Value
                            tagneeded=False
            if tagneeded:                      
                #DryRun=True
                #if not DryRun:
                volume.create_tags(Tags=[{'Key':insttag['Key'], 'Value':insttag['Value']}])     # Copy the Tag Key and Value from the EC2 Instance to the EBS volume
            else:
                print(volume.id,"Does not need tag",insttag['Key']  )     # No action required
    
