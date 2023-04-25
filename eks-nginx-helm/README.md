# Instructions

### General Tips

If on the Console and expected AWS resources do not show, ensure you are in the N. Virginia region

1. Create dir scafolding

.
├── CLI-output.txt
├── README.md
├── eks
│   └── eks-config.yaml
└── helm-magic
    ├── Chart.yaml
    ├── templates
    │   ├── deployment.yaml
    │   └── service.yaml
    └── values.yaml

1. Ensure the following binaries are installled:
- eksctl
- aws
- helm
- kubectl

2. Login to AWS, click the user in the top right > Security credentials > Access keys > create a pair key for use in the CLI

3. On the Terminal, follow the prompts to enter Access Key, Secret Key, region and output format.

The region we'll be using is 'us-east-1' and the default output is 'JSON'

```
aws configure
```

4. Verify the correct credentials are being used

```
aws sts get-caller-identity
```

5. cd into 'eks-magic' directory

6. Dry run the creation of the eks cluster to ensure the creation looks correct

```
eksctl create cluster -f eks-config.yaml --dry-run
```

7. Once happy, create the cluster

```
eksctl create cluster -f eks-config.yaml
```

8. Observe the cluster being created on the AWS Console. Note this will take 10-20 minutes.

Ensure to be in us-east-1 region, otherwise it won't show

``` 
CloudFormation > Stacks > eksctl-dev-cluster > Events
```

9. Observe the created cluster

```
Elastic Kubernetes Service > Clusters > eksctl-dev-cluster
```

10. cd up one

11. Dry run the Helm chart creation to ensure the creation looks correct

```
helm install wand helm-magic --dry-run
```

12. Install once happy

```
helm install wand helm-magic
```

13. If you want to make any changes post-installation, you will instead need to upgrade.
Otherwise, you'll get an error message stating 'cannot re-use a name that is still in use'

```
hem upgrade -i wand
```

14. Confirm all resources are running

```
kubectl get all
```

15. Test if you can access Nginx using the External-IP of the svc which was printed in the above command.
First cd into helm-magic, then:

Either:

```
curl <External-IP>
```

Or navigate to the webpage.

The expected confirmation message contains 'If you see this page, the nginx web server is successfully installed and working'

16. Clean up

```

# delete eks cluster
eksctl delete cluster --name dev

# sign out of aws console

# delete aws credentials, or upon using 'aws configure' again, new credentials can be added

To delete, go into:
vim ~/.aws/credentials 

```