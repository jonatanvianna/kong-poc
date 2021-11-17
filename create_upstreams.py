import ipdb
import requests
from pprint import pprint


def upstreams_create(upstream_name):
    data = {
        "name": f"{upstream_name}",
    }
    response = requests.post(
        url=f"{admin_host}/upstreams",
        json=data
    )
    pprint("Create Upstream")
    pprint(response.json())
    return response.json().get("id")


def upstreams_update(upstream_name):
    data = {
        # "id": "58c8ccbb-eafb-4566-991f-2ed4f678fa70",
        # "created_at": 1422386534,
        # "name": f"{upstream_name}",
        # "algorithm": "round-robin",
        # "hash_on": "none",
        # "hash_fallback": "none",
        # "hash_on_header": "??",
        # "hash_fallback_header": "none",
        # "hash_on_cookie": "",
        # "hash_on_cookie_path": "/",
        # "slots": 10000,
        "healthchecks": {
            "active": {
                "https_verify_certificate": True,
                # "unhealthy": {
                #     "http_statuses": [429, 404, 500, 501, 502, 503, 504, 505],
                #     "tcp_failures": 0,
                #     "timeouts": 0,
                #     "http_failures": 0,
                #     "interval": 0
                # },
                "http_path": "/rte",
                "timeout": 1,
                "healthy": {
                    "http_statuses": [200, 302, 201],
                    "interval": 5,
                    "successes": 2
                },
                "https_sni": "example.com",
                "concurrency": 10,
                "type": "http"
            },
            "passive": {
                "unhealthy": {
                    "http_failures": 3,
                    "http_statuses": [429, 500, 503],
                    "tcp_failures": 0,
                    "timeouts": 0
                },
                "type": "http",
                "healthy": {
                    "successes": 0,
                    "http_statuses": [200, 201, 202, 203, 204, 205, 206, 207, 208, 226, 300, 301, 302, 303, 304, 305, 306, 307, 308]
                }
            },
            "threshold": 0
        },
        # "tags": ["user-level", "low-priority"],
        # "host_header": "example.com",
        # "client_certificate": {"id":"ea29aaa3-3b2d-488c-b90c-56df8e0dd8c6"}
    }
    response = requests.patch(
        url=f"{admin_host}/upstreams/{upstream_name}",
        json=data
    )
    pprint("Update Upstream")
    pprint(response.json())
    return response.json().get("id")


def upstreams_list():
    pprint(requests.get(f"{admin_host}/upstreams").json())


def upstreams_delete(upstream_name):
    pprint(requests.delete(url=f"{admin_host}/upstreams/{upstream_name}"))


def services_create(service_name, url="", host=""):
    # 1 add a service
    data = {
        # "url": url,
        "host": host,
        "name": service_name
    }
    response = requests.post(
        url=f"{admin_host}/services",
        json=data
    )
    pprint("Create Service")
    pprint(response.json())

    # curl -i -X POST http://0.0.0.0:8001/services \
    #   --data name=example_service \
    #   --data  \
    #   --data host='0.0.0.0' \
    #   --data port='9091'
    #   --data url='http://mockbin.org'

    # curl -i -X POST http://0.0.0.0:8001/services \
    #   --data name=example_service2 \
    #   --data url='http://0.0.0.0:9090' \
    #   --data host='0.0.0.0' \
    #   --data port='9090'


def services_list(service_name):
    pprint(requests.get(url=f"{admin_host}/services").json())


def services_delete(service_name):
    pprint(requests.delete(url=f"{admin_host}/services/{service_name}"))


def routes_create(service_name, route_name, paths):
    data = {
        "protocols": ["http"],
        "methods": ["GET"],
        "paths": paths,
        "name": route_name,
        # "hosts": ["api.com"]
    }
    response = requests.post(
        url=f"{admin_host}/services/{service_name}/routes",
        json=data
    )
    pprint("Create Route")
    pprint(response.json())


    # 2 add a route to the service
    # curl -i -X POST http://0.0.0.0:8001/services/example_service/routes \
    #   --data 'paths[]=/mock' \
    #   --data 'name=mocking'


    # curl -i -X POST http://0.0.0.0:8001/services/example_service2/routes \
    #   --data 'paths[]=/rou2' \
    #   --data 'hosts[]=api.com'

    # curl -i -X GET http://0.0.0.0:8000/oi -H="Host: api.com"


def routes_list(service_name):
    pprint(requests.get(url=f"{admin_host}/services/{service_name}/routes").json())


def routes_delete(route_name):
    pprint(requests.delete(url=f"{admin_host}/routes/{route_name}"))


def targets_create(upstream_name, target):
    # ipdb.set_trace()
    data = {
        # "upstream": {"id":f"{upstream_id}"},
        "target": target,
        # "weight": 100,
        # "tags": ["user-level", "low-priority"]
    }

    response = requests.post(
        url=f"{admin_host}/upstreams/{upstream_name}/targets",
        json=data
    )
    pprint("Create Target")
    pprint(response)


def targets_list(upstream_name):
    pprint(requests.get(f"{admin_host}/upstreams/{upstream_name}/targets").json())


def targets_delete(upstream_name, host):
    pprint(requests.delete(url=f"{admin_host}/upstreams/{upstream_name}/targets/{host}"))


if __name__ == "__main__":

    # Set your localhost ip here
    # Kong needs to know it. If not request will be redirectd internally
    my_localhost_ip = "192.168.0.105"

    admin_host = "http://0.0.0.0:8001"
    host_1 = f"{my_localhost_ip}:9091"
    host_2 = f"{my_localhost_ip}:9092"
    host_3 = f"{my_localhost_ip}:9093"

    # ipdb.set_trace()

    service_name = "my-service"
    upstream_name = "my-upstream"
    route_name="rte"

    # CREATE
    upstream_id = upstreams_create(upstream_name=upstream_name)
    services_create(service_name=service_name, host=upstream_name)
    routes_create(service_name=service_name, route_name=route_name, paths=["/rte"])
    targets_create(upstream_name=upstream_name, target=host_1)
    targets_create(upstream_name=upstream_name, target=host_2)
    targets_create(upstream_name=upstream_name, target=host_3)


    # UPDATE
    # upstreams_update(upstream_name=upstream_name)


    # DELETE
    # targets_delete(upstream_name=upstream_name, host=host_1)
    # targets_delete(upstream_name=upstream_name, host=host_2)
    # targets_delete(upstream_name=upstream_name, host=host_3)
    # routes_delete(route_name=route_name)
    # services_delete(service_name=service_name)
    # upstreams_delete(upstream_name=upstream_name)


    # LIST
    # services_list(service_name=service_name)
    # routes_list(service_name=service_name)
    # targets_list(upstream_name=upstream_name)
    # upstreams_list()


    # MANUAL CREATION

    # curl -i -X POST http://0.0.0.0:8001/upstreams \
    #   --data name=upstream

    # curl -i -X POST http://0.0.0.0:8001/services \
    #   --data name=example_service2 \
    #   --data host='upstream'

    # curl -i -X POST http://0.0.0.0:8001/services/example_service2/routes \
    #   --data 'paths[]=/' \
    #   --data name=mocking

    # curl -X POST http://0.0.0.0:8001/upstreams/upstream/targets \
    #   --data target='mockbin.org:80'

    # curl -X POST http://0.0.0.0:8001/upstreams/upstream/targets \
    #   --data target='httpbin.org:80'

    # curl -X POST http://0.0.0.0:8001/upstreams/my-upstream/targets \
    #   --data target='192.168.0.105:9090'

    #### Create a service with path /anything/api/oilers:
    curl -i -X POST http://0.0.0.0:8001/services \
      --data name=runandshoot4ever \
      --data host=httpbin.org \
      --data path=/anything/api/oilers

    #### Create a route with path /titans/api:

    curl -i -X POST http://0.0.0.0:8001/services/runandshoot4ever/routes \
      --data name=tannehill \
      --data 'paths[]=/titans/api'

    #### Make an API call to /titans/api:
    curl -i -X GET http://0.0.0.0:8000/titans/api/players/search\?q=henry




    #### Create a service with path /anything/api/oilers:
    curl -i -X POST http://0.0.0.0:8001/services \
      --data name=rewrite-test \
      --data host=httpbin.org


    #### Create a route with path /titans/api:

    curl -i -X POST http://0.0.0.0:8001/services/rewrite-test/routes \
      --data name=cli2 \
      --data 'paths[]=/clients/(?<function>\\\[a-zA-Z0-9]+?)'


    #### Make an API call to /titans/api:
    curl -i -X GET http://0.0.0.0:8000/clients/22/fonts