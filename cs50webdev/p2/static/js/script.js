document.addEventListener('DOMContentLoaded', () => {

  // 🌎 globals
  var channels;

  // 👩‍💻 check to see if screenname already in existence locally
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
  } else // load channel list
  {
    // do we need to do anything here? 🚨
  };

  // ⚡️ Function to add ability to add channel to channel list page
  document.querySelector('#add_channel').onclick = function() {

    // get names of currently listed channels
    var channel_name = JSON.parse(channels);
    var new_channel = document.getElementById('new_channel').value;

    // check to see if channel name already in use
    for (var i in channel_name) {
      if (channel_name[i] === new_channel){
        document.getElementById('new_channel').value = "";
        alert("Channel name already exists. Please retry.");
      };
    };

    // make XML request if everything okay
    const req = new XMLHttpRequest();
    req.open('POST', '/add_channel', true);
    var data = new_channel;
    console.log(new_channel);
    console.log(typeof new_channel);
    req.send(data);

    document.getElementById('new_channel').value = "";
    if (req.status === 200) {
      location.reload(true);
    };
  };
    // 🚨 end of all DOMContentLoaded logic
});
