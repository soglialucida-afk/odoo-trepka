from odoo import http
from odoo.http import request
from datetime import datetime, timedelta

SERVICES = {
    'relax_45': ('Relaxacijska masaža 45 min', 45),
    'swedish_60': ('Švedska masaža 60 min', 60),
    'sports_90': ('Športna masaža 90 min', 90),
}

WORK_START = 9
WORK_END = 17
LUNCH_START = 12
LUNCH_END = 13
MASAZER_EMAIL = 'masaza@trepka.si'


def generate_slots(service_key, booking_date, booked_slots):
    if service_key not in SERVICES:
        return []
    _, duration = SERVICES[service_key]
    slots = []
    base = datetime(booking_date.year, booking_date.month, booking_date.day)
    current = base.replace(hour=WORK_START, minute=0)
    end = base.replace(hour=WORK_END, minute=0)
    lunch_s = base.replace(hour=LUNCH_START, minute=0)
    lunch_e = base.replace(hour=LUNCH_END, minute=0)

    while current + timedelta(minutes=duration) <= end:
        slot_end = current + timedelta(minutes=duration)
        overlaps_lunch = current < lunch_e and slot_end > lunch_s
        if not overlaps_lunch:
            slot_str = current.strftime('%H:%M')
            if slot_str not in booked_slots:
                slots.append(slot_str)
        current += timedelta(minutes=duration)
    return slots


class TrepkaController(http.Controller):

    @http.route('/', type='http', auth='public', website=True)
    def index(self, **kwargs):
        return request.render('trepka_maserka.homepage', {})

    @http.route('/rezervacija', type='http', auth='public', website=True)
    def rezervacija(self, **kwargs):
        return request.render('trepka_maserka.booking_page', {})

    @http.route('/rezervacija/slots', type='json', auth='public', website=True, methods=['POST'])
    def get_slots(self, date_str=None, service=None, **kwargs):
        try:
            booking_date = datetime.strptime(date_str, '%Y-%m-%d').date()
            if booking_date.weekday() == 6:
                return {'slots': []}
            booked = request.env['trepka.booking'].sudo().search([
                ('booking_date', '=', date_str),
                ('service', '=', service),
                ('state', '!=', 'cancelled'),
            ])
            booked_slots = [b.time_slot for b in booked]
            return {'slots': generate_slots(service, booking_date, booked_slots)}
        except Exception as e:
            return {'slots': [], 'error': str(e)}

    @http.route('/rezervacija/submit', type='http', auth='public', website=True, methods=['POST'], csrf=True)
    def rezervacija_submit(self, **kwargs):
        name = kwargs.get('name', '').strip()
        email = kwargs.get('email', '').strip()
        phone = kwargs.get('phone', '').strip()
        service = kwargs.get('service', '').strip()
        booking_date = kwargs.get('booking_date', '').strip()
        time_slot = kwargs.get('time_slot', '').strip()
        notes = kwargs.get('notes', '').strip()

        if not all([name, email, service, booking_date, time_slot]):
            return request.render('trepka_maserka.booking_page', {
                'error': 'Prosimo, izpolnite vsa obvezna polja.'
            })

        booking = request.env['trepka.booking'].sudo().create({
            'name': name, 'email': email, 'phone': phone,
            'service': service, 'booking_date': booking_date,
            'time_slot': time_slot, 'notes': notes,
        })

        service_name = SERVICES.get(service, (service, 0))[0]

        try:
            request.env['mail.mail'].sudo().create({
                'subject': f'Nova rezervacija: {service_name} — {booking_date}',
                'body_html': f'''
                    <h3>Nova rezervacija</h3>
                    <p><b>Ime:</b> {name}</p>
                    <p><b>E-mail:</b> {email}</p>
                    <p><b>Telefon:</b> {phone or "ni naveden"}</p>
                    <p><b>Storitev:</b> {service_name}</p>
                    <p><b>Datum:</b> {booking_date}</p>
                    <p><b>Termin:</b> {time_slot}</p>
                    <p><b>Opombe:</b> {notes or "/"}</p>
                ''',
                'email_to': MASAZER_EMAIL,
                'email_from': f'{name} <{email}>',
            }).send()
        except Exception:
            pass

        try:
            request.env['crm.lead'].sudo().create({
                'name': f'Rezervacija: {service_name} — {name}',
                'contact_name': name,
                'email_from': email,
                'phone': phone,
                'description': f'Datum: {booking_date}\nTermin: {time_slot}\nOpombe: {notes}',
            })
        except Exception:
            pass

        return request.render('trepka_maserka.booking_success', {
            'booking_name': name,
            'service_name': service_name,
            'booking_date': booking_date,
            'time_slot': time_slot,
        })

    @http.route("/blog", type="http", auth="public", website=True)
    def blog_index(self, **kwargs):
        posts = request.env["trepka.blog.post"].sudo().search([
            ("is_published", "=", True)
        ])
        return request.render("trepka_maserka.blog_index", {"posts": posts})

    @http.route("/blog/<string:slug>", type="http", auth="public", website=True)
    def blog_post(self, slug, **kwargs):
        post = request.env["trepka.blog.post"].sudo().search([
            ("slug", "=", slug),
            ("is_published", "=", True)
        ], limit=1)
        if not post:
            return request.not_found()
        return request.render("trepka_maserka.blog_post", {"post": post})
