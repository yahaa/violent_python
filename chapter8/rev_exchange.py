import pika

conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = conn.channel()
channel.exchange_declare(exchange='logs', type='fanout')

res = channel.queue_declare(exclusive=True)
qu_name = res.method.queue
channel.queue_bind(exchange='logs', queue=qu_name)
print '[*] Waiting for logs. To exit press CTR'


def callback(ch, method, property, body):
    print '[x] %r' % (body)


channel.basic_consume(callback, queue=qu_name, no_ack=True)
channel.start_consuming()
