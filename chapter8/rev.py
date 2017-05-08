import pika
conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = conn.channel()
channel.queue_declare(queue='helloworld')


def callback(ch, method, properties, body):
    print '[x] Received %s' % body


channel.basic_consume(callback, queue='helloworld', no_ack=True)
channel.start_consuming()
