# Copyright (c) 2026, Yasmina Hussein and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Capability(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from digital_transformation.digital_transformation_website.doctype.capability_features.capability_features import CapabilityFeatures
		from frappe.types import DF

		description: DF.TextEditor | None
		detail_link_url: DF.Data | None
		features: DF.Table[CapabilityFeatures]
		icon: DF.Attach | None
		image: DF.AttachImage | None
		image_caption: DF.Data | None
		number: DF.Int
		tagline: DF.Data | None
		title: DF.Data | None
	# end: auto-generated types

	_DOCTYPE_NAME = "Capability"
