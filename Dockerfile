FROM odoo:19.0

USER root

COPY ./trepka_maserka /mnt/extra-addons/trepka_maserka

RUN chown -R odoo:odoo /mnt/extra-addons/

USER odoo
