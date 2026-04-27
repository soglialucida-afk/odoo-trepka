FROM odoo:19.0

USER root

COPY ./trepka_maserka /usr/lib/python3/dist-packages/odoo/addons/trepka_maserka
RUN chown -R odoo:odoo /usr/lib/python3/dist-packages/odoo/addons/trepka_maserka

USER odoo
