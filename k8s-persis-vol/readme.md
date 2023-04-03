# How to create and attach a persistent volume in k8s

1. Apply persistent volume

```
kubectl apply -f redis-pv.yaml
```

2. Apply persistent volume claim

```
kubectl apply -f redis-pvc.yaml
```

3. Apply redispod with mounted volume

```
kubectl apply -f redispod.yaml
```

4. Connect to the container using the redis cli

```
kubectl exec redispod -it redis-cli
```

5. Write data to the container

```
SET server:name "redis server"
```

6. Read the data

```
GET server:name
```

7. Quit the redis cli

```
QUIT
```

8. Delete redispod

```
kubectl delete pod redispod
```

9. Edit the pod deployment file to change the pod name from

```
name: redispod
```

to

```
name: redispod2
```

10. Apply the new pod

```
kubectl apply -f redispod.yaml
```

11. Verify the data still exists

```
GET server:name
```

The data still exists as the volume was not deleted, just the pod.
When the pod was recreated, it reattached to the volume along with its data

This was a practice lab - all yaml scripts belong to acloudguru