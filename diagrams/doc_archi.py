from diagrams import Diagram, Cluster
from diagrams.onprem.client import Users
from diagrams.onprem.network import Nginx
from diagrams.onprem.container import Docker
from diagrams.saas.cdn import Cloudflare
from diagrams.generic.network import Firewall
from diagrams.onprem.compute import Server
from diagrams.onprem.ci import GithubActions

with Diagram("FeastVerse Documentation Architecture", show=False, direction="TB"):
    user = Users("End User")
    cdn = Cloudflare("CDN & Protection")
    firewall = Firewall("Security Layer")

    with Cluster("Railway Cloud Infrastructure"):
        with Cluster("Documentation Services"):
            nginx = Nginx("Nginx Web Server")
            mkdocs = Server("MkDocs Documentation")
            docker = Docker("Containerized Deployment")
            ci_cd = GithubActions("CI/CD Deployment")

            ci_cd >> docker >> nginx
            nginx >> mkdocs

    user >> cdn >> firewall >> nginx
