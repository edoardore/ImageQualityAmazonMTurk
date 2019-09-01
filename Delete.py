import boto3
from datetime import datetime

# Get the MTurk client
mturk = boto3.client('mturk',
                     aws_access_key_id="",
                     aws_secret_access_key="",
                     region_name='us-east-1',
                     endpoint_url="https://mturk-requester-sandbox.us-east-1.amazonaws.com",
                     )

# Delete HITs
for item in mturk.list_hits()['HITs']:
    hit_id = item['HITId']
    print('HITId:', hit_id)

    # Get HIT status
    status = mturk.get_hit(HITId=hit_id)['HIT']['HITStatus']
    print('HITStatus:', status)

    # If HIT is active then set it to expire immediately
    if status == 'Assignable':
        response = mturk.update_expiration_for_hit(
            HITId=hit_id,
            ExpireAt=datetime(2015, 1, 1)
        )

        # Delete the HIT
    try:
        mturk.delete_hit(HITId=hit_id)
    except:
        print('Not deleted')
    else:
        print('Deleted')
