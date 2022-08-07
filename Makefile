
build:
	docker build -t kenv:latest .

k8s-deploy:
	minikube image load kenv:latest