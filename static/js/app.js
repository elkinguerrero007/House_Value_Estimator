$(document).ready(function() {
    $("form").submit(function(event) {
      event.preventDefault();
      $.ajax({
        type: "POST",
        url: "/predict",
        data: $('form').serialize(),
        success: function(response) {
          $('#result-container').show();
          $('#result').text('$' + response['prediction'].toFixed(2).toString());
        },
        error: function() {
          alert('Ha ocurrido un error al procesar la solicitud');
        }
      });
    });
  });
