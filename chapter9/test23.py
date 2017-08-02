echo 'apiVersion: apps / v1beta1
kind: Deployment
metadata:
    name: ttttt
    namespace: zihua
spec:
    replicas: 3
    revisionHistoryLimit: 10
    template:
        metadata:
            labels:
                app: nginx
        spec:
            containers:
            - name: nginx
                image: nginx: 1.10
                ports:
                - containerPort: 80
' | kubectl -s '127.0.0.1: 18081' create - f -


echo 'apiVersion: apps / v1beta1
kind: Deployment
metadata:
    name: deployment - example
spec:
    replicas: 3
    revisionHistoryLimit: 10
    template:
        metadata:
            labels:
                app: nginx
        spec:
            containers:
            - name: nginx
                image: nginx: 1.11
                ports:
                - containerPort: 80
' | kubectl -s '127.0.0.1: 18081' replace - f -


{
    "type": "ADDED",
    "object": {
        "kind": "Pod",
        "apiVersion": "v1",
        "metadata": {
            "name": "deployment-example-2777353149-3sc7p",
            "generateName": "deployment-example-2777353149-",
            "namespace": "default",
            "selfLink": "/api/v1/namespaces/default/pods/deployment-example-2777353149-3sc7p",
            "uid": "2be48cb1-704c-11e7-a855-0242ac120003",
            "resourceVersion": "589872",
            "creationTimestamp": "2017-07-24T08:43:31Z",
            "labels": {
                "app": "nginx",
                "pod-template-hash": "2777353149"
            },
            "annotations": {
                "kubernetes.io/created-by": "{\"kind\":\"SerializedReference\",\"apiVersion\":\"v1\",\"reference\":{\"kind\":\"ReplicaSet\",\"namespace\":\"default\",\"name\":\"deployment-example-2777353149\",\"uid\":\"2be37c42-704c-11e7-a855-0242ac120003\",\"apiVersion\":\"extensions\",\"resourceVersion\":\"585985\"}}\n"
            },
            "ownerReferences": [
                {
                    "apiVersion": "extensions/v1beta1",
                    "kind": "ReplicaSet",
                    "name": "deployment-example-2777353149",
                    "uid": "2be37c42-704c-11e7-a855-0242ac120003",
                    "controller": true,
                    "blockOwnerDeletion": true
                }
            ]
        },
        "spec": {
            "volumes": [
                {
                    "name": "default-token-cpwxf",
                    "secret": {
                        "secretName": "default-token-cpwxf",
                        "defaultMode": 420
                    }
                }
            ],
            "containers": [
                {
                    "name": "nginx",
                    "image": "nginx:1.10",
                    "ports": [
                        {
                            "containerPort": 80,
                            "protocol": "TCP"
                        }
                    ],
                    "resources": {},
                    "volumeMounts": [
                        {
                            "name": "default-token-cpwxf",
                            "readOnly": true,
                            "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount"
                        }
                    ],
                    "terminationMessagePath": "/dev/termination-log",
                    "terminationMessagePolicy": "File",
                    "imagePullPolicy": "IfNotPresent"
                }
            ],
            "restartPolicy": "Always",
            "terminationGracePeriodSeconds": 30,
            "dnsPolicy": "ClusterFirst",
            "serviceAccountName": "default",
            "serviceAccount": "default",
            "nodeName": "dce182",
            "securityContext": {},
            "schedulerName": "default-scheduler",
            "tolerations": [
                {
                    "key": "node.alpha.kubernetes.io/notReady",
                    "operator": "Exists",
                    "effect": "NoExecute",
                    "tolerationSeconds": 300
                },
                {
                    "key": "node.alpha.kubernetes.io/unreachable",
                    "operator": "Exists",
                    "effect": "NoExecute",
                    "tolerationSeconds": 300
                }
            ]
        },
        "status": {
            "phase": "Running",
            "conditions": [
                {
                    "type": "Initialized",
                    "status": "True",
                    "lastProbeTime": null,
                    "lastTransitionTime": "2017-07-24T08:43:31Z"
                },
                {
                    "type": "Ready",
                    "status": "True",
                    "lastProbeTime": null,
                    "lastTransitionTime": "2017-07-24T09:04:38Z"
                },
                {
                    "type": "PodScheduled",
                    "status": "True",
                    "lastProbeTime": null,
                    "lastTransitionTime": "2017-07-24T08:43:31Z"
                }
            ],
            "hostIP": "192.168.100.182",
            "podIP": "172.28.245.114",
            "startTime": "2017-07-24T08:43:31Z",
            "containerStatuses": [
                {
                    "name": "nginx",
                    "state": {
                        "running": {
                            "startedAt": "2017-07-24T09:04:38Z"
                        }
                    },
                    "lastState": {},
                    "ready": true,
                    "restartCount": 0,
                    "image": "nginx:1.10",
                    "imageID": "docker-pullable://nginx@sha256:6202beb06ea61f44179e02ca965e8e13b961d12640101fca213efbfd145d7575",
                    "containerID": "docker://5ff1909904031a2a531e2f6439e5b76d0d07fa3bc8893a3dab7b9485c15f8846"
                }
            ],
            "qosClass": "BestEffort"
        }
    }
}


{
    "type": "ADDED",
    "object": {
        "kind": "Deployment",
        "apiVersion": "apps/v1beta1",
        "metadata": {
            "name": "deployment-example",
            "namespace": "default",
            "selfLink": "/apis/apps/v1beta1/namespaces/default/deployments/deployment-example",
            "uid": "2be305c9-704c-11e7-a855-0242ac120003",
            "resourceVersion": "586880",
            "generation": 1,
            "creationTimestamp": "2017-07-24T08:43:31Z",
            "labels": {
                "app": "nginx"
            },
            "annotations": {
                "deployment.kubernetes.io/revision": "1"
            }
        },
        "spec": {
            "replicas": 3,
            "selector": {
                "matchLabels": {
                    "app": "nginx"
                }
            },
            "template": {
                "metadata": {
                    "creationTimestamp": null,
                    "labels": {
                        "app": "nginx"
                    }
                },
                "spec": {
                    "containers": [
                        {
                            "name": "nginx",
                            "image": "nginx:1.10",
                            "ports": [
                                {
                                    "containerPort": 80,
                                    "protocol": "TCP"
                                }
                            ],
                            "resources": {},
                            "terminationMessagePath": "/dev/termination-log",
                            "terminationMessagePolicy": "File",
                            "imagePullPolicy": "IfNotPresent"
                        }
                    ],
                    "restartPolicy": "Always",
                    "terminationGracePeriodSeconds": 30,
                    "dnsPolicy": "ClusterFirst",
                    "securityContext": {},
                    "schedulerName": "default-scheduler"
                }
            },
            "strategy": {
                "type": "RollingUpdate",
                "rollingUpdate": {
                    "maxUnavailable": "25%",
                    "maxSurge": "25%"
                }
            },
            "revisionHistoryLimit": 10,
            "progressDeadlineSeconds": 600
        },
        "status": {
            "observedGeneration": 1,
            "replicas": 3,
            "updatedReplicas": 3,
            "unavailableReplicas": 3,
            "conditions": [
                {
                    "type": "Available",
                    "status": "False",
                    "lastUpdateTime": "2017-07-24T08:43:31Z",
                    "lastTransitionTime": "2017-07-24T08:43:31Z",
                    "reason": "MinimumReplicasUnavailable",
                    "message": "Deployment does not have minimum availability."
                },
                {
                    "type": "Progressing",
                    "status": "False",
                    "lastUpdateTime": "2017-07-24T08:53:32Z",
                    "lastTransitionTime": "2017-07-24T08:53:32Z",
                    "reason": "ProgressDeadlineExceeded",
                    "message": "ReplicaSet \"deployment-example-2777353149\" has timed out progressing."
                }
            ]
        }
    }
}


docker - -tlsverify - -tlscacert = ca.pem \
    - -tlscert = cert.pem \
    - -tlskey = key.pem \
    - H = 127.0.0.1: 2376 ps


kind: Deployment
metadata:
    name: deployment - example
spec:
    replicas: 3
    revisionHistoryLimit: 10
    template:
        metadata:
            labels:
                app: nginx
        spec:
            containers:
            - name: nginx
                image: nginx: 1.11
                ports:
                - containerPort: 80

kind: Namespace
apiVersion: v1
metadata:
    name: default
    annotations:
    net.beta.kubernetes.io / network - policy: |
        {
            "ingress": {
                "isolation": "DefaultDeny"
            }
        }


apiVersion: extensions / v1beta1
kind: NetworkPolicy
metadata:
    name: allow - nginx1 - to - nginx2
    namespace: default2
spec:
    podSelector:
    matchLabels:
    run: nginx2
    ingress:
    - from:
        - podSelector:
            matchLabels:
                run: nginx1
