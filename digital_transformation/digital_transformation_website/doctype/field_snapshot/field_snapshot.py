# Copyright (c) 2026, Yasmina Hussein and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class FieldSnapshot(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		category_tag: DF.Literal["", "Strategy & Innovation", "Field Operations", "Disaster Preparedness", "Capacity Building"]
		description: DF.SmallText | None
		featured: DF.Check
		image: DF.AttachImage | None
		title: DF.Data | None
	# end: auto-generated types

	_DOCTYPE_NAME = "Field Snapshot"
