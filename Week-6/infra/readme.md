# 📝 Student Portal — AWS ECS Deployment

> Containerized web application deployed on AWS ECS (Fargate) using Terraform for infrastructure as code, with ECR for image registry and ALB for load balancing.

---

## 📋 Table of Contents

- [Architecture Overview](#architecture-overview)
- [Prerequisites](#prerequisites)
- [ECR Setup & Image Push](#ecr-setup--image-push)
- [Deploy Infrastructure](#deploy-infrastructure)
- [ECS Debugging Guide](#ecs-debugging-guide)
- [IAM Troubleshooting](#iam-troubleshooting)
- [Quick Checklist](#quick-checklist)

---

## 🏗️ Architecture Overview

```
Terraform → Creates infrastructure (ECR, ECS, ALB, IAM)
Docker    → Builds & pushes container image
ECS       → Pulls image from ECR and runs container
ALB       → Routes traffic to ECS tasks
CloudWatch → Collects logs & helps debug failures
```

---

## ✅ Prerequisites

- AWS CLI configured (`aws configure`)
- Terraform >= 1.0
- Docker installed and running
- IAM permissions for ECR, ECS, ALB, CloudWatch, and IAM

---

## 📦 ECR Setup & Image Push

### 1. Create ECR Repository

```bash
terraform init
terraform apply -target=aws_ecr_repository.app_image
```

### 2. Get AWS Account ID

```bash
aws sts get-caller-identity
```

Copy the `Account` value — you'll need it in the next steps.

### 3. Authenticate Docker with ECR

```bash
aws ecr get-login-password --region us-east-1 \
  | docker login --username AWS \
    --password-stdin <ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com
```

### 4. Build Docker Image

```bash
docker build -t studentportal .
```

### 5. Tag Image

```bash
docker tag studentportal:latest \
  <ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/jan26week5-studentportal:1.0
```

### 6. Push Image to ECR

```bash
docker push \
  <ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/jan26week5-studentportal:1.0
```

### 7. Reference Image in Terraform (ECS Task Definition)

**Hardcoded (not recommended):**
```hcl
image = "<ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/jan26week5-studentportal:1.0"
```

**Using Terraform reference (recommended):**
```hcl
image = "${aws_ecr_repository.app_image.repository_url}:1.0"
```

---

## 🚀 Deploy Infrastructure

```bash
terraform apply
```

---

## 🐞 ECS Debugging Guide — 0/1 Tasks Running

### Step 1: Inspect Stopped Tasks

1. Navigate to **Amazon ECS → Cluster → Service → Tasks**
2. Filter by **Stopped**
3. Click the task → review **Stopped Reason**

---

### Step 2: Common Errors & Fixes

| Error | Cause | Fix |
|---|---|---|
| `CannotPullContainerError` | Image not pushed or wrong URI/tag | Re-push image to ECR |
| `ResourceInitializationError` | No internet access (private subnet) | Use public subnet or add NAT Gateway |
| `AccessDeniedException` | Missing IAM role permissions | Attach required policies (see below) |
| Port mismatch | App port differs from ECS config | Match container port in task definition |
| Health check failed | Wrong ALB health check path | Set correct path in `health_check` block |

---

####  CannotPullContainerError

```bash
# Verify image exists in ECR
aws ecr describe-images --repository-name jan26week5-studentportal

# Re-push if missing
docker push <ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/jan26week5-studentportal:1.0
```

####  ResourceInitializationError (No internet / NAT)

```hcl
# Option A: Deploy in public subnet with public IP
network_configuration {
  assign_public_ip = true
  subnets          = [aws_subnet.public.id]
}

# Option B: Deploy in private subnet with NAT Gateway
# (add NAT Gateway to your Terraform config)
```

####  Health Check Failed

```hcl
health_check {
  path                = "/"
  interval            = 30
  timeout             = 5
  healthy_threshold   = 2
  unhealthy_threshold = 3
}
```

---

### Step 3: Check CloudWatch Logs

1. Navigate to **Amazon CloudWatch → Log Groups → `/ecs/jan26week5-studentportal`**
2. Check for:
   - Application crashes or startup errors
   - Database connection failures
   - Missing environment variables

---

### Step 4: Verify Networking

| Component | Required Rule |
|-----------|---------------|
| ALB Security Group | Inbound HTTP (port 80) from `0.0.0.0/0` |
| ECS Security Group | Inbound from ALB Security Group |
| Subnets | Public (assign public IP) OR Private + NAT Gateway |

---

## 🔐 IAM Troubleshooting

### AccessDeniedException — logs:CreateLogGroup

**Error:**
```
ResourceInitializationError: failed to validate logger args:
User: arn:aws:sts::<ACCOUNT_ID>:assumed-role/ecsTaskExecutionRole/...
is not authorized to perform: logs:CreateLogGroup
```

**Root Cause:** The ECS task execution role is missing CloudWatch Logs permissions.

**Fix — Inline Policy (Console):**

1. Go to **IAM → Roles** → search for `jan26-bootcamp-student-portal-ecsTaskExecutionRole`
2. Click **Add permissions → Create inline policy**
3. Switch to **JSON** tab and paste:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents",
        "logs:DescribeLogStreams"
      ],
      "Resource": "arn:aws:logs:us-east-1:*:log-group:/ecs/*"
    }
  ]
}
```

4. Name it `ECSCloudWatchLogsPolicy` → **Save**

**Fix — Terraform (recommended):**

```hcl
resource "aws_iam_role_policy" "ecs_cloudwatch_logs" {
  name = "ECSCloudWatchLogsPolicy"
  role = aws_iam_role.ecs_task_execution_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents",
          "logs:DescribeLogStreams"
        ]
        Resource = "arn:aws:logs:us-east-1:*:log-group:/ecs/*"
      }
    ]
  })
}
```

---

## ✅ Quick Checklist

- [ ] ECR repository created via Terraform
- [ ] Docker image built and pushed to ECR
- [ ] Correct image URI referenced in ECS task definition
- [ ] CloudWatch log group permissions attached to task execution role
- [ ] ALB and ECS security groups configured correctly
- [ ] Subnets configured (public IP or NAT Gateway)
- [ ] Health check path matches application route

---

## 📎 Useful Commands

```bash
# Check ECR images
aws ecr describe-images --repository-name jan26week5-studentportal

# Get current AWS identity
aws sts get-caller-identity

# List ECS services
aws ecs list-services --cluster <CLUSTER_NAME>

# Describe stopped tasks
aws ecs describe-tasks --cluster <CLUSTER_NAME> --tasks <TASK_ARN>
```

--- 

*Infrastructure managed with [Terraform](https://www.terraform.io/) · Container registry on [Amazon ECR](https://aws.amazon.com/ecr/) · Runtime on [Amazon ECS Fargate](https://aws.amazon.com/fargate/)*