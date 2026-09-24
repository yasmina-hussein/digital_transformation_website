# Copyright (c) 2026, Yasmina Hussein and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class CoreValue(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		description: DF.SmallText | None
		number: DF.Int
		sort_order: DF.Int
		title: DF.Data | None
	# end: auto-generated types

	_DOCTYPE_NAME = "Core Value"
