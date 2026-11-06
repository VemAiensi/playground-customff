// Copyright (c) 2026, tryme and contributors
// For license information, please see license.txt

frappe.ui.form.on("Profile", {
	refresh(frm) {},
	first_name(frm) {
		console.log("You're editing the first name field");

		// lastName = frm.doc.last_name;
		// console.log(lastName);

		// frm.set_value("last_name", Math.random());
		frm.trigger("update_full_name");
	},
	middle_name(frm) {
		frm.trigger("update_full_name");
	},
	last_name(frm) {
		frm.trigger("update_full_name");
	},
	husbands_name(frm) {
		frm.trigger("update_full_name");
	},
	suffix(frm) {
		frm.trigger("update_full_name");
	},

	update_full_name(frm) {
		function capitalize(str) {
			if (str.trim()) {
				const tokens = str.split(" ");
				const capitalizedTokens = tokens.map((token) => {
					const firstLetter = token.charAt(0).toUpperCase();
					return firstLetter + token.slice(1).toLowerCase();
				});

				return capitalizedTokens.join(" ");
			} else return "";
		}

		lastName = capitalize(frm.doc.last_name);
		firstName = capitalize(frm.doc.first_name);
		middleName = capitalize(frm.doc.middle_name);
		husbandName = capitalize(frm.doc.husbands_name);
		suffix = frm.doc.suffix;

		frm.set_value(
			"full_name_lfm",
			`${lastName}, ${firstName}${suffix && " " + suffix}, ${middleName}${husbandName && " -" + husbandName}`,
		);
	},
});
