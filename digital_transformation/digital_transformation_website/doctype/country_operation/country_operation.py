# Copyright (c) 2026, Yasmina Hussein and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class CountryOperation(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from digital_transformation.digital_transformation_website.doctype.initiative.initiative import Initiative
		from frappe.types import DF

		country_name: DF.Data | None
		data_feeds_count: DF.Int
		description: DF.SmallText | None
		initiatives_count: DF.Int
		is_active_hub: DF.Check
		iso_code: DF.Data | None
		key_initiatives: DF.TableMultiSelect[Initiative]
		products_count: DF.Int
		region: DF.Literal["", "East Africa", "Horn of Africa"]
	# end: auto-generated types

	_DOCTYPE_NAME = "Country Operation"
