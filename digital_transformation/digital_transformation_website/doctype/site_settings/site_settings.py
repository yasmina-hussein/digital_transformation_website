# Copyright (c) 2026, Yasmina Hussein and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class SiteSettings(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		about_hero_page: DF.AttachImage | None
		mission_statement: DF.SmallText | None
		total_counties: DF.Int
		total_countries: DF.Int
		vision_statement: DF.SmallText | None
		who_we_are: DF.TextEditor | None
	# end: auto-generated types

	_DOCTYPE_NAME = "Site Settings"
