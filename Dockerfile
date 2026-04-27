FROM odoo:19.0

USER root

COPY ./trepka_maserka /mnt/extra-addons/trepka_maserka
RUN chown -R odoo:odoo /mnt/extra-addons/

# Prebriši default config
RUN echo "[options]\naddons_path = /mnt/extra-addons,/usr/lib/python3/dist-packages/odoo/addons\n" > /etc/odoo/odoo.conf

USER odoo
