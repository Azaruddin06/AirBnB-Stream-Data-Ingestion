import json
import boto3
import random
from datetime import datetime, timedelta

sqs_client = boto3.client('sqs')
QUEUE_URL = 'https://sqs.us-east-1.amazonaws.com/381492087220/AirbnbBookingQueue' 



def generate_airbnbData():
    # Generate Random values
    booking_id = f"booking_id_{random.randint(1, 1000000)}"
    user_id = f"user_{random.randint(100, 1000)}"
    property_id = f"property_{random.randint(100, 1000)}"
    price = round(random.uniform(50, 500), 2)
    city = ["New York", "London", "Paris", "Tokyo", "Sydney", "Bangalore"]
    country = ["USA", "UK", "France", "Japan", "Australia","India"]
    location = f"{random.choice(city)}, {random.choice(country)}"

    # Generate random dates
    base_date = datetime(2024, 3, 1)  
    max_offset = (datetime.today() - base_date).days  
    random_offset = random.randint(0, max_offset)
    start_date = (base_date + timedelta(days=random_offset)).strftime('%Y-%m-%d')
    days_rand = random.randint(1, 10)
    stay_duration = random.randint(1, days_rand)
    end_date = (datetime.strptime(start_date, '%Y-%m-%d') + timedelta(days=stay_duration)).strftime('%Y-%m-%d')
    price =round(random.uniform(50, 500), 2)
    return {
    "bookingId": booking_id,
    "userId": user_id,
    "propertyId": property_id,
    "location": location,
    "startDate": start_date,
    "endDate": end_date,
    "price":  f"{price} USD"
    }


def lambda_handler(event, context):
    i=0
    while(i<10):
        sales_order = generate_airbnbData()
        print(sales_order)
        sqs_client.send_message(
            QueueUrl=QUEUE_URL,
            MessageBody=json.dumps(sales_order)
        )
        i += 1
    
    return {
        'statusCode': 200,
        'body': json.dumps('Airbnb Booking data published to SQS!')
    }

