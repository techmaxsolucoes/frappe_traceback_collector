if (!frappe.assets.handler.hasOwnProperty('html')){
    frappe.assets.handler['html'] = function(txt, src){
        frappe.templates[src.match(/([^\/]+)(?=\.\w+$)/)[0]] = txt.replace(/\$\.extend\(frappe\.\_messages\,\ (\{.*\})\)/, "");
    }
}

frappe.require([
    'assets/frappe_traceback_collector/templates/traceback_view.html',
    'assets/frappe_traceback_collector/templates/traceback_object.html'
]);

frappe.ui.form.on("Traceback", "load", function(frm){
    frm.set_read_only(true);
});

frappe.ui.form.on("Traceback", "refresh", function(frm){
    frm.set_df_property("view", "options", frappe.render_template("traceback_view", {"doc": frm.doc}));
});