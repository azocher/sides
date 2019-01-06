document.addEventListener('DOMContentLoaded', function() {
  // 📤 display existing channel messages

  // connect to socket
  var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

  // when socket connected, listen for message send button
  socket.on('connect', function() {

    // 📬 send message from user
    document.querySelector("#send_message").onclick = function() {
      var message = document.querySelector("#message").value;
      var sn = localStorage['screename'];
      var avatar = localStorage['avatar'];
      socket.emit('send message', {'message': message, 'sn': sn, 'emoji': avatar});
    };
  });

  socket.on('message received', function(data) {
    const p = document.createElement('p');
    p.innerHTML = `${data.avatar} ${data.screename} ${data.message}`;
    document.querySelector("#messages_container").append(p);
  })
});

 
