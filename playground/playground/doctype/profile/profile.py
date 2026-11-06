# Copyright (c) 2026, tryme and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Profile(Document):
	def before_save(self):
		def capitalize(str):
			if str:
				tokens = str.split()
				capitalized_tokens = [token[0].upper() + token[1:].lower() for token in tokens ]
				return ' '.join(capitalized_tokens)
			else:
				return ''
			
			
			
		def set_full_name_lfm():
			last_name = self.last_name if self.last_name else ' '
			suffix = ' ' + self.suffix if self.suffix else ''
			middle_name = f"{self.middle_name}" if self.middle_name else ' '
			husbands_name = f" -{self.husbands_name}" if self.husbands_name else ''

			self.full_name_lfm = f"{last_name}, {self.first_name}{suffix}, {middle_name}{husbands_name}"

		def set_full_name_fml():
			def get_mi(str):
				tokens = str.split()
				token_length = len(tokens)
				initials = ''
				for token in tokens:
					initials = initials + ((token[0].upper()))

				return (initials[0].lower() + initials[1:]  if token_length > 1 else initials) + "." if str else ''

			
			# middle_initial = get_mi(self.last_name if self.last_name else self.middle_name) if self.husbands_name else (get_mi(self.middle_name) if self.last_name else '')

			if self.husbands_name:
				if self.last_name:
					middle_initial = ' ' + get_mi(self.last_name)
				else:
					middle_initial =  ' ' +  get_mi(self.middle_name) if self.middle_name else ''
			else:
				if self.last_name:
					middle_initial =  ' ' + get_mi(self.middle_name) if self.middle_name else ''
				else: middle_initial = ''

			last_name = ' ' + self.husbands_name if self.husbands_name else (' ' + self.last_name if self.last_name else (' ' + self.middle_name if self.middle_name else ''))
			suffix = ' ' + self.suffix if self.suffix else ''

			self.full_name_fml = f"{self.first_name}{middle_initial}{last_name}{suffix}"

		self.first_name = capitalize(self.first_name)
		self.middle_name = capitalize(self.middle_name)
		self.last_name = capitalize(self.last_name)
		self.husbands_name = capitalize(self.husbands_name)

		set_full_name_lfm()
		set_full_name_fml()