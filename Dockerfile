# Use the official Odoo image from Docker Hub
FROM odoo:17.0

# Copy your custom addons into the Odoo addons directory
COPY ./addons /mnt/extra-addons

# Copy your custom Odoo configuration file
COPY ./config/odoo.conf /etc/odoo/odoo.conf
