import os
import re
import shutil

# Paths
posts_dir = "/srv/dev-disk-by-uuid-5d9f109b-e277-4117-973e-c7e67e8422ab/super_vault/yson/Obsidian Super Vault/posts/"
attachments_dir = "/srv/dev-disk-by-uuid-5d9f109b-e277-4117-973e-c7e67e8422ab/super_vault/yson/Obsidian Super Vault/97 - Resources/"
static_images_dir = "/home/yson-server/projects/myblog/static/images"
output_dir = "/home/yson-server/projects/myblog/content/posts"  # New directory to store modified copies

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Process each markdown file in the posts directory
for filename in os.listdir(posts_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(posts_dir, filename)
        output_path = os.path.join(output_dir, filename)  # Store the modified file here

        # Read the original markdown content
        with open(filepath, "r") as file:
            content = file.read()

        # Find all image links in the format [[image.png]]
        images = re.findall(r'\[\[([^]]*\.png)\]\]', content)

        # Replace image links and ensure URLs are correctly formatted
        new_content = content  # Keep the original content untouched
        for image in images:
            markdown_image = f"![Image Description](/images/{image.replace(' ', '%20')})"
            new_content = new_content.replace(f"[[{image}]]", markdown_image)

            # Copy the image to the Hugo static/images directory if it exists
            image_source = os.path.join(attachments_dir, image)
            if os.path.exists(image_source):
                shutil.copy(image_source, static_images_dir)

        # Write the modified content to a new file, not the original one
        with open(output_path, "w") as file:
            file.write(new_content)

print("Markdown files processed and copied to output directory without modifying originals.")

