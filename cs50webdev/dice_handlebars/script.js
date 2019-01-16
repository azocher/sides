// template for what should be added to DOM anytime I role dice
const template = Handlebars.compile("<li>Random puppy: <img src=\"img/{{ value }}.jpg\"></li>");

document.addEventListener('DOMContentLoaded', function() {
  document.querySelector('#roll').onclick = function() {

    // generate a random roll
    const roll = Math.floor((Math.random() * 6) + 1);

    // Add roll result to DOM
    const content = template({'value': roll});
    document.querySelector('#rolls').innerHTML += content;
  };
});
