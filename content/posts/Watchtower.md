---
creation date: 2025-01-29 18:59
tags: 

- HomeLab
---

**Watchtower** is a Docker container that automatically updates your running containers when new versions of their images are available. It monitors your Docker containers, checks for updated images on the configured registries (e.g., Docker Hub), pulls the updated image, and restarts the container with the new version.

---

### Key Features of Watchtower:

1. **Automatic Updates**:
    
    - It checks for updates to the images of your running containers at regular intervals.
    - If an update is available, it pulls the new image, stops the old container, and starts a new container with the updated image.
2. **Minimal Configuration**:
    
    - Works with your existing `docker-compose.yml` or manually created containers.
    - Automatically inherits volumes, ports, and other settings from the old container.
3. **Customizable Update Behavior**:
    
    - You can control how frequently it checks for updates.
    - Set specific containers to be excluded from updates using labels.
4. **Optional Notifications**:
    
    - It supports notifications via services like Slack, Email, PagerDuty, and more, so you’re informed when containers are updated.

---

### Why Use Watchtower?

1. **Stay Up-to-Date**: Keep your containers updated with the latest security patches and features without manual intervention.
2. **Convenience**: Saves time by automating updates, especially when running multiple containers.
3. **Lightweight**: Watchtower itself is a lightweight container with minimal resource usage.
4. **Security**: Ensures you’re running the latest, most secure versions of container images.

---

### Example Use Case

If you're running containers like **Vaultwarden** or **Homepage**, Watchtower will:

1. Periodically check for updates to their images.
2. If new versions are available:
    - Pull the updated image.
    - Restart the container using the new image, while preserving your existing configurations (volumes, ports, etc.).

---

### How to Use Watchtower

1. **Run Watchtower via Docker**:
    
    ```bash
    docker run -d \
      --name watchtower \
      -v /var/run/docker.sock:/var/run/docker.sock \
      containrrr/watchtower
    ```
    
    - The `-v /var/run/docker.sock:/var/run/docker.sock` allows Watchtower to interact with the Docker daemon to manage containers.
2. **Using Docker Compose**: Add Watchtower to your `docker-compose.yml`:
    
    ```yaml
    services:
      watchtower:
        image: containrrr/watchtower
        container_name: watchtower
        volumes:
          - /var/run/docker.sock:/var/run/docker.sock
        command: --interval 300  # Check for updates every 5 minutes
        restart: unless-stopped
    ```
    
3. **Excluding Containers**: Use labels to prevent specific containers from being updated:
    
    ```yaml
    services:
      some-service:
        image: some-image:latest
        labels:
          com.centurylinklabs.watchtower.enable: "false"
    ```
    

---

### Pros and Cons of Watchtower

#### **Pros**:

- Fully automated container updates.
- Easy to set up and configure.
- Reduces maintenance time.
- Supports notifications for update status.

#### **Cons**:

- May restart critical containers without warning unless configured properly.
- Requires trust in the upstream image updates (e.g., no breaking changes).
- Updates the entire container image, not just the application inside it.

---

### Best Practices When Using Watchtower

1. **Test Updates in Non-Production Environments**: Run Watchtower on non-critical systems to test updates before rolling them out to production.
2. **Use Image Tags Wisely**: Avoid using `latest` tags unless necessary. Use version tags to lock to specific releases (e.g., `1.2.3`).
3. **Monitor Logs**: Enable notifications or check logs periodically to ensure updates are applied correctly.
4. **Exclude Critical Containers**: Prevent Watchtower from updating containers where downtime must be tightly controlled.

---

### When Should You Use Watchtower?

Watchtower is great for **small-scale deployments** or personal/home server setups where automated updates reduce maintenance effort. However, for **large-scale production environments**, consider using tools like Kubernetes or other CI/CD pipelines that provide more granular control over updates.

