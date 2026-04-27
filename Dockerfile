FROM odoo:19.0

USER root

COPY ./trepka_maserka /mnt/extra-addons/trepka_maserka
RUN chown -R odoo:odoo /mnt/extra-addons/

RUN printf "[options]\naddons_path = /mnt/extra-addons,/usr/lib/python3/dist-packages/odoo/addons\ndata_dir = /var/lib/odoo\n" > /etc/odoo/odoo.conf

USER odoo
# force rebuild Mon Apr 27 18:31:24 CEST 2026
