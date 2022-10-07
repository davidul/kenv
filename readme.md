# KENV

Lists env variables of docker image or K8s pod.
By default listen on port 9090.

Building docker image

```
docker build -t kenv .
```

Or use a make command

```shell
make build
```

## Execution

You can run either in server mode or just simply command line.
In server mode HTTP server will be started.

Simple execution
```shell
python kenv.py
```

Execute in docker

```shell
docker run kenv
```

Execute in docker in server mode

```shell
docker run -p 9090:9090 kenv --server=y
```

Query `http://localhost:9090`, sample response

```json
{
    "sysinfo": {
        "os-uname": [
            "Linux",
            "431f4d701606",
            "5.10.104-linuxkit",
            "#1 SMP PREEMPT Thu Mar 17 17:05:54 UTC 2022",
            "aarch64"
        ],
        "os-name": "posix"
    },
    "environment": {
        "PATH": "/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
        "HOSTNAME": "431f4d701606",
        "LANG": "C.UTF-8",
        "GPG_KEY": "A035C8C19219BA821ECEA86B64E628F8D684696D",
        "PYTHON_VERSION": "3.10.5",
        "PYTHON_PIP_VERSION": "22.0.4",
        "PYTHON_SETUPTOOLS_VERSION": "58.1.0",
        "PYTHON_GET_PIP_URL": "https://github.com/pypa/get-pip/raw/49ca29908cfd49683da12f2d5a4fa5689539f9d9/public/get-pip.py",
        "PYTHON_GET_PIP_SHA256": "d077d469ce4c0beaf9cc97b73f8164ad20e68e0519f14dd886ce35d053721501",
        "HOME": "/root"
    }
}
```
Pass it to ```jq``` to get nice output

```shell
curl http://localhost:9090 | jq
```

## K8s

Using minikube, start the cluster

```shell
minikube start
```

Load the image to the `minikube` 

```shell
minikube image load kenv:latest
```

Apply the POD definition

```shell
kubectl apply -f pod.yml
```

Apply the SVC definition

```shell
kubectl apply -f service.yml
```

Query the service

```shell
curl 10.100.130.155:9090
```