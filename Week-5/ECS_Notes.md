# ECS (Elastic Container Service) - Class Notes

## What is ECS?
AWS service to run, manage, and scale containers in production. Solves the pain of running containers manually on EC2 with custom scripts.

---

## Capacity Types (Where containers actually run)

**1. EC2 (Auto Scaling Group)**
- You manage the VMs — patching, scaling, compliance software (Qualys, Symantec)
- Full flexibility but high operational overhead
- Use when compliance requires software installed on underlying compute

**2. Fargate** ✅ *(recommended/easiest)*
- AWS manages all underlying compute — fully "serverless" from your perspective
- No patching, no VM visibility, no scaling of VMs
- Tied to AWS networking (cannot use custom networking)

**3. On-Premises / ECS Anywhere**
- Run containers on your own data center hardware
- Connect via VPN or Direct Connect
- You manage compute, patching, scaling — most complex option
- Use case: compliance requiring on-prem execution, or utilizing idle physical servers

---

## Core ECS Concepts

### Task Definition *(Template)*
A JSON config that defines:
- Container image (public or private)
- Port mappings
- CPU & memory (soft limit = minimum needed, hard limit = maximum allowed)
- Logging config → CloudWatch log groups
- Networking mode (AWS VPC or custom)
- Environment variables & secrets
- Volumes

### Task *(Wrapper around containers)*
- A running unit — can hold **one or more containers**
- Provides AWS networking integration (replaces Docker networking)
- **Not self-healing** — if it dies, it stays dead
- **Not auto-scaling**
- Use for: one-time jobs, automations, AI agents that run and finish

┌─────────────────────────────┐
│           TASK              │
│  ┌───────────┐              │
│  │ Container │              │
│  │   (app)   │              │
│  └───────────┘              │
│                             │
│  - AWS Networking (ENI)     │
│  - IAM Role attached        │
│  - CloudWatch logging       │
│  - CPU/Memory allocated     │
└─────────────────────────────┘

### Service *(Wrapper around tasks)*
- Manages **scaling** and **self-healing** of tasks
- Self-healing = if a task dies, a new one comes up (not the same task restarting)
- Define desired task count
- Attach a **load balancer** here
- Use for: always-running apps (web servers, APIs, persistent agents)
┌─────────────────────────────────────────┐
│                SERVICE                  │
│                                         │
│  ┌──────────┐  ┌──────────┐  ┌────────┐ │
│  │  TASK 1  │  │  TASK 2  │  │ TASK 3 │ │
│  │ ┌──────┐ │  │ ┌──────┐ │  │┌──────┐│ │
│  │ │ App  │ │  │ │ App  │ │  ││ App  ││ │
│  │ └──────┘ │  │ └──────┘ │  │└──────┘│ │
│  └──────────┘  └──────────┘  └────────┘ │
│                                         │
│  - Self Healing    - Load Balancer      │
│  - Auto Scaling    - Desired Count      │
└─────────────────────────────────────────┘

### Cluster
- Logical grouping — **not a physical resource, no cost**
- (Unlike EKS cluster which does cost money)

---

## IAM Roles in ECS (Two types)

| Role | Purpose | When active |
|------|---------|-------------|
| **Task Execution Role** | Pulls image from ECR, creates CloudWatch logs | During container startup |
| **Task Role** | Allows running container to call other AWS services (RDS, DynamoDB, etc.) | While container is running |

> Always use **minimum permission model** — create custom policies over broad managed ones.

---

## ECR (Elastic Container Registry)
- AWS's private Docker registry (like Docker Hub but private)
- Authentication via IAM (no manual token needed if roles are configured correctly)
- Image URI pattern: `<account-id>.dkr.ecr.<region>.amazonaws.com/<repo-name>:<tag>`

**Push flow:**
```bash
# 1. Authenticate Docker to ECR
aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <account-id>.dkr.ecr.<region>.amazonaws.com

# 2. Build & tag
docker build -t app .
docker tag app:latest <ecr-uri>:1.0

# 3. Push
docker push <ecr-uri>:1.0
```

---

## ECS vs EKS

| | ECS | EKS |
|--|-----|-----|
| Complexity | Simpler | Complex |
| Scale | Moderate | Massive (up to 64,000 nodes) |
| Networking | AWS networking only | Fully customizable |
| Cloud portability | Hard to migrate | Easy (Kubernetes is cloud-agnostic) |
| Multi-client isolation | Difficult | Namespaces make it easy |
| GPU/ML workloads | Limited | Highly customizable |
| Team requirement | Small team OK | Needs Kubernetes specialists |
| Microservices | Works for few services | Built for large-scale microservices |

**Rule of thumb:** ECS for simpler setups with small teams. EKS when you need scale, customization, or multi-cloud portability.

---

## CloudWatch Logging
- All container logs → CloudWatch **log groups**
- Default log group: `/ecs/<task-definition-name>`
- Can set up dashboards, alerts, and monitoring from CloudWatch

---

## Key Reminders
- **Never** use public IP directly for ECS in production — always use a **Load Balancer**
- Tasks in public subnets get a public IP but this is only for testing
- Without the correct Task Execution Role → task will fail to start (common Terraform gotcha)
- Task definition versions are immutable — changes create a new revision

---

