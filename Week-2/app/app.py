
from flask import Flask, render_template_string
app = Flask(__name__)
TEMPLATE = """ 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kajal - AWS DevOps Engineer Portfolio</title>
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='0.9em' font-size='90'>☁️</text></svg>">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        :root {
            --bg-primary: #ffffff;
            --bg-secondary: #f8f9fa;
            --bg-card: #ffffff;
            --text-primary: #1a1a1a;
            --text-secondary: #666666;
            --accent: #FF9900;
            --accent-hover: #cc7a00;
            --border: #e0e0e0;
            --shadow: rgba(0, 0, 0, 0.1);
            --code-bg: #f4f4f4;
        }
        [data-theme="dark"] {
            --bg-primary: #0f1419;
            --bg-secondary: #1a1f2e;
            --bg-card: #232940;
            --text-primary: #e6e6e6;
            --text-secondary: #a8a8a8;
            --accent: #FF9900;
            --accent-hover: #ffad33;
            --border: #2d3748;
            --shadow: rgba(0, 0, 0, 0.3);
            --code-bg: #1a1f2e;
        }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.6;
            color: var(--text-primary);
            background-color: var(--bg-primary);
            transition: background-color 0.3s ease, color 0.3s ease;
        }
        nav {
            background-color: var(--bg-card);
            box-shadow: 0 2px 10px var(--shadow);
            position: sticky;
            top: 0;
            z-index: 1000;
            transition: background-color 0.3s ease;
        }
        .nav-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 1rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .logo {
            font-size: 1.5rem;
            font-weight: 700;
            color: var(--accent);
            font-family: 'Courier New', monospace;
            transition: all 0.3s ease;
            cursor: pointer;
        }
        .logo::after {
            content: '_';
            animation: blink 1s infinite;
        }
        .logo:hover {
            text-shadow: 0 0 20px var(--accent), 0 0 30px var(--accent);
            transform: scale(1.05);
        }
        @keyframes blink {
            0%, 50% {
                opacity: 1;
            }
            51%, 100% {
                opacity: 0;
            }
        }
        .nav-links {
            display: flex;
            gap: 2rem;
            list-style: none;
            align-items: center;
        }
        .nav-links a {
            color: var(--text-primary);
            text-decoration: none;
            font-weight: 500;
            transition: color 0.3s ease;
        }
        .nav-links a:hover {
            color: var(--accent);
        }
        .theme-toggle {
            background: var(--bg-secondary);
            border: 2px solid var(--border);
            border-radius: 50px;
            width: 60px;
            height: 30px;
            cursor: pointer;
            position: relative;
            transition: all 0.3s ease;
        }
        .theme-toggle::before {
            content: '🌙';
            position: absolute;
            top: 2px;
            left: 4px;
            font-size: 18px;
            transition: all 0.3s ease;
        }
        [data-theme="dark"] .theme-toggle::before {
            content: '☀️';
            left: 32px;
        }
        .hero {
            background: linear-gradient(135deg, var(--bg-secondary) 0%, var(--bg-card) 100%);
            padding: 6rem 2rem;
            text-align: center;
        }
        .hero-content {
            max-width: 800px;
            margin: 0 auto;
        }
        .hero h1 {
            font-size: 3rem;
            margin-bottom: 1rem;
            color: var(--text-primary);
        }
        .hero .tagline {
            font-size: 1.5rem;
            color: var(--accent);
            margin-bottom: 1rem;
        }
        .hero .subtitle {
            font-size: 1.1rem;
            color: var(--text-secondary);
            margin-bottom: 2rem;
        }
        .cta-buttons {
            display: flex;
            gap: 1rem;
            justify-content: center;
            flex-wrap: wrap;
        }
        .btn {
            padding: 0.8rem 2rem;
            border-radius: 8px;
            text-decoration: none;
            font-weight: 600;
            transition: all 0.3s ease;
            display: inline-block;
        }
        .btn-primary {
            background-color: var(--accent);
            color: white;
        }
        .btn-primary:hover {
            background-color: var(--accent-hover);
            transform: translateY(-2px);
            box-shadow: 0 4px 12px var(--shadow);
        }
        .btn-secondary {
            background-color: transparent;
            color: var(--text-primary);
            border: 2px solid var(--border);
        }
        .btn-secondary:hover {
            border-color: var(--accent);
            color: var(--accent);
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 4rem 2rem;
        }
        .section-title {
            text-align: center;
            margin-bottom: 3rem;
        }
        .section-title h2 {
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
            color: var(--text-primary);
        }
        .section-title .underline {
            width: 80px;
            height: 4px;
            background: var(--accent);
            margin: 0 auto;
        }
        .about-content {
            max-width: 800px;
            margin: 0 auto;
        }
        .about-text p {
            margin-bottom: 1rem;
            color: var(--text-secondary);
        }
        .skills-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
        }
        .skill-category {
            background: var(--bg-card);
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 4px 6px var(--shadow);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .skill-category:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 15px var(--shadow);
        }
        .skill-category h3 {
            color: var(--accent);
            margin-bottom: 1.5rem;
            font-size: 1.3rem;
        }
        .skill-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
        }
        .skill-tag {
            background: var(--bg-secondary);
            color: var(--text-primary);
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-size: 0.9rem;
            border: 1px solid var(--border);
        }
        .projects-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 2rem;
        }
        .project-card {
            background: var(--bg-card);
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 4px 6px var(--shadow);
            transition: all 0.3s ease;
        }
        .project-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 12px 20px var(--shadow);
        }
        .project-header {
            background: linear-gradient(135deg, var(--accent) 0%, var(--accent-hover) 100%);
            color: white;
            padding: 1.5rem;
        }
        .project-header h3 {
            margin-bottom: 0.5rem;
        }
        .project-type {
            font-size: 0.9rem;
            opacity: 0.9;
        }
        .project-body {
            padding: 1.5rem;
        }
        .project-description {
            color: var(--text-secondary);
            margin-bottom: 1rem;
        }
        .tech-stack {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-bottom: 1rem;
        }
        .tech-badge {
            background: var(--code-bg);
            color: var(--text-primary);
            padding: 0.3rem 0.8rem;
            border-radius: 4px;
            font-size: 0.85rem;
            font-family: 'Courier New', monospace;
        }
        .project-metrics {
            background: var(--bg-secondary);
            padding: 1rem;
            border-radius: 8px;
            margin-bottom: 1rem;
        }
        .metric {
            display: flex;
            justify-content: space-between;
            margin-bottom: 0.5rem;
            color: var(--text-secondary);
            font-size: 0.9rem;
        }
        .metric:last-child {
            margin-bottom: 0;
        }
        .metric-value {
            color: var(--accent);
            font-weight: 600;
        }
        .project-links {
            display: flex;
            gap: 1rem;
        }
        .project-link {
            flex: 1;
            text-align: center;
            padding: 0.6rem;
            background: var(--bg-secondary);
            color: var(--text-primary);
            text-decoration: none;
            border-radius: 6px;
            font-weight: 500;
            transition: all 0.3s ease;
        }
        .project-link:hover {
            background: var(--accent);
            color: white;
        }
        .contact-content {
            max-width: 800px;
            margin: 0 auto;
            text-align: center;
        }
        .contact-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            margin-top: 2rem;
        }
        .contact-item {
            background: var(--bg-card);
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 4px 6px var(--shadow);
            transition: all 0.3s ease;
        }
        .contact-item:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 15px var(--shadow);
        }
        .contact-icon {
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }
        .contact-item h3 {
            color: var(--text-primary);
            margin-bottom: 0.5rem;
        }
        .contact-item a {
            color: var(--accent);
            text-decoration: none;
            font-weight: 500;
        }
        .contact-item a:hover {
            text-decoration: underline;
        }
        footer {
            background: var(--bg-card);
            padding: 2rem;
            text-align: center;
            border-top: 1px solid var(--border);
            color: var(--text-secondary);
        }
        @media (max-width: 768px) {
            .hero h1 {
                font-size: 2rem;
            }
            .hero .tagline {
                font-size: 1.2rem;
            }
            .nav-links {
                gap: 1rem;
            }
            .projects-grid {
                grid-template-columns: 1fr;
            }
            .container {
                padding: 2rem 1rem;
            }
        }
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        .fade-in {
            animation: fadeInUp 0.6s ease-out;
        }
    </style>
</head>
<body>
    <nav>
        <div class="nav-container">
            <div class="logo">$kajal</div>
            <ul class="nav-links">
                <li><a href="#about">About</a></li>
                <li><a href="#skills">Skills</a></li>
                <li><a href="#projects">Projects</a></li>
                <li><a href="#contact">Contact</a></li>
                <li><button class="theme-toggle" onclick="toggleTheme()" aria-label="Toggle dark mode"></button></li>
            </ul>
        </div>
    </nav>
    <section class="hero">
        <div class="hero-content fade-in">
            <h1>Hi, I'm Kajal</h1>
            <p class="tagline">AWS DevOps Engineer</p>
            <p class="subtitle">Building scalable cloud infrastructure and automating workflows.</p>
            <div class="cta-buttons">
                <a href="#projects" class="btn btn-primary">View My Work</a>
                <a href="#contact" class="btn btn-secondary">Get in Touch</a>
            </div>
        </div>
    </section>
    <section id="about" class="container">
        <div class="section-title">
            <h2>About Me</h2>
            <div class="underline"></div>
        </div>
        <div class="about-content">
    <div class="about-text">
        <p>Hi, I'm a DevOps Engineer with hands-on experience in AWS cloud infrastructure, automation, and CI/CD pipelines. I focus on building reliable, scalable systems by connecting development and operations seamlessly.</p>
        
        <p>I enjoy solving complex problems, improving deployment workflows, and applying infrastructure-as-code and automation-first practices to create maintainable cloud solutions.</p>
        
        <p>Outside of work, I explore new DevOps tools, write technical content, and contribute to open-source projects.</p>
    </div>
</div>
    </section>
    <section id="skills" class="container" style="background: var(--bg-secondary);">
        <div class="section-title">
            <h2>Technical Skills</h2>
            <div class="underline"></div>
        </div>
        <div class="skills-grid">
            <div class="skill-category">
                <h3>Cloud Platforms</h3>
                <div class="skill-tags">
                    <span class="skill-tag">AWS (EC2, S3, RDS)</span>
                    <span class="skill-tag">Lambda</span>
                    <span class="skill-tag">CloudFormation</span>
                    <span class="skill-tag">Route 53</span>
                    <span class="skill-tag">VPC</span>
                    <span class="skill-tag">IAM</span>
                </div>
            </div>
            <div class="skill-category">
                <h3>Containers & Orchestration</h3>
                <div class="skill-tags">
                    <span class="skill-tag">Docker</span>
                    <span class="skill-tag">Kubernetes</span>
                    <span class="skill-tag">ECS/EKS</span>
                    <span class="skill-tag">Docker Compose</span>
                </div>
            </div>
            <div class="skill-category">
                <h3>Infrastructure as Code</h3>
                <div class="skill-tags">
                    <span class="skill-tag">Terraform</span>
                    <span class="skill-tag">Ansible</span>
                    <span class="skill-tag">CloudFormation</span>
                    <span class="skill-tag">Packer</span>
                </div>
            </div>
            <div class="skill-category">
                <h3>CI/CD</h3>
                <div class="skill-tags">
                    <span class="skill-tag">GitHub Actions</span>
                    <span class="skill-tag">ArgoCD</span>
                    <span class="skill-tag">CodePipeline</span>
                </div>
            </div>
            <div class="skill-category">
                <h3>Monitoring & Logging</h3>
                <div class="skill-tags">
                    <span class="skill-tag">Prometheus</span>
                    <span class="skill-tag">Grafana</span>
                    <span class="skill-tag">ELK Stack</span>
                    <span class="skill-tag">CloudWatch</span>
                
                </div>
            </div>
            <div class="skill-category">
                <h3>Programming & Scripting</h3>
                <div class="skill-tags">
                    <span class="skill-tag">Python</span>
                    <span class="skill-tag">Bash</span>
                    <span class="skill-tag">YAML</span>
                    <span class="skill-tag">Git</span>
                </div>
            </div>
        </div>
    </section>
    <section id="projects" class="container" style="background: var(--bg-secondary);">
        <div class="section-title">
            <h2>Featured Projects</h2>
            <div class="underline"></div>
        </div>
        <div class="projects-grid">
            <div class="project-card">
                <div class="project-header">
                    <h3>AWS 3-Tier Web Application</h3>
                    <p class="project-type">Cloud Architecture</p>
                </div>
                <div class="project-body">
                    <p class="project-description">
                        Designed and deployed a highly available, scalable 3-tier architecture using AWS best practices. Implemented auto-scaling, load balancing, and multi-AZ deployment for maximum reliability.
                    </p>
                    <div class="tech-stack">
                        <span class="tech-badge">AWS</span>
                        <span class="tech-badge">EC2</span>
                        <span class="tech-badge">RDS</span>
                        <span class="tech-badge">ALB</span>
                        <span class="tech-badge">Auto Scaling</span>
                        <span class="tech-badge">CloudWatch</span>
                    </div>
                    <div class="project-links">
                        <a href="#" class="project-link">GitHub</a>
                    </div>
                </div>
            </div>
            <div class="project-card">
                <div class="project-header">
                    <h3>Kubernetes CI/CD Pipeline</h3>
                    <p class="project-type">DevOps Automation</p>
                </div>
                <div class="project-body">
                    <p class="project-description">
                        Built an end-to-end CI/CD pipeline for containerized microservices using Jenkins, Docker, and Kubernetes. Automated testing, building, and deployment with zero-downtime releases.
                    </p>
                    <div class="tech-stack">
                        
                        <span class="tech-badge">Docker</span>
                        <span class="tech-badge">Kubernetes</span>
                        <span class="tech-badge">Helm</span>
                        <span class="tech-badge">ArgoCD</span>
                        <span class="tech-badge">GitHub</span>
                    </div>
                
                    <div class="project-links">
                        <a href="#" class="project-link">GitHub</a>
                    </div>
                </div>
            </div>
            <div class="project-card">
                <div class="project-header">
                    <h3>Infrastructure as Code (IaC)</h3>
                    <p class="project-type">Terraform & Automation</p>
                </div>
                <div class="project-body">
                    <p class="project-description">
                        Automated complete infrastructure provisioning using Terraform modules. Created reusable, version-controlled infrastructure with proper state management and environment separation.
                    </p>
                    <div class="tech-stack">
                        <span class="tech-badge">Terraform</span>
                        <span class="tech-badge">AWS</span>
                        <span class="tech-badge">S3</span>
                        <span class="tech-badge">DynamoDB</span>
                        <span class="tech-badge">GitHub Actions</span>
                    </div>
                    
                    <div class="project-links">
                        <a href="#" class="project-link">GitHub</a>
                    </div>
                </div>
            </div>
            
    </section>
    <section id="contact" class="container">
        <div class="section-title">
            <h2>Let's Connect</h2>
            <div class="underline"></div>
        </div>
        <div class="contact-content">
            <p style="color: var(--text-secondary); margin-bottom: 2rem; font-size: 1.1rem;">
                I'm always open to discussing new projects, opportunities, or collaborations. 
                Feel free to reach out through any of these channels!
            </p>
            <div class="contact-grid">
                <div class="contact-item">
                    <div class="contact-icon">📝</div>
                    <h3>Medium</h3>
                    <a href="https://medium.com/@k" target="_blank">medium.com/@yourusername</a> 
                </div>
                <div class="contact-item">
                    <div class="contact-icon">💼</div>
                    <h3>LinkedIn</h3>
                    <a href="www.linkedin.com/in/k" target="_blank">linkedin.com/in/yourprofile</a> 
                </div>
                <div class="contact-item">
                    <div class="contact-icon">💻</div>
                    <h3>GitHub</h3>
                    <a href="https://github.com/" target="_blank">github.com/yourusername</a> 
                </div>
            </div>
        </div>
    </section>
    <footer>
        <p>&copy; 2026 Kajal | DevOps Portfolio | Built with passion for automation</p>
    </footer>
    <script>
        function toggleTheme() {
            const html = document.documentElement;
            const currentTheme = html.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            html.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
        }
        document.addEventListener('DOMContentLoaded', () => {
            const savedTheme = localStorage.getItem('theme') || 'light';
            document.documentElement.setAttribute('data-theme', savedTheme);
        });
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('fade-in');
                }
            });
        }, observerOptions);
        document.querySelectorAll('.project-card, .skill-category, .contact-item').forEach(el => {
            observer.observe(el);
        });
    </script>
</body>
</html>
<!-- """
@app.route("/")
def index():
    return render_template_string(TEMPLATE)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True) 