---
creation date: 2025-01-29 18:59
tags: 

- HomeLab
---
## Road Map

!![Image Description](/images/Pasted%20image%2020250129191000.png)

## Step 1 Obsidian

- Start writing blog in obsidian under a `post` folder

## Step 2 Hugo

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
	```
