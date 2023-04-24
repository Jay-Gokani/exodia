
This was a lab which I followed on QA Cloud Academy. The code is not my own.

### Set-up 

1. Log into AWS Console.
There are two EC2 instances, one of which runs a web-based IDE

2. Copy the public IPV4 IP address of the IDE instance and navigate to it and inspect the code (which is found in this repo)

### Deploy Python API application

Here we will deploy the Python app in a k8s build (deploymen and service) and build a generator pod to continually make HTTP requests against the app.

The first 4 endpoints in code > api.py all introduce latency and the 5 returns a HTTP 500 error, all which Prometheus will track

Within k8s > api.yml, note the following:

- Lines 1-25: API Deployment containing 2 pods
- Line 22: Pods are based off the container image cloudacademydevops/api-metrics
- Lines 27-46: API Service - loadbalances traffic across the 2 API Deployment pods
- Lines 34-37: API Service is annotated to ensure that the Prometheus scraper will automatically discover the API pods behind it. Prometheus will then collect their metrics from the discovered targets

1. Start a new Terminal
2. Deploy the k8s cluster (which also deploys the Python app which is referenced inside it)

kubectl apply -f ./code/k8s

3. Confirm the two API pods are running - two will show

kubectl get po

4. Confirm the service was created

kubectl get svc

5. Spin up a generator pod to generate traffic against the API app

kubectl run generator --env="API_URL=http://api-service:5000" --image=cloudacademydevops/api-generator --image-pull-policy IfNotPresent

6. Confirm the generator pod is running

kubectl get po

### Install and Configure K8s Dashboard

Here, we spin up the K8s dashboard and expose it on port 30990 so it can locally be accessed. It's used to deploy containerised apps to a k8s cluster, troubleshoot and managed other cluster resources.

1. Create a namespace in the cluster

kubectl create ns monitoring

2. Install the dashboard into the monitoring namespace, using the publicly available Helm Kubernetes Dashboard Helm Chart

{
helm repo add k8s-dashboard https://kubernetes.github.io/dashboard
helm repo update
helm install k8s-dashboard --namespace monitoring k8s-dashboard/kubernetes-dashboard --set=protocolHttp=true --set=serviceAccount.create=true --set=serviceAccount.name=k8sdash-serviceaccount --version 3.0.2
}

3. Establish permissions to allow the dashboard to read and write all resources

kubectl create clusterrolebinding kubernetes-dashboard --clusterrole=cluster-admin --serviceaccount=monitoring:k8sdash-serviceaccount

4. Expose the dashboard to the internet using a NodePort service on port 30990

{
kubectl expose deployment k8s-dashboard-kubernetes-dashboard --type=NodePort --name=k8s-dashboard --port=30990 --target-port=9090 -n monitoring
kubectl patch service k8s-dashboard -n monitoring -p '{"spec":{"ports":[{"nodePort": 30990, "port": 30990, "protocol": "TCP", "targetPort": 9090}]}}'
}

5. Get the public IP address of the k8s cluster that the dashboard was deployed into and view it.

A public IP address will return in this format: http://<PUBLIC_IP>:30990.

export | grep K8S_CLUSTER_PUBLICIP

### Install and Configure Prometheus

After deployment, Prom will collect HTTP request based metrics from the API pods and infrastructure (memory and CPU) metrics from the cluster's nodes. We'll expose this to port 30900 which will allow local access

1. Use the Helm chart to install Prom into the monitoring namespace

{
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add stable https://charts.helm.sh/stable
helm repo update
helm install prometheus --namespace monitoring --values ./code/prometheus/values.yml prometheus-community/prometheus --version 13.0.0
}

{
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add stable https://charts.helm.sh/stable
helm repo update
helm install prometheus --namespace monitoring --values ./code/prometheus/values.yml prometheus-community/prometheus --version 13.0.0
}

2. Confirm Prom has successfully been rolled out

kubectl get deployment -n monitoring -w

3. Confirm the Node Exporter DaemonSet has been created. This is used to collect infrastructure metrics off each node within the k8s cluster

kubectl get daemonset -n monitoring

4. Patch the DaemonSet to ensure Prom can collect metrics

kubectl patch daemonset prometheus-node-exporter -n monitoring -p '{"spec":{"template":{"metadata":{"annotations":{"prometheus.io/scrape": "true"}}}}}'

5. Expose Prom to the internet by creating a NodePort based service and mapping a port

{
kubectl expose deployment prometheus-server --type=NodePort --name=prometheus-main --port=30900 --target-port=9090 -n monitoring
kubectl patch service prometheus-main -n monitoring -p '{"spec":{"ports":[{"nodePort": 30900, "port": 30900, "protocol": "TCP", "targetPort": 9090}]}}'
}

6. Get the public IP address and view the Prom platform

export | grep K8S_CLUSTER_PUBLICIP

### Install and Configure Grafana

This will be built in the monitoring namespace in the k8s cluster. Grafana will be connected to Prometheus then a prebuild dashboard will be imported and deployed. The interface will be exposed over port 30300, allowing for local access

1. Use Helm to install the Grafana Helm Chart into the monitoring namespace in the k8s cluster

{
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update
helm install grafana --namespace monitoring grafana/grafana --version 6.1.14
}

2. Confirm it was built successfully

kubectl get deployment grafana -n monitoring -w

3. Expose the interface to the internet using a NodePort and map port 30300

{
kubectl expose deployment grafana --type=NodePort --name=grafana-main --port=30300 --target-port=3000 -n monitoring
kubectl patch service grafana-main -n monitoring -p '{"spec":{"ports":[{"nodePort": 30300, "port": 30300, "protocol": "TCP", "targetPort": 3000}]}}'
}

4. Extract the default admin password which will be used to login. The default username is 'admin'

kubectl get secret --namespace monitoring grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo

5. Get the public IP address and view

export | grep K8S_CLUSTER_PUBLICIP

6. On the interface go to

Data Sources > 
Add your first data source > 
Prometheus

7. Update the HTTP URL with what was found in step 5 and save

8. Open project/code/grafana/dashboard.json and copy the config

9. In the Grafana interface go to

Create >
Import >
Import via panel json

Paste the config and save

10. The Grafana dashboard is up!