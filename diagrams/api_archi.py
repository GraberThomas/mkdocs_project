from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.queue import Kafka
from diagrams.onprem.network import Nginx
from diagrams.saas.cdn import Cloudflare
from diagrams.generic.network import Firewall
from diagrams.generic.storage import Storage
from diagrams.onprem.client import Users

with Diagram("FeastVerse System Architecture", show=False, direction="TB"):
    user = Users("End User")
    cdn = Cloudflare("CDN & Protection")
    lb = ELB("Load Balancer")
    firewall = Firewall("Security Layer")

    with Cluster("Railway Cloud Infrastructure"):
        with Cluster("Backend Services"):
            backend1 = EC2("API Server 1")
            backend2 = EC2("API Server 2")
            backend3 = EC2("API Server 3")
            queue = Kafka("Message Queue")
            cache = Redis("Cache Layer")
            storage = Storage("Object Storage")

            backend1 - queue
            backend2 - queue
            backend3 - queue
            backend1 - cache
            backend2 - cache
            backend3 - cache

        with Cluster("Database Layer"):
            db = PostgreSQL("PostgreSQL DB")
            backend1 - db
            backend2 - db
            backend3 - db

    user >> cdn >> lb >> firewall >> [backend1, backend2, backend3]
    firewall >> storage