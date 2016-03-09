$('.markdownx').on('markdownx.init', function() {
    console.log("INIT");
});

$('.markdownx').on('markdownx.update', function(e, response) {
    console.log("UPDATE" + response);
});

console.log("Hi! Here I am!");
var latex = document.getElementsByClassName("equation");
Array.prototype.forEach.call(latex, function(el) {
    katex.render(el.getAttribute("data-expr"), el, { displayMode: (el.getAttribute("data-expr") === "True") });
});