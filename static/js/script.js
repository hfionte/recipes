/* Author: Holly Fionte

*/

$('a.add-ingredient, a.delete-ingredient').live('click', function (e) {
  e.preventDefault();
  var href = $(e.currentTarget).attr('href');
  $.get(href, function(data) {
    $('ul.ingredients').html(data);
  });
});

