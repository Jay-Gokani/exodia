User request -> mongo-express external service -> mongo-express + mongo-secret -> mongodb internal service + mongo-configmap specified URL -> mongodb + mongo-secret for auth -> (loops) 

Note: if Docker Desktop or the computer restarts, an error will appear stating that the host and port can't be connected to
Minikube will need to be restarted with:
minikube start

Request flow through K8s components:
1. MongoDB brower request

2. Mongo Express External Service

3. Mongo Express Pod

4. MongoDB Internal Service (using ConfigMap specified URL)

5. MongoDB pod (using Secret to authenticate with the DB Username and Password)


Instructions:
1. Create a directory to house all the files

2. Create a mongodb yaml file which specifies the config. This will be in a public repo so a Secret needs to be created so sensitive data isn't exposed

3. Create a secret which defines the credentials for the mongodb in another config file. The username and password need to be base64 encoded. Put the key and value details in the Deployment config.

4. Easiest way to encode text is by running the following in the terminal:
echo -n "<text>" | base64

5. Apply the Secret by running:
minikube start
kubectl apply -f mongo-secret.yaml
kubectl get secret
Note the f flag is for 'filename'

6. Apply the Deployment
kubectl apply -f mongodb.yaml

7. Watch the resources which are being created
kubectl get all
kubectl get pod
kubectl get pod --watch

8. Add a service config to the mongo.yaml file
this is often added to the same file as the service attaches to the deployment

9. kubectl apply -f mongo.yaml
an output will come back stating that the deployment was unchanged but service created

10. kubectl describe service mongodb-service
returns an output with one line being which app it is attached to, and the endpoint of the pod, confirming it was successfully attached

11. write out scripts for mongo-express.yaml and mongo-configmap.yaml
the configmap is used for holding the IP for the mongodb service - it can be referenced by other files too

12. kubectl apply -f mongo-configmap.yaml
this has to be done before the mongo-express deployment as it is a dependancy

13. kubectl apply -f mongo-express.yaml

14. add Service config to mongo-express.yaml
dash three times under the script
the Service attaches to the mongo-express deployment
the default 'type' which does not need to be explicitly express is internal which gives an internal Cluster IP
we choose LoadBalancer type which is external

15. kubectl get service
one has come back for kubernetes, one for mongodb and one named 'mongo-express-service'

16. minikube service mongo-express-service
this is needed for minikube to assign an external IP address to the service, which can then be accessed through a browser

17. minikube delete --all 
delete the entire cluster
be sure to start minikube again when creating the next project with:
minikube start 