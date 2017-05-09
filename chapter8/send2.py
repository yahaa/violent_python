import pika
import sys
cre = pika.PlainCredentials('zihua', 'password')
conn_params = pika.ConnectionParameters('ip', credentials=cre)
conn = pika.BlockingConnection(conn_params)
channel = conn.channel()
channel.exchange_declare(exchange='hello-world', type='direct',
                         passive=False, durable=True, auto_delete=False)
msg = sys.argv[1]
msg_props = pika.BasicProperties()
msg_props.content_type = 'text/plain'
channel.basic_publish(body=msg, exchange='hello-world',
                      properties=msg_props, routing_key='test1')
channel.close()
