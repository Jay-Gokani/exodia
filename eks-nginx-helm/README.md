TODO:

4. build eks cluster
5. deploy helm chart

helm install nickname chart_name --dry-run

6. curl helm chart

### Instructions

1. Ensure the following binaries are installled:
- eksctl
- aws
- helm
- kubectl

2. Login to AWS, go into IAM and create keys for use in the CLI

3. On the Terminal, follow the prompts to enter Access Key, Secret Key, region and output format.

The region we'll be using is 'us-east-1' and the default output is 'JSON'

```
aws configure
```

4. Verify the correct credentials are being use

```
aws sts get-caller-identity
```

5. 
