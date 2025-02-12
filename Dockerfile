# Use the official lightweight Nginx image
FROM nginx:latest

# Remove default Nginx HTML files
RUN rm -rf /usr/share/nginx/html/*

# Copy Hugo-generated static files to Nginx
COPY public/ /usr/share/nginx/html

# Expose port 80
EXPOSE 80

