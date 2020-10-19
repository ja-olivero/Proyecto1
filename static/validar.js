$(function()
{
  $("#form-despacho").validate
  ({
    rules:
    {
      nom:
      {
        required:true
      },
      apellido:
      {
        required:true
      },
      tel:
      {
        required:true
      },
      direc:
      {
        required:true
      },
      mail:
      {
        required:true
      },
      ciudad:
      {
        required:true
      },
      tipore:
      {
        required:true
      },
      zip:
      {
        required:true
      }
    },
    messages:
    {
      nom:
      {
        required:'Este campo es requerido',
        minlength:'Por favor ingresa al menos 5 carácteres'
      },
      apellido:
      {
        required:'Este campo es requerido',
        minlength:'Por favor ingresa al menos 5 carácteres'
      },
      tel:
      {
        required:'Este campo es requerido',
        minlength:'Por favor ingresa 9 carácteres',
        maxlength:'Por favor ingresa 9 carácteres'
      },
      direc:
      {
        required:'Este campo es requerido'

      },
      mail:
      {
        required:'Este campo es requerido'

      },
      ciudad:
      {
        required:'Este campo es requerido'

      },
      tipore:
      {
        required:'Este campo es requerido',
        minlength:'Por favor Ingrese un minimo de 4 caracteres',
        maxlength:'Ingrese un maximo de 13 caracteres'
      },
      zip:
      {
        required:'Este campo es requerido',
        minlength:'Por favor ingrese su zip minimo y maximo de 3 digitos',
        maxlength:'Por favor ingrese su zip minimo y maximo de 3 digitos'
      }
    }
  });
});
