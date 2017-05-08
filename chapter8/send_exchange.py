import pika
import sys
conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = conn.channel()
channel.exchange_declare(exchange='logs', type='fanout')
msg = ''.join(sys.argv[1:]) or 'info : hello world'
channel.basic_publish(exchange='logs', routing_key='', body=msg)
print '[x] Sent %r' % (msg,)
conn.close()
