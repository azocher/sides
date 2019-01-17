// template for what should be added to DOM anytime I role dice
Handlebars.registerHelper('message', function(info) {
  return info.partOne + " " + info.partTwo;
});

const template = Handlebars.compile("<li>Random puppy: <img src=\"img/{{ value }}.jpg\"></li>");
const welcome = Handlebars.compile("<h3>{{ message info }}</h3>");



document.addEventListener('DOMContentLoaded', function() {
  console.log("made it this far!");
  document.querySelector('#roll').onclick = function() {

    // generate a random roll
    const roll = Math.floor((Math.random() * 6) + 1);

    // Add roll result to DOM
    const content = template({'value': roll});
    document.querySelector('#rolls').innerHTML += content;

    // add new message to DOM
    const test = welcome({'info': {'partOne': 'Hi, there', 'partTwo': "someone!"}});
    document.querySelector("#message").innerHTML = test;
  };
});
