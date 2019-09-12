from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def validate_positive(value):
    if value < 0:
        raise ValidationError(
            _('%(value)s debe ser u numero positivo'),
            params={'value': value},
        )

def validate_porcentaje(valor):
	if valor>100 or valor<0:
		raise ValidationError(
			_('%(valor)s debe ser porcentaje [0,100]'),
			params={'valor':valor},
		)

def validate_digit(valor):
	if not valor.isdigit():
		raise ValidationError(_('deben ser digitos...'))