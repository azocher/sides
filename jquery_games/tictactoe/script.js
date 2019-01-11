$(function() {
  var current_user = "X";
  var game_turns = 0;
  var game_board = [
  ]
  var winning_combos = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [6, 4, 2],
  ]
  var current_possible = [

  ]

  // event listener for turn
  $("td").click(function() {
    console.log($(this));
    // which piece got clicked
    var row = $(this.parentNode).index();
    var board_piece = $(this).index();
    if (current_user === "X") {
      game_turns++
      $(this).text(current_user);$
      current_user = "O";
      $("#user").text(current_user);
    } else {
      game_turns++
      $(this).text(current_user);
      current_user = "X";
      $("#user").text(current_user);
    };
  });
});
