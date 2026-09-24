# Copyright (c) 2026, Yasmina Hussein and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class BlogPost(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		author: DF.Link | None
		category_tag: DF.Literal[None]
		content: DF.TextEditor | None
		featured_image: DF.AttachImage | None
		publish_date: DF.Date | None
		read_time_minute: DF.Int
		slug: DF.Data | None
		title: DF.Data | None
	# end: auto-generated types

	_DOCTYPE_NAME = "Blog Post"
