import boto3


def create_table(dynamodb=None):
    table = dynamodb.create_table(
        TableName='Cars',
        KeySchema=[
            {
                'AttributeName': 'year',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'name',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'year',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'name',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    return table


def insert_data(table):
    cars = [
            {
                "year": 1998,
                "name": "GF-CP9A",
                "info": {"maker": "三菱自動車", "release_date": "1998-01-26T00:00:00Z"}
            },
            {
                "year": 2007,
                "name": "WRX STI",
                "info": {"maker": "SUBARU", "release_date": "2007-10-24T00:00:00Z"}
            }
    ]

    with table.batch_writer() as batch:
        for car in cars:
            batch.put_item(Item=car)
            print(f'Adding car: {car["year"]}, {car["name"]}')


if __name__ == '__main__':
    dynamodb = boto3.resource(
        service_name='dynamodb', 
        endpoint_url='http://dynamodb-local:8000',
        aws_access_key_id='',
        aws_secret_access_key='',
        region_name='')

    car_table = create_table(dynamodb)
    print(f'Table status: {car_table.table_status}')
    insert_data(car_table)
