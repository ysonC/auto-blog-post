import os
import re
import shutil

# Paths
posts_dir = "/srv/dev-disk-by-uuid-5d9f109b-e277-4117-973e-c7e67e8422ab/super_vault/yson/Obsidian Super Vault/posts/"
attachments_dir = "/srv/dev-disk-by-uuid-5d9f109b-e277-4117-973e-c7e67e8422ab/super_vault/yson/Obsidian Super Vault/97 - Resources/"
static_images_dir = "/home/yson-server/projects/myblog/static/images"
output_dir = "/home/yson-server/projects/myblog/content/posts"  # Hugo content folder

# Ensure directories exist
os.makedirs(output_dir, exist_ok=True)
os.makedirs(static_images_dir, exist_ok=True)

# Process each markdown file in the posts directory
for filename in os.listdir(posts_dir):
    if filename.endswith(".md"):
        source_path = os.path.join(posts_dir, filename)
        output_path = os.path.join(output_dir, filename)  # Store the modified file here

        # Read the original markdown content
        with open(source_path, "r", encoding="utf-8") as file:
            content = file.read()

        # Find all image links in Obsidian format: ![[image.png]]
        images = re.findall(r'!\[\[([^]]*\.(png|jpg|jpeg|gif|webp))\]\]', content)

        # Replace image links and copy images
        new_content = content  # Keep the original content untouched
        for image in images:
            image_name = image[0]  # Extract filename
            image_path = os.path.join(attachments_dir, image_name)

            # Convert to Hugo-compatible format
            markdown_image = f"![Image Description](/images/{image_name.replace(' ', '%20')})"
            new_content = new_content.replace(f"![[{image_name}]]", markdown_image)

            # Copy image if it exists
            if os.path.exists(image_path):
                shutil.copy(image_path, os.path.join(static_images_dir, image_name))
                print(f"Copied: {image_name} → {static_images_dir}")

        # Write the modified content to the Hugo output directory
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(new_content)
        print(f"Processed: {filename} → {output_path}")

print("✅ Markdown files processed and copied to output directory.")
