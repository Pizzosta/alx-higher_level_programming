$(document).ready(function () {
  const url = 'https://www.fourtonfish.com/hellosalut/?';
  $('INPUT#btn_translate').click(function () {
    $.get(url + $('INPUT#language_code').val(), function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
