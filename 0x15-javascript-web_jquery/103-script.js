$(document).ready(function () {
  $('INPUT#btn_translate').click(translate);
  $('INPUT#language_code').focus(function () {
    $(this).keydown(function (event) {
      if (event.keyCode === 13) {
        translate();
      }
    });
  });
});

function translate () {
  const url = 'https://www.fourtonfish.com/hellosalut/hello/';
  $.get(url + $('INPUT#language_code').val(), function (data) {
    $('DIV#hello').text(data.hello);
  });
}
