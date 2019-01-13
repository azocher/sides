document.addEventListener('DOMContentLoaded', () => {

  // 🌎 globals
  var channels;
  var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

  // 🗒 if user closed last current session on channel, redirect to that channel
  if (window.history.length > 2) {
    localStorage.removeItem('path');
  } else if (localStorage.getItem("path")) {
    window.location.replace(localStorage.getItem("path"));
  };

  socket.on('connect', function() {
    // 👩‍💻 check to see if screenname already in existence locally
    if (!localStorage.getItem('screename')) {

      // display sn div/view
      var div_style = document.querySelector('#sign_in').style;
      div_style.zIndex = "7";
      div_style.display = "block";

      // on go button click set sn
      document.querySelector('#go').onclick = function() {
          var sn = document.querySelector('#sn_input').value;
          var avatar = document.querySelector('input[type=checkbox]:checked').value;
          localStorage.setItem('screename', sn);
          localStorage.setItem('avatar', avatar);
          socket.emit('new user', {'sn': sn, 'emoji': avatar});
          div_style.display = "none";
      };
    };
  });

    // check for incoming new users logging on
    socket.on('login', function(data) {
      const p = document.createElement('p');
      p.innerHTML = `${data.avatar} ${data.screename}`;
      document.querySelector("#current_users").append(p);
    });

    // ⚡️ Function to add ability to add channel to channel list page
    document.querySelector('#add_channel').onclick = function() {
      // query for new channel name
      var new_channel = document.getElementById('new_channel').value;

      // get names of currently listed channels
     var channels = document.querySelectorAll('#channel_list li');

     // check if channel name already in use
     var flag = true;
     channels.forEach( function(channel) {
       if (channel.innerText === new_channel) {
         document.getElementById('new_channel').value = "";
         alert("Channel name already exists. Please retry.");
         flag = false;
       };
     });
     if (flag != true) {
       return false;
     }

      function send_channel() {
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
      send_channel();
    };
    // 🚨 end of all DOMContentLoaded logic
});
