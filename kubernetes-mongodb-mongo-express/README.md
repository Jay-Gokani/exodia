User request -> mongo-express external service -> mongo-express + mongo-secret -> mongodb internal service + mongo-configmap specified URL -> mongodb + mongo-secret for auth -> (loops) 

Note: if Docker Desktop or the computer restarts, an error will appear stating that the host and port can't be connected to
Minikube will need to be restarted with:
```
minikube start
```

# Request flow through K8s components:
1. MongoDB brower request

2. Mongo Express External Service

3. Mongo Express Pod

4. MongoDB Internal Service (using ConfigMap specified URL)

5. MongoDB pod (using Secret to authenticate with the DB Username and Password)


# Instructions:
1. Create a directory to house all the files

2. Create a mongodb yaml file which specifies the config. This will be in a public repo so a Secret needs to be created so sensitive data isn't exposed

3. Create a secret which defines the credentials for the mongodb in another config file  
The username and password need to be base64 encoded  
Put the key and value details in the Deployment config

4. Easiest way to encode text is by running the following in the terminal:  
```
echo -n "<text>" | base64
```

5. Apply the Secret by running:  
```
minikube start  
kubectl apply -f mongo-secret.yaml  
kubectl get secret
```  
Note the f flag is for 'filename'

6. Apply the Deployment  
``` 
kubectl apply -f mongodb.yaml
```

7. Watch the resources which are being created  
```
kubectl get all
kubectl get pod
kubectl get pod --watch
```

8. Add a service config to the mongo.yaml file  
This is often added to the same file as the service attaches to the deployment  

9. Apply the service
```
kubectl apply -f mongo.yaml
```  
An output will come back stating that the deployment was unchanged but service created

10. Check the service was successfully attached
```
kubectl describe service mongodb-service
```  
Returns an output with one line being which app it is attached to, and the endpoint of the pod, confirming it was successfully attached

11. Write out scripts for mongo-express.yaml and mongo-configmap.yaml  
The configmap is used for holding the IP for the mongodb service - it can be referenced by other files too

12. Apply the configmap
```
kubectl apply -f mongo-configmap.yaml
```  
This has to be done before the mongo-express deployment as it is a dependancy

13. Apply mongo-express
```
kubectl apply -f mongo-express.yaml
```  

14. Add Service config to mongo-express.yaml  
Dash three times under the script  
The service attaches to the mongo-express deployment  
The default 'type' which does not need to be explicitly expressed is internal which gives an internal Cluster IP
We choose LoadBalancer type which is external

15. Investigate the services
```
kubectl get service
```  
One has come back for kubernetes, one for mongodb and one named 'mongo-express-service'

16. Assign an external IP address to the service
```
minikube service mongo-express-service
```  
This is needed for minikube to assign an external IP address to the service, which can then be accessed through a browser

17. Delete the cluster
```
minikube delete --all
```  
Delete the entire cluster  
Be sure to start minikube again when creating the next project with:  
```
minikube start
```