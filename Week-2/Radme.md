# 🚀 Complete NGINX Setup on AWS EC2 (Production Guide + SSL)

> Deploy a production-ready NGINX web server on AWS EC2 and secure it with SSL using Certbot.

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Phase 1: Launch EC2 Infrastructure](#-phase-1--launch-ec2-infrastructure)
- [Phase 2: Install and Configure NGINX](#-phase-2--install-nginx)
- [Phase 3: Host Custom Website](#-phase-3--host-your-custom-website)
- [Phase 4: Connect Domain](#-phase-4--connect-domain-required-for-ssl)
- [Phase 5: Enable SSL with Certbot](#-phase-5--enable-ssl-with-certbot)
- [Important Files](#-important-files)
- [Common Commands](#-common-nginx-commands)
- [Troubleshooting](#-troubleshooting)
- [Cleanup](#-cleanup-avoid-aws-charges)
- [Final Architecture](#-final-architecture)

---

## 🌟 Overview

This guide walks you through:

- Launching an AWS EC2 instance
- Installing and configuring NGINX
- Hosting a custom website
- Connecting a domain
- Securing your site with HTTPS (Certbot SSL)

By the end, you'll have a **production-ready web server** running securely on AWS.

---

## 📌 Phase 1 — Launch EC2 Infrastructure

### Step 1️⃣ Launch EC2 Instance

Go to: **AWS Console → EC2 → Launch Instance**

**Configuration:**

| Setting | Value |
|---------|-------|
| AMI | Amazon Linux 2 |
| Instance Type | t2.micro (Free tier) |
| Key Pair | Create or select existing |
| Storage | 8 GB (default) |

**Security Group Rules:**

| Type | Port | Source |
|------|------|--------|
| SSH | 22 | My IP |
| HTTP | 80 | 0.0.0.0/0 |
| HTTPS | 443 | 0.0.0.0/0 |

Click **Launch Instance**.

---

### Step 2️⃣ Connect to EC2

**Using AWS Console:**

> EC2 → Select Instance → Connect → EC2 Instance Connect

**Using SSH:**

```bash
chmod 400 nginx-key.pem
ssh -i nginx-key.pem ec2-user@YOUR_PUBLIC_IP
```

---

## 📌 Phase 2 — Install NGINX

### Step 3️⃣ Update Server

```bash
sudo yum update -y
```

### Step 4️⃣ Install NGINX

```bash
sudo yum install nginx -y
```

### Step 5️⃣ Start and Enable NGINX

```bash
sudo systemctl start nginx
sudo systemctl enable nginx
sudo systemctl status nginx
```

If you see `Active: active (running)` — NGINX is running successfully ✅

### Step 6️⃣ Test in Browser

Open: `http://YOUR_PUBLIC_IP`

You should see: **Welcome to nginx!**

---

## 📌 Phase 3 — Host Your Custom Website

### Step 7️⃣ Create Website Directory

```bash
sudo mkdir -p /usr/share/nginx/html/mywebsite
```

### Step 8️⃣ Create HTML File

```bash
sudo nano /usr/share/nginx/html/mywebsite/index.html
```

Paste your HTML content and save.

### Step 9️⃣ Update NGINX Configuration

```bash
sudo nano /etc/nginx/nginx.conf
```

Find:
```nginx
root /usr/share/nginx/html;
```

Change to:
```nginx
root /usr/share/nginx/html/mywebsite;
```

Add inside the `location` block:
```nginx
location / {
    try_files $uri $uri/ =404;
}
```

### Step 🔟 Test & Reload

```bash
sudo nginx -t
sudo systemctl reload nginx
```

Visit: `http://YOUR_PUBLIC_IP` — your custom website is now live 🎉

---

## 📌 Phase 4 — Connect Domain (Required for SSL)

> ⚠️ **SSL cannot be issued for a public IP.** You must use a domain name.

### Step 1️⃣ Purchase Domain

You can use:
- [GoDaddy](https://www.godaddy.com)
- [Namecheap](https://www.namecheap.com)
- [Google Domains](https://domains.google)

### Step 2️⃣ Point Domain to EC2

In your DNS settings, create:

| Type | Name | Value |
|------|------|-------|
| A Record | @ | YOUR_PUBLIC_IP |

Wait **5–10 minutes** for DNS propagation, then test: `http://yourdomain.com`

If it loads successfully, proceed to SSL.

---

## 🔐 Phase 5 — Enable SSL with Certbot

### Step 1️⃣ Install Certbot

```bash
sudo yum install certbot python3-certbot-nginx -y
```

### Step 2️⃣ Obtain SSL Certificate

Replace with your domain:

```bash
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
```

You will be prompted for:
- Email address
- Terms agreement
- HTTP → HTTPS redirect (choose **2: Redirect**)

Certbot will automatically:
- Generate SSL certificate
- Update NGINX configuration
- Enable HTTPS
- Add HTTP → HTTPS redirect

### Step 3️⃣ Test HTTPS

Open: `https://yourdomain.com`

You should see: 🔒 **Secure connection (Green lock)**

### Step 4️⃣ Verify Auto-Renewal

```bash
sudo certbot renew --dry-run
```

If no errors appear, auto-renewal is working correctly ✅

---

## 📂 Important Files

| File | Purpose |
|------|---------|
| `/etc/nginx/nginx.conf` | Main NGINX configuration |
| `/etc/letsencrypt/live/` | SSL certificate files |
| `/var/log/nginx/access.log` | Access logs |
| `/var/log/nginx/error.log` | Error logs |

---

## 🔄 Common NGINX Commands

```bash
sudo systemctl start nginx    # Start NGINX
sudo systemctl stop nginx     # Stop NGINX
sudo systemctl restart nginx  # Restart NGINX
sudo systemctl reload nginx   # Reload config (no downtime)
sudo nginx -t                 # Test configuration syntax
```

---

## 🐛 Troubleshooting

**If SSL fails, check:**

```bash
sudo nginx -t
sudo systemctl status nginx
sudo tail -50 /var/log/nginx/error.log
```

**Common issues:**

- DNS not yet propagated
- Port 80 blocked in Security Group
- Incorrect domain name in Certbot command

---

## 🧹 Cleanup (Avoid AWS Charges)

To prevent unexpected charges:

1. EC2 → **Terminate Instance**
2. **Release Elastic IP** (if used)
3. **Delete Security Group** (optional)

---

## ✅ Final Architecture

**Without SSL:**
```
User → Domain → NGINX (EC2) → HTML Website
```

**With SSL:**
```
User → HTTPS (443) → NGINX + Certbot → Website
```

---

# 📸 Screenshots

## 🛠 Installation

![Installation](./Output/1.png)

---

## 🌐 Test Your Web Server

Open your browser and navigate to:

http://YOUR_PUBLIC_IP

![Testing](./Output/2.png)

---

## 📂 Application Files

![App File](./Output/3.png)

---

## 🔐 Enable SSL with Certbot

![Certbot](./Output/4.png)

---

## 🔒 HTTPS Working (Green Padlock)

![HTTPS](./Output/6.png)

---

## 🖥 NGINX Running

![NGINX](./Output/7.png)

---


---

*Built with ❤️ on AWS EC2 + NGINX + Let's Encrypt*


---


