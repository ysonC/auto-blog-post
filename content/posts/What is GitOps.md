---
date: 2025-02-01
title: What is GitOps
tags: 

- extra
---
## What is?

A way to mange infrastructure by using Git as the single control centre. Instead of manually setting up or updating the system, config file that describe the system is stored on Git. When these files are change, automation tools (Argo CD or Flux) will automatically update the systems to match the new config.

It makes the deployment consistent, easy to track (version control), and quick to roll back if something goes wrong.

## What are the option?

### For Kubernetes: Argo CD or Flux

|**Aspect**|**Argo CD**|**Flux CD**|
|---|---|---|
|**User Interface**|Rich, web-based dashboard with detailed visualizations for monitoring and management.|Minimal built-in UI; primarily CLI-driven with basic visual feedback.|
|**Ease of Use**|More beginner-friendly thanks to its intuitive graphical interface.|Simple and lightweight—best for teams comfortable working via the CLI and scripts.|
|**Workflow Integration**|Offers both manual and automated sync options; supports multi-cluster deployments.|Focuses on a strict Git-centric, pull-based workflow, integrating seamlessly into Git.|
|**Advanced Features**|Provides detailed status reporting, rollback capabilities, and extensive multi-cluster support.|Emphasizes simplicity and flexibility, leaving more customization to user scripts.|
|**Integration & Ecosystem**|Integrates well with various CI/CD tools and the Kubernetes ecosystem, benefiting from a large community.|Tightly integrates with Git workflows, making it ideal for environments that prefer minimal overhead.|
