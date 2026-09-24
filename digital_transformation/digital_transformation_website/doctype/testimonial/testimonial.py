# Copyright (c) 2026, Yasmina Hussein and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Testimonial(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		author_location: DF.Data | None
		author_name: DF.Data | None
		author_organization: DF.Data | None
		author_photo: DF.AttachImage | None
		author_role: DF.Data | None
		display_order: DF.Int
		quote: DF.TextEditor | None
	# end: auto-generated types

	_DOCTYPE_NAME = "Testimonial"
