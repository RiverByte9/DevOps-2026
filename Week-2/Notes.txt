# 🚀 Complete NGINX Setup Guide on AWS EC2


> **A comprehensive, hands-on guide to deploying production-ready NGINX web server on AWS from scratch**

Learn how to launch an AWS EC2 instance, install and configure NGINX, and host your own website accessible from anywhere in the world — all in under 90 minutes!

---

## 📋 Table of Contents

- [What is NGINX?](#-what-is-nginx)
- [Why NGINX?](#-why-nginx)
- [What You'll Learn](#-what-youll-learn)
- [Prerequisites](#-prerequisites)
- [Quick Start](#-quick-start)
- [Phase 1: Infrastructure Setup](#-phase-1-infrastructure-setup)
- [Phase 2: NGINX Installation](#-phase-2-nginx-installation--configuration)
- [Understanding NGINX Configuration](#-understanding-nginx-configuration)
- [Common Commands](#-common-commands)
- [Troubleshooting](#-troubleshooting)
- [Next Steps](#-next-steps)
- [Contributing](#-contributing)

---

## 🌟 What is NGINX?

NGINX is a **lightweight, open-source web server** trusted by some of the world's highest-traffic websites. But it's not just a web server — it's a multi-purpose tool built for modern cloud-native architectures.

### What NGINX Can Do:

| Feature | Description |
|---------|-------------|
| 🌐 **Web Server** | Serves static content blazingly fast |
| 🔄 **Reverse Proxy** | Routes traffic to backend services seamlessly |
| ⚖️ **Load Balancer** | Spreads load across multiple app servers |
| 🔒 **SSL Termination** | Secures apps with HTTPS |
| ⚡ **Cache Layer** | Boosts performance by reducing backend hits |

---

## 💡 Why NGINX?

NGINX's **event-driven, asynchronous architecture** allows it to handle **thousands of concurrent connections** with minimal resource usage, making it ideal for:

- ✅ Containerized environments
- ✅ Microservice-based architectures
- ✅ Cloud-native deployments
- ✅ High-traffic applications
- ✅ DevOps workflows

That's why NGINX is a **go-to solution** in modern DevOps and cloud-native environments.

---

## 🎓 What You'll Learn

By completing this guide, you'll gain practical, production-ready skills:

### Infrastructure & Cloud
- ✅ Launch and configure AWS EC2 instances
- ✅ Set up security groups and firewall rules
- ✅ Manage cloud resources effectively

### NGINX & Web Servers
- ✅ Install NGINX on Amazon Linux 2
- ✅ Understand NGINX configuration hierarchy
- ✅ Configure virtual hosts and server blocks
- ✅ Manage web server lifecycle (start, stop, reload)

### Linux Administration
- ✅ Navigate Linux filesystem
- ✅ Manage file permissions and ownership
- ✅ Use command-line text editors (nano)
- ✅ Monitor logs in real-time

### DevOps Practices
- ✅ Deploy static websites
- ✅ Test and validate configurations
- ✅ Debug with access and error logs
- ✅ Follow infrastructure-as-code principles

---

## 📦 Prerequisites

### Required

- **AWS Account** (Free tier eligible)
  - Sign up at [aws.amazon.com](https://aws.amazon.com)
  - No charges for free tier usage
  - Credit card required for verification

### Helpful (But Not Required)

- Basic HTML knowledge
- Familiarity with command-line interfaces
- Text editor experience


| Phase | What You'll Do |
|-------|----------------|
| **Phase 1** |AWS EC2 setup and infrastructure |
| **Phase 2** |NGINX installation and configuration |


---

## ⚡ Quick Start

### 1️⃣ Launch EC2 Instance

```bash
AWS Console → EC2 → Launch Instance
- AMI: Amazon Linux 2 (Free tier)
- Type: t2.micro (1 vCPU, 1GB RAM)
- Security Groups: SSH (22), HTTP (80), HTTPS (443)
```

### 2️⃣ Connect to Your Server

```bash
# Via AWS Console (Easiest)
EC2 Dashboard → Select Instance → Connect → EC2 Instance Connect

# Or via SSH
ssh -i "nginx-server-key.pem" ec2-user@YOUR_SERVER_IP
```

### 3️⃣ Install NGINX

```bash
# Update system
sudo yum update -y

# Install NGINX
sudo yum install nginx -y

# Start and enable NGINX
sudo systemctl start nginx
sudo systemctl enable nginx

# Verify it's running
sudo systemctl status nginx
```

### 4️⃣ Test Your Web Server

Open browser and navigate to:
```
http://YOUR_SERVER_IP
```

✅ **You should see the NGINX welcome page!**

### 5️⃣ Deploy Your Custom Site

```bash
# Create website directory
sudo mkdir -p /usr/share/nginx/html/mywebsite

# Create HTML file
sudo nano /usr/share/nginx/html/mywebsite/index.html
# (Add your HTML content and save with Ctrl+X, Y, Enter)

# Update NGINX config
sudo nano /etc/nginx/nginx.conf
# Change: root /usr/share/nginx/html/mywebsite;

# Test and reload
sudo nginx -t
sudo systemctl reload nginx
```

🎉 **Your website is now live!**

---

## 🏗️ Phase 1: Infrastructure Setup

### Step 1: Launch AWS EC2 Instance (15 minutes)

#### 1.1 Access AWS Console

1. Navigate to [aws.amazon.com](https://aws.amazon.com)
2. Sign in to AWS Console
3. Select your preferred region (e.g., "US East (N. Virginia)")

#### 1.2 Launch Instance

1. Search for **"EC2"** in AWS Console
2. Click **"Launch Instance"** button

#### 1.3 Configure Your Instance

**Name and OS:**
```
Name: nginx-web-server
AMI: Amazon Linux 2 AMI (HVM) - Free tier eligible
```

**Instance Type:**
```
Type: t2.micro (1 vCPU, 1 GB RAM)
Status: Free tier eligible ✅
```

**Key Pair (Critical for SSH Access):**
```
Action: Create new key pair
Name: nginx-server-key
Type: RSA
Format: .pem (Mac/Linux) or .ppk (Windows)

⚠️ IMPORTANT: Save this file securely!
```

**Network Settings:**

Create security group: `nginx-webserver-sg`

| Rule | Type | Port | Source | Purpose |
|------|------|------|--------|---------|
| 1 | SSH | 22 | My IP | Server management |
| 2 | HTTP | 80 | Anywhere (0.0.0.0/0) | Web traffic |
| 3 | HTTPS | 443 | Anywhere (0.0.0.0/0) | Secure web traffic |

**Storage:**
```
Size: 8 GB gp2 (default)
Status: Free tier eligible ✅
```

#### 1.4 Launch

1. Review settings in **Summary** panel
2. Click **"Launch instance"**
3. Wait 1-2 minutes for initialization
4. Click **"View all instances"**

#### 1.5 Note Your Instance Details

Once running (Status: `2/2 checks passed`):

```bash
# Find your Public IPv4 address
Example: 54.123.45.67

# Save this - you'll use it throughout the guide
```

**✅ Phase 1 Complete!** You now have a running cloud server.

---

## 💻 Phase 2: NGINX Installation & Configuration

### Step 2: Connect to Your EC2 Instance (5 minutes)

#### Method 1: AWS Console (Recommended)

1. EC2 Dashboard → Select instance (checkbox)
2. Click **"Connect"** button
3. Go to **"EC2 Instance Connect"** tab
4. Username: `ec2-user`
5. Click **"Connect"**

✅ A terminal opens in your browser!

#### Method 2: SSH from Local Machine

**Mac/Linux:**
```bash
chmod 400 nginx-server-key.pem
ssh -i "nginx-server-key.pem" ec2-user@YOUR_SERVER_IP
```

**Windows (Git Bash/WSL):**
```bash
ssh -i "nginx-server-key.pem" ec2-user@YOUR_SERVER_IP
```

---

### Step 3: Install and Start NGINX (10 minutes)

#### 3.1 Update System Packages

```bash
sudo yum update -y
```
*Updates all system packages (~1-2 minutes)*

#### 3.2 Install NGINX

```bash
sudo yum install nginx -y
```
*Downloads and installs NGINX (~30 seconds)*

#### 3.3 Start NGINX Service

```bash
# Start NGINX immediately
sudo systemctl start nginx

# Enable auto-start on boot
sudo systemctl enable nginx

# Check status
sudo systemctl status nginx
```

**Expected Output:**
```
● nginx.service - The nginx HTTP and reverse proxy server
   Loaded: loaded (/usr/lib/systemd/system/nginx.service; enabled)
   Active: active (running) since [date/time]
```

Look for: `Active: active (running)` in green

Press `q` to exit status view.

#### 3.4 Test Your Web Server

1. Open web browser
2. Navigate to: `http://YOUR_SERVER_IP`
3. You should see: **"Welcome to nginx!"**

🎉 **Congratulations! Your web server is running!**

---

### Step 4: Understand NGINX Configuration (15 minutes)

#### 4.1 NGINX Configuration Hierarchy

The `/etc/nginx/nginx.conf` file follows a clear structure:

```
events → http → server → location
```

This nested structure makes NGINX powerful and flexible:

| Block | Responsibility |
|-------|---------------|
| `events` | Connection handling (worker processes, concurrency) |
| `http` | HTTP-level settings (logging, compression, MIME types) |
| `server` | Virtual host configuration (website or domain) |
| `location` | URL routing and request processing logic |

#### 4.2 View Configuration File

```bash
cat /etc/nginx/nginx.conf
```

**Key sections:**

```nginx
user nginx;                          # User NGINX runs as
worker_processes auto;               # Number of worker processes

events {
    worker_connections 1024;         # Max connections per worker
}

http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;
    
    server {
        listen       80;             # Port NGINX listens on
        server_name  _;              # Server name (default catch-all)
        root         /usr/share/nginx/html;  # Website files location
        
        location / {
            # Request handling logic
        }
    }
}
```

#### 4.3 Test Configuration Syntax

```bash
sudo nginx -t
```

**Expected output:**
```
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

✅ Always run this before reloading NGINX!

---

### Step 5: Host Your First Custom Page (15 minutes)

#### 5.1 Clean Up Default Files

```bash
sudo rm -rf /usr/share/nginx/html/*
```

#### 5.2 Create Website Directory

```bash
sudo mkdir -p /usr/share/nginx/html/mywebsite
```

#### 5.3 Create HTML File

```bash
sudo nano /usr/share/nginx/html/mywebsite/index.html
```

**Paste this HTML:**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My First NGINX Site</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-align: center;
        }
        h1 {
            font-size: 3em;
            margin-bottom: 20px;
        }
        p {
            font-size: 1.2em;
            line-height: 1.6;
        }
        .container {
            background: rgba(255, 255, 255, 0.1);
            padding: 40px;
            border-radius: 10px;
            backdrop-filter: blur(10px);
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 Hello from NGINX!</h1>
        <p>Welcome to my custom web server</p>
        <p>This page is served by NGINX on AWS EC2</p>
        <p><strong>Server IP:</strong> YOUR_SERVER_IP_HERE</p>
    </div>
</body>
</html>
```

**Save the file:**
- Press `Ctrl + X`
- Press `Y` (confirm)
- Press `Enter`

#### 5.4 Set Permissions

```bash
sudo chown -R ec2-user:ec2-user /usr/share/nginx/html
```

#### 5.5 Update NGINX Configuration

```bash
sudo nano /etc/nginx/nginx.conf
```

**Find this section (around line 40):**

```nginx
server {
    listen       80;
    listen       [::]:80;
    server_name  _;
    root         /usr/share/nginx/html;  # OLD LINE
    
    include /etc/nginx/default.d/*.conf;
    
    location / {
    }
}
```

**Change to:**

```nginx
server {
    listen       80;
    listen       [::]:80;
    server_name  _;
    root         /usr/share/nginx/html/mywebsite;  # NEW LINE
    
    include /etc/nginx/default.d/*.conf;
    
    location / {
        try_files $uri $uri/ =404;  # ADD THIS LINE
    }
}
```

**Save:** `Ctrl + X` → `Y` → `Enter`

#### 5.6 Test and Reload

```bash
# Test configuration
sudo nginx -t

# If test passes, reload NGINX
sudo systemctl reload nginx
```

#### 5.7 View Your Website

1. Open browser
2. Navigate to: `http://YOUR_SERVER_IP`
3. See your custom purple gradient page! 🎨

🎉 **You've deployed a custom website!**

---

### Step 6: Change Default HTTP Port (Optional)

#### 6.1 Edit Configuration

```bash
sudo nano /etc/nginx/nginx.conf
```

**Change port:**

```nginx
# FROM:
listen       80;
listen       [::]:80;

# TO:
listen       8080;
listen       [::]:8080;
```

**Save:** `Ctrl + X` → `Y` → `Enter`

#### 6.2 Update AWS Security Group

1. AWS Console → EC2 → Security Groups
2. Select `nginx-webserver-sg`
3. Edit inbound rules → Add rule:
   - Type: Custom TCP
   - Port: 8080
   - Source: Anywhere-IPv4 (0.0.0.0/0)
4. Save rules

#### 6.3 Reload NGINX

```bash
sudo nginx -t
sudo systemctl reload nginx
```

#### 6.4 Test New Port

Browser: `http://YOUR_SERVER_IP:8080`

**To revert to port 80:**
```bash
# Edit nginx.conf and change 8080 back to 80
sudo nano /etc/nginx/nginx.conf
sudo nginx -t
sudo systemctl reload nginx
```

---

### Step 7: Configure and View NGINX Logs (10 minutes)

#### 7.1 Log File Locations

```bash
# Access logs (all HTTP requests)
/var/log/nginx/access.log

# Error logs (problems and errors)
/var/log/nginx/error.log
```

#### 7.2 View Logs in Real-Time

```bash
# Monitor access logs
sudo tail -f /var/log/nginx/access.log

# Monitor error logs
sudo tail -f /var/log/nginx/error.log
```

Press `Ctrl + C` to stop monitoring

#### 7.3 View Recent Logs

```bash
# Last 20 access log entries
sudo tail -n 20 /var/log/nginx/access.log

# Last 10 error log entries
sudo tail -n 10 /var/log/nginx/error.log
```

#### 7.4 Understanding Access Log Format

**Example log entry:**
```
54.123.45.67 - - [14/Feb/2026:10:30:45 +0000] "GET / HTTP/1.1" 200 512
```

**What it means:**

| Field | Value | Description |
|-------|-------|-------------|
| IP | 54.123.45.67 | Visitor's IP address |
| Timestamp | 14/Feb/2026:10:30:45 | When request was made |
| Method | GET | HTTP method |
| Path | / | Requested URL path |
| Status | 200 | HTTP status code (200 = success) |
| Size | 512 | Response size in bytes |

#### 7.5 Test 404 Error Logging

```bash
# In browser, visit:
# http://YOUR_SERVER_IP/this-page-does-not-exist

# Check error log:
sudo tail /var/log/nginx/error.log
```

You should see a "404 Not Found" entry.

---

## ✅ Phase 2 Complete!

### What You've Accomplished:

- ✅ Running EC2 instance in AWS cloud
- ✅ NGINX installed and configured
- ✅ Custom website hosted and accessible
- ✅ Understanding of NGINX configuration structure
- ✅ Knowledge of essential NGINX commands
- ✅ Log monitoring and analysis skills

**These are production-ready DevOps skills used by professionals worldwide!**

---

## 📖 Understanding NGINX Configuration

### Configuration Hierarchy

```nginx
# Global context
user nginx;
worker_processes auto;
error_log /var/log/nginx/error.log;

# Events context - Connection processing
events {
    worker_connections 1024;
    use epoll;
}

# HTTP context - Web server settings
http {
    include /etc/nginx/mime.types;
    default_type application/octet-stream;
    
    access_log /var/log/nginx/access.log;
    
    # Server context - Virtual host
    server {
        listen 80;
        server_name example.com;
        root /usr/share/nginx/html;
        
        # Location context - URL routing
        location / {
            try_files $uri $uri/ =404;
        }
        
        location /api {
            proxy_pass http://backend:8080;
        }
    }
}
```

### Key Directives Explained

| Directive | Context | Purpose |
|-----------|---------|---------|
| `user` | Global | User NGINX runs as (security) |
| `worker_processes` | Global | Number of worker processes |
| `worker_connections` | Events | Max connections per worker |
| `listen` | Server | Port and IP to listen on |
| `server_name` | Server | Domain name matching |
| `root` | Server/Location | Document root directory |
| `try_files` | Location | File lookup order |
| `proxy_pass` | Location | Reverse proxy configuration |

---

## 🔧 Common Commands

### NGINX Service Management

```bash
# Start NGINX
sudo systemctl start nginx

# Stop NGINX
sudo systemctl stop nginx

# Restart NGINX (full restart with downtime)
sudo systemctl restart nginx

# Reload configuration (zero downtime)
sudo systemctl reload nginx

# Check status
sudo systemctl status nginx

# Enable auto-start on boot
sudo systemctl enable nginx
```

### Configuration Testing

```bash
# Test configuration syntax
sudo nginx -t

# Test and show configuration
sudo nginx -T

# Safe reload (test first, then reload)
sudo nginx -t && sudo systemctl reload nginx
```

### Log Management

```bash
# View access logs (last 50 lines)
sudo tail -n 50 /var/log/nginx/access.log

# Follow access logs in real-time
sudo tail -f /var/log/nginx/access.log

# View error logs
sudo tail -n 50 /var/log/nginx/error.log

# Follow error logs in real-time
sudo tail -f /var/log/nginx/error.log

# Search logs for specific IP
grep "54.123.45.67" /var/log/nginx/access.log

# Count requests by status code
awk '{print $9}' /var/log/nginx/access.log | sort | uniq -c
```

### File and Directory Management

```bash
# Navigate to web root
cd /usr/share/nginx/html

# List files with details
ls -lah

# Create directory
sudo mkdir -p /usr/share/nginx/html/newsite

# Edit file
sudo nano /usr/share/nginx/html/index.html

# Set ownership
sudo chown -R ec2-user:ec2-user /usr/share/nginx/html

# Set permissions (directories: 755, files: 644)
sudo find /usr/share/nginx/html -type d -exec chmod 755 {} \;
sudo find /usr/share/nginx/html -type f -exec chmod 644 {} \;
```

### System Information

```bash
# Check NGINX version
nginx -v

# Check server public IP
curl ifconfig.me

# Check running processes
ps aux | grep nginx

# Check listening ports
sudo netstat -tulpn | grep nginx

# Check disk space
df -h

# Check memory usage
free -h
```

---

## 🐛 Troubleshooting

### Issue 1: Can't Access Website

**Symptoms:** Browser shows "This site can't be reached"

**Solutions:**

```bash
# 1. Check if NGINX is running
sudo systemctl status nginx

# 2. Start NGINX if stopped
sudo systemctl start nginx

# 3. Check security group allows port 80
# AWS Console → EC2 → Security Groups → Edit inbound rules

# 4. Verify server IP
curl ifconfig.me

# 5. Test locally on server
curl localhost
```

---

### Issue 2: 403 Forbidden Error

**Symptoms:** Browser shows "403 Forbidden"

**Solutions:**

```bash
# Fix permissions
sudo chmod -R 755 /usr/share/nginx/html
sudo chown -R nginx:nginx /usr/share/nginx/html

# Verify index file exists
ls -la /usr/share/nginx/html/index.html

# Check NGINX error log
sudo tail -20 /var/log/nginx/error.log
```

---

### Issue 3: Configuration Test Fails

**Symptoms:** `sudo nginx -t` shows errors

**Solutions:**

```bash
# View the exact error
sudo nginx -t

# Restore from backup if needed
sudo cp /etc/nginx/nginx.conf.backup /etc/nginx/nginx.conf

# Validate before reload
sudo nginx -t && sudo systemctl reload nginx
```

---

### Issue 4: Changes Not Showing

**Symptoms:** Website shows old content after updates

**Solutions:**

```bash
# 1. Hard refresh browser
# Chrome/Firefox: Ctrl + Shift + R (Windows/Linux)
# Chrome/Firefox: Cmd + Shift + R (Mac)

# 2. Reload NGINX
sudo systemctl reload nginx

# 3. Test with curl (bypasses cache)
curl http://YOUR_SERVER_IP

# 4. Verify file was saved
cat /usr/share/nginx/html/index.html
```

---

## 🚀 Next Steps

### Beginner Level

- [ ] Customize your HTML/CSS design
- [ ] Add multiple pages with navigation
- [ ] Upload images and media files
- [ ] Create a portfolio website

### Intermediate Level

- [ ] **Set up Virtual Hosts** - Host multiple websites
- [ ] **Configure SSL/HTTPS** - Secure your site with Let's Encrypt
- [ ] **Custom Domain** - Use your own domain name
- [ ] **Custom Error Pages** - Create branded 404/500 pages
- [ ] **Basic Authentication** - Password protect sections

### Advanced Level

- [ ] **Reverse Proxy** - Proxy to backend applications
- [ ] **Load Balancing** - Distribute traffic across servers
- [ ] **Caching** - Implement caching strategies
- [ ] **Rate Limiting** - Prevent abuse and DDoS
- [ ] **Monitoring** - Set up CloudWatch or custom monitoring

---

## 📚 Learning Resources

### Official Documentation

- [NGINX Official Docs](https://nginx.org/en/docs/)
- [AWS EC2 Documentation](https://docs.aws.amazon.com/ec2/)
- [Amazon Linux 2 User Guide](https://docs.aws.amazon.com/linux/)

### Tools & Utilities

- [NGINX Config Generator](https://nginxconfig.io/) - Interactive config builder
- [SSL Labs Server Test](https://www.ssllabs.com/ssltest/) - Test SSL configuration
- [Let's Encrypt](https://letsencrypt.org/) - Free SSL certificates

