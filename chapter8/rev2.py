import pika
cre = pika.PlainCredentials('zihua', 'password')
conn_params = pika.ConnectionParameters('ip', credentials=cre)
conn = pika.BlockingConnection(conn_params)
channel = conn.channel()
channel.exchange_declare(exchange='hello-world', type='direct',
                         passive=False, durable=True, auto_delete=False)

channel.queue_declare(queue='hello-queue')
channel.queue_bind(queue='hello-queue',
                   exchange='hello-world', routing_key='test1')


def msg_consumer(ch, method, header, body):
    ch.basic_ack(delivery_tag=method.delivery_tag)
    if body == 'quit':
        ch.basic_cancel(consumer_tag='hello')
        ch.stop_consuming()
    else:
        print body
    return


channel.basic_consume(msg_consumer, queue='hello-queue',
                      consumer_tag='hello')
channel.start_consuming()
