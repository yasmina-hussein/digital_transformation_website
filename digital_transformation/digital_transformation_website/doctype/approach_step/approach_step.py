# Copyright (c) 2026, Yasmina Hussein and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ApproachStep(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		description: DF.SmallText | None
		icon: DF.Literal["", "Search", "Pen", "Code", "Rocket", "Chart", "Refresh"]
		step_number: DF.Int
		title: DF.Data | None
	# end: auto-generated types

	_DOCTYPE_NAME = "Approach Step"
