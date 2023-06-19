from kafka import KafkaAdminClient
from kafka.admin import NewTopic
import time
import os


# # MongoDB sunucusuna bağlanmak için gerekli bilgileri girin
# mongo_host = '127.0.0.1'  # MongoDB sunucusunun adı veya IP adresi
# mongo_port = 27017  # MongoDB sunucusunun port numarası

# client = MongoClient(mongo_host, mongo_port, serverSelectionTimeoutMS=5000)
# db = client["mydatabase"]  # Veritabanı adınızı buraya girin
# # Diğer işlemlerinizi burada gerçekleştirin
# # Örneğin: db.your_collection_name.find_one() gibi sorgular yapabilirsiniz
# print("MongoDB bağlantısı başarılı.")


server = os.environ['KAFKA_BROKERCONNECT']

def create_topic():
    admin_client = KafkaAdminClient(bootstrap_servers=server)
    topic = NewTopic(name='X', num_partitions=1, replication_factor=3)
    admin_client.create_topics(new_topics=[topic])

create_topic()