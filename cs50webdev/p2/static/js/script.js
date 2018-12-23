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
  }

  // make AJAX request for channel_list
  var channels;
  const request = new XMLHttpRequest();
  request.open('GET', '/channels', true);

  request.onload= function() {
    channels = request.response;
    var jsoned = JSON.parse(channels);
    for (var i in jsoned) {
      var ul = document.getElementById("channel_list");
      var newli = document.createElement("li");
      newli.innerHTML = "<a href='#'>" + jsoned[i] + "</a>";
      ul.appendChild(newli);
    };
  };
  request.send();

  var channel_name = JSON.parse(channels);
  // function to add channel to list
  document.getElementById("add_a_channel").onclick = check_channel();

  function check_channel() {
    // check and see if value conflicts with any values in channel list
    for (var i in channel_name) {
      var new_channel = document.getElementById('new_channel').value;
      if (channel_name[i] === new_channel){
        document.getElementById('new_channel').value = "";
        alert("Channel name already exists. Please retry.");
      };
    };
  };

    // have to make API call to send data to Flask
    const request_add_channel = new XMLHttpRequest();
    request_add_channel.open('POST', '/add_channel', true);


    request_add_channel.send(new_channel);
  };
});
