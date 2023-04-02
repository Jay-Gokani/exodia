### EKS Cluster

- Creating an AWS EKS cluster through the GUI
- The aim of this was to understand at a high-level how this works
- This is far from best practice

# Overview

- An AWS IAM User is created with an assigned key-pair
- EC2 instance is created, logged-in to and eksctl (to create the ekscluster), kubectl (to manage the k8s cluster) and AWS CLI (to interact with AWS resources) are installed on the instance
- EKS cluster created through the terminal of the EC2 instance
- In the k8s cluster, LoadBalancer then Deployment are created through the EC2 instance terminal

### How this might work on a real project

- AWS IAM Role created through .tf script
- Key-pair used to authenticate on local CLI to AWS, or better yet a secrets manager with a rotating hash
- EKS cluster deployed using eksctl and a tf script
- K8s components deployed using kubectl and Helm charts
- No EC2 needed

### Steps

1. IAM User in AWS Console is created, administrator permissions attached and a key-pair created
2. Create and launch EC2 instance with AWS Linux 2 image, auto public IP provided and key-pair attached
    1. Update AWS CLI through the EC2 terminal
    2. Install kubectl and eksctl binaries and move them to the ‘bin' dir through the terminal
3. Authenticate using

```
aws configure
```

4. Launch EKS Cluster with 3 worker nodes through EC2 instance using eksctl
```
eksctl create cluster —-name dev —-region us-east-1 —-nodegroup-name standard-workers —-node-type t3.medium —-nodes 3 -—nodes-min 1 —-nodes-max 4 —-managed
```

Or, a tidier version
```
eksctl create cluster \
  —-name dev \ 
  —-region us-east-1 \ 
  -—nodegroup-name standard-workers \
  -—node-type t3.medium \
  -—nodes 3 \
  -—nodes-min 1 \
  -—nodes-max 4 \ 
  -—managed
```

Alternatively, parse the config file (untested but gives the general idea)
```
eksctl create cluster -f eks-config.yaml
```

We could even use a tf file instead

5. Use kubectl to create a:

LoadBalancer (to connect to the internet) - this has to come first
```
kubectl apply -f service.yaml
```
 
Deployment (containing an NGINX image from DockerHub)
```
kubectl apply -f deployment.yaml
```

6. Access the application through printing then visiting the EXTERNAL-IP
```
kubectl get service
```
We have accessed the app through the LoadBalancer as this is what exposes the app to the internet

7. Test high availability by shutting down all nodes
Head into the AWS Console and change the Instance State of all three nodes to 'Stopped'

8. Go into EC2 terminal and run
```
kubectl get nodes
```
You will see that all 3 have stopped and 3 more are being built
AWS has auto-provisioned replacement instances
When the cluster is stable, the app is up and running again    