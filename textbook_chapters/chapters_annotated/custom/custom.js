require([
    'base/js/namespace',
    'base/js/events'
], function(Jupyter, events) {
    events.on('app_initialized.NotebookApp', function() {
        var link = document.createElement("link");
        link.rel = "stylesheet";
        link.type = "text/css";
        link.href = "file:///C:/Users/DSKT/anaconda3/envs/PyWiggins/etc/jupyter/custom/custom.css";
        document.getElementsByTagName("head")[0].appendChild(link);
    });
});
