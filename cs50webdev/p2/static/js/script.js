document.addEventListener('DOMContentLoaded', () => {

    // check to see if screenname already in existence locally
  if (!localStorage.getItem('screename')) {

    // display sn div/view
    var div_style = document.querySelector('#sign_in').style;
    div_style.zIndex = "7";
    div_style.display = "block";

    // on go button click set sn
    document.querySelector('#go').onclick = function() {
        console.log("clicked!");
        var sn = document.querySelector('#sn_input').value;
        var avatar = document.querySelector('input[type=checkbox]:checked').value;
        console.log(avatar);
        localStorage.setItem('screename', sn);
        localStorage.setItem('avatar', avatar);
        div_style.display = "hidden";
    };
  } else {
      // make AJAX request for channel_list
      const request = new XMLHttpRequest();
      request.open('GET', '/channels', true);

      request.onreadystatechange = function() {
        var channels = request.response;
        console.log(typeof channels);
        document.querySelector('#channel_list').innerText = channels;
        }

    request.send();
    console.log(request);
  };
});
