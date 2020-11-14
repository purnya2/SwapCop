(function hideBlocked(){
    document.querySelectorAll('.WHAT IS THIS FUNCTION').forEach(div => div.setAttribute("style", "display: none;"));
    setTimeout(hideBlocked,500);

})();
