
1. cd into minikube-nginx dir

2. Start minikube

```
minikube start
```

3. Create Kubernetes service

```
kubectl create -f service.yaml
```

4. Create Kubernetes service

```
kubectl create -f deployment.yaml
```

5. Watch for the creation of the 3 pods and 1 service

```
Kubectl get all
```

6. Minikube doesn't assign an external IP, so the following needs to be issued to expose I need to use another command to expose it

```
minikube service nginx-service
```

7. Clean up

```
minikube delete --all
```
