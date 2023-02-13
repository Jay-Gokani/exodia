
Request flow through K8s components:
1. MongoDB brower request

2. Mongo Express External Service

3. Mongo Express Pod

4. MongoDB Internal Service (using ConfigMap specified URL)

5. MongoDB pod (using Secret to authenticate with the DB Username and Password)


Instructions:
1. Create a directory to house all the files

2. Create a mongodb yaml file to house the deployment config

