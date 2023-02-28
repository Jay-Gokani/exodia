
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
