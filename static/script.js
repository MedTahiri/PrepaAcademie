function scrollToDiv(divId) {
    var element = document.getElementById(divId);
    element.scrollIntoView({behavior: 'smooth'});
};

var iframe = document.getElementById('pdf-frame');
iframe.onload = function () {
    this.style.height = this.contentWindow.document.body.scrollHeight + 'px';
};