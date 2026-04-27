FROM odoo:19.0

USER root

COPY ./trepka_maserka /mnt/extra-addons/trepka_maserka
RUN chown -R odoo:odoo /mnt/extra-addons/

RUN echo "[options]" > /etc/odoo/odoo.conf && \
    echo "addons_path = /mnt/extra-addons,/usr/lib/python3/dist-packages/odoo/addons" >> /etc/odoo/odoo.conf && \
    echo "data_dir = /var/lib/odoo" >> /etc/odoo/odoo.conf

USER odoo
