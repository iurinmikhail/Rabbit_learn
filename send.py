import pika


connection_parametrs = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parametrs)

channel = connection.channel()
channel.queue_declare(queue='letterbox')
message = 'Hello! This is my first message'
channel.basic_publish(exchange='',
                      routing_key='letterbox',
                      body=message)

print(" [x] Sent 'Hello World!'")
connection.close()