import pika
import sys

conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = conn.channel()
channel.queue_declare(queue='task_queue', durable=True)
msg = ''.join(sys.argv[1:]) or 'hello world'
channel.basic_publish(exchange='', routing_key='task_queue', body=msg,
                      properties=pika.BasicProperties(delivery_mode=2,))

print '[x] Sent %r' % (msg,)
conn.close()
