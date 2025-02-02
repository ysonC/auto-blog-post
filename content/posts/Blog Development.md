---
date: 2025-01-29
title: Blog Development
tags:
  - blog
  - HomeLab
---
## Road Map

![Image Description](/images/Pasted%20image%2020250129191000.png)
## Step 1: Obsidian

- Start writing blog in obsidian under a `post` folder

## Step 2: Hugo

- Use Hugo to turn the markdown in to website code.

### Install Go

- Download Go for Linux
	```bash
	wget https://go.dev/dl/go1.23.5.linux-arm64.tar.gz
	```
- **Remove any previous Go installation** by deleting the `/usr/local/go` folder (if it exists), then extract the archive you just downloaded into `/usr/local`, creating a fresh Go tree in `/usr/local/go`:
	```bash
	rm -rf /usr/local/go && tar -C /usr/local -xzf go1.23.5.linux-amd64.tar.gz
	```

- Add `/usr/local/go/bin` to the `PATH` environment variable.
	```bash
	export PATH=$PATH:/usr/local/go/bin
	```

### Install Hugo

- Install via package manger 
	```bash
	sudo apt install hugo
	```

### Add git to folder with Hugo theme

- Find themes from this link: [https://themes.gohugo.io/](https://themes.gohugo.io/)
    - _follow the theme instructions on how to download. The BEST option is to install as a git submodule_
- Create folder and git init it
	```bash
	git ini
	git config --global user.name "Wyson Cheng"
	git config --global user.email "wyson002@gmail.com"

	git submodule add -f https://github.com/panr/hugo-theme-terminal.git themes/terminal

	# Run hugo to build the website
	hugo
	```

- Local deploy
	```bash
	hugo server --bind 0.0.0.0 --baseURL http://10.179.5.96:1313/
	```

## Step 3: Sync posts and images

- Use rsync to sync posts from my obsidian vault to the hugo folder
	```bash
	rsync -av --delete "/srv/dev-disk-by-uuid-5d9f109b-e277-4117-973e-c7e67e8422ab/super_vault/yson/Obsidian Super Vault/posts/" "/home/yson-server/projects/myblog/content/posts/"
	```

- Use python script to copy images from vault so the website can use
```python
import os
import re
import shutil

# Paths
posts_dir = "/srv/dev-disk-by-uuid-5d9f109b-e277-4117-973e-c7e67e8422ab/super_vault/yson/Obsidian Super Vault/posts/"
attachments_dir = "/srv/dev-disk-by-uuid-5d9f109b-e277-4117-973e-c7e67e8422ab/super_vault/yson/Obsidian Super Vault/97 - Resources/"
static_images_dir = "/home/yson-server/projects/myblog/static/images"

# Step 1: Process each markdown file in the posts directory
for filename in os.listdir(posts_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(posts_dir, filename)

        with open(filepath, "r") as file:
            content = file.read()

        # Step 2: Find all image links in the format ![Image Description](/images/Pasted%20image%20...%20.png)
        images = re.findall(r'\[\[([^]]*\.png)\]\]', content)

        # Step 3: Replace image links and ensure URLs are correctly formatted
        for image in images:
            # Prepare the Markdown-compatible link with %20 replacing spaces
            markdown_image = f"![Image Description](/images/{image.replace(' ', '%20')})"
            content = content.replace(f"[[{image}]]", markdown_image)

            # Step 4: Copy the image to the Hugo static/images directory if it exists
            image_source = os.path.join(attachments_dir, image)
            if os.path.exists(image_source):
                shutil.copy(image_source, static_images_dir)

        # Step 5: Write the updated content back to the markdown file
        with open(filepath, "w") as file:
            file.write(content)

print("Markdown files processed and images copied successfully.")
```

## Step 4: Auto push to git and sync to docker 

```bash
#!/bin/bash

echo "Start syncing and processing image links in Markdown files..."
if [ ! -f "sync_blogs.py" ]; then
    echo "Python script images.py not found."
    exit 1
fi

echo "Running python script to sync blogs..."
if ! python3 sync_blogs.py; then
    echo "Failed to process image links."
    exit 1
fi

echo "Building the Hugo site..."
if ! hugo; then
    echo "Hugo build failed."
    exit 1
fi

echo "Syncing file to nginx docker..."
rsync -avz --delete public/ /home/yson-server/docker-services/nginx/blog/public

echo "Staging changes for Git..."
if git diff --quiet && git diff --cached --quiet; then
    echo "No changes to stage."
else
    git add .
fi

commit_message="New Blog Post on $(date +'%Y-%m-%d %H:%M:%S')"
if git diff --cached --quiet; then
    echo "No changes to commit."
else
    echo "Committing changes..."
    git commit -m "$commit_message"
fi

echo "Deploying to GitHub Main..."
if ! git push origin main; then
    echo "Failed to push to main branch."
    exit 1
fi
```


## Step 5: Setup docker for Nginx

- Use Portainer to deploy Nginx for the blog
```yaml
  nginx-blog:
    image: nginx:alpine
    container_name: nginx-blog
    volumes:
      - ${BASE}/nginx/blog/public:/usr/share/nginx/html
    ports:
      - "33000:80"
    restart: unless-stopped
```


## Extra

- `config.yml` for new theme: PaperMod

```yaml
baseURL: "http://10.179.5.96:33000"
title: "My Super Juicy Blog"
theme: "PaperMod"

menu:
  main:
    - name: Archive
      url: archives
      weight: 5
    - name: Tags
      url: tags/
      weight: 10
    - name: Github
      url: https://github.com/ysonC

params:
  author: "Wyson Cheng"

  homeInfoParams:
    Title: Hi there
    Content: Welcome to my blog

  socialIcons:
    - name: "github"
      url: "https://github.com/ysonC"

  ShowBreadCrumbs: true
```
