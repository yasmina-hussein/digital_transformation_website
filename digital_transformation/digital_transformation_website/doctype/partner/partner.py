# Copyright (c) 2026, Yasmina Hussein and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Partner(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from digital_transformation.digital_transformation_website.doctype.focus_tag.focus_tag import FocusTag
		from frappe.types import DF

		category: DF.Literal["", "Strategic", "Technology", "Funding", "Implementation"]
		description: DF.SmallText | None
		external_url: DF.Data | None
		focus_area: DF.Table[FocusTag]
		logo: DF.AttachImage | None
		partner_name: DF.Data | None
	# end: auto-generated types

	_DOCTYPE_NAME = "Partner"
