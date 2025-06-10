This repository contains a sample microservice application that demonstrates:
- Application deployment on **Kubernetes (Minikube)**
- Kafka cluster setup using **Strimzi Operator**
- Producer job sending messages to Kafka
- Application consuming messages
- **OpenTelemetry Collector** configured to export traces to **KloudMate**

---

## Folder Structure

├── docker/
│ ├── Dockerfile.app
│ └── Dockerfile.producer
├── k8s/ 
│ ├── app/ 
│ │ ├── deployment.yaml
│ │ └── service.yaml
│ ├── kafka/ 
│ │ ├── installed-kafka-crd.yaml
│ │ ├── kafka-cluster.yaml
│ │ ├── kafka-nodepools.yaml
│ │ ├── kafka-producer-job.yaml
│ │ ├── kafka-topic.yaml
│ │ ├── kraft-cluster.yaml
│ │ ├── kraft-kafka.yaml
│ │ ├── strimzi-crds-0.46.0.yaml
│ │ └── strimzi-operator.yaml
│ └── observability/ 
│ ├── otel-collector-config.yaml
│ └── otel-collector-deployment.yaml
├── src/ 
│ ├── app.py
│ └── producer.py
├── test_trace.py 
└── README.md


---

## How to Run

### 1. Build Docker Images
```
docker build -t demo-app -f docker/Dockerfile.app .
docker build -t demo-producer -f docker/Dockerfile.producer .
2. Start Minikube and Enable Docker Registry Access
minikube start --driver=docker
eval $(minikube docker-env)
3. Deploy Strimzi & Kafka
kubectl apply -f k8s/kafka/
4. Deploy Application and Producer
kubectl apply -f k8s/app/
kubectl apply -f k8s/kafka/kafka-producer-job.yaml
5. Deploy OpenTelemetry Collector
kubectl apply -f k8s/observability/
 Observability with KloudMate
Traces are exported using the OTLP HTTP endpoint:

https://otel.kloudmate.com:4318
Auth header used:

Authorization: <Your_API_Key>
 Successful Trace Export Example
To verify the trace export setup, run:

python test_trace.py
If the setup is correct, you’ll see:

 Span sent to KloudMate successfully
And traces will be visible in KloudMate.

 Screenshot
![image](https://github.com/user-attachments/assets/4e3512b9-29a3-45f2-9799-7cfad78e5fe4)
