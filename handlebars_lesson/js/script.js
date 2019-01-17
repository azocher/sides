var source = document.getElementById("post_template").innerHTML;
var template = Handlebars.compile(source);

document.addEventListener("DOMContentLoaded", function() {
  var posts = {
    '1': {
      'title': "My first blog post!",
      'author': "Anna Zocher",
      'tag': "javascript",
      'body': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Fermentum odio eu feugiat pretium nibh ipsum consequat. A cras semper auctor neque vitae tempus quam. Vivamus at augue eget arcu dictum varius. Pretium vulputate sapien nec sagittis aliquam malesuada bibendum arcu."
      },
    '2': {
      'title': "My first blog post!",
      'author': "Anna Zocher",
      'tag': "javascript",
      'body': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Fermentum odio eu feugiat pretium nibh ipsum consequat. A cras semper auctor neque vitae tempus quam. Vivamus at augue eget arcu dictum varius. Pretium vulputate sapien nec sagittis aliquam malesuada bibendum arcu."
      },
    '3': {
      'title': "My first blog post!",
      'author': "Anna Zocher",
      'tag': "javascript",
      'body': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Fermentum odio eu feugiat pretium nibh ipsum consequat. A cras semper auctor neque vitae tempus quam. Vivamus at augue eget arcu dictum varius. Pretium vulputate sapien nec sagittis aliquam malesuada bibendum arcu."
      }
    }

    for (post in posts) {
      // get text to apply to post_template
      var content = template(posts[post]);

      // add new copy of template to container div
      console.log(content);
      document.querySelector(".container-fluid").innerHTML += content;
    }



});
