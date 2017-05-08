import pika
conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = conn.channel()
channel.queue_declare(queue='helloworld')
channel.basic_publish(exchange='', routing_key='helloworld',
                      body='I\'m your farther hahaha')
print '[x] Sent helloworld to queue'
conn.close()
