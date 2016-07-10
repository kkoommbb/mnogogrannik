$('.markdownx').on('markdownx.init', function() {
    console.log("INIT");
});

$('.markdownx').on('markdownx.update', function(e, response) {
    console.log("UPDATE" + response);
});