(function hideBlocked(){
    document.querySelectorAll('.message-group-blocked').forEach(div => div.setAttribute("style", "display: none;"));
    setTimeout(hideBlocked,500);

})();