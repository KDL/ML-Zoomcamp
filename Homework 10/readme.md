# Homework 10
For homework 10, the output of Bash console, pasted as HTML code is used
For this, [console1.html](console1.html) (main console, which includes the input & outputs) and [console2.html](console2.html) (secondary console output) are used.

Commands are the following:

## Q1: Kind version
`` ./kind --version ``
kind version 0.11.1


## Q2: Verification
`` sudo kubectl get service ``

IP: 10.96.0.1

## Q3: Uploading to Kind
``  sudo ./kind load docker-image churn-model:v001 ``
Image: "churn-model:v001" with ID "sha256:46c6e2e478a29f8c10fd5f6cf765ed0ab1b3f4ae5bce14b2c3283f1ce5d2337c" not yet present on node "kind-control-plane", loading…

## Q4: Deployment
Port: 9696 (From homework 5)

## Q5: Pod name
`` sudo kubectl get pod ``
NAME                    READY   STATUS    RESTARTS   AGE
churn-66f869ddb-qg2xj   1/1     Running   0          10s

The name of the pod is churn-66f869ddb-qg2xj

## Q6: Service
appname is churn
