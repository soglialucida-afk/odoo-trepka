FROM odoo:19.0

USER root

# Kopiraj naš modul v Odoo addons mapo
COPY ./trepka_maserka /mnt/extra-addons/trepka_maserka

# Nastavi pravice
RUN chown -R odoo:odoo /mnt/extra-addons/

USER odoo

# Odoo config
COPY ./odoo.conf /etc/odoo/odoo.conf
