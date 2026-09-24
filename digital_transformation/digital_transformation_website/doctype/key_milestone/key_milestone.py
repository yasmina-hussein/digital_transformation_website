# Copyright (c) 2026, Yasmina Hussein and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class KeyMilestone(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		description: DF.SmallText | None
		image: DF.AttachImage | None
		image_caption: DF.Data | None
		is_verified_impact_milestone: DF.Check
		sort_order: DF.Int
		tag: DF.Data | None
		title: DF.Data | None
		year: DF.Int
	# end: auto-generated types

	_DOCTYPE_NAME = "Key Milestone"
