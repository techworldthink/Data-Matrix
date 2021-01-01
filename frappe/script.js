frappe.ui.form.on("matrix", {
  refresh(frm) {},
  g_btn(frm) {
    frappe.call({
      method:"tharif_calculator.tharif_calculator.doctype.matrix.matrix.encode_data",
      args: {
        doctype: "matrix",
        name: frm.doc.name,
      },
      callback: (r) => console.log(r),
    });

    frappe.msgprint("Data matrix generated");
  },
});




/*
var doctype = "matrix";
    frappe.model.with_doc(doctype, { name: "tharif" }, function () {
      var values = frappe.model.get_list(doctype);
      console.log(values[0].name);
      let name = values[0].name;
    }),
*/
