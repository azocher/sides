document.addEventListener('DOMContentLoaded', () => {

    // check to see if screenname already in existence locally
  if (!localStorage.getItem('screename')) {

    // display sn div/view
    var div_style = document.querySelector('#sign_in').style;
    div_style.zIndex = "7";
    div_style.display = "block";

    // on go button click set sn
    document.querySelector('#go').onclick = function() {
        var sn = document.querySelector('#sn_input').value;
        localStorage.setItem('screename', sn);
        div_style.display = "hidden";
    };
  };
});
