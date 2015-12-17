(function($,W,D)
{
jQuery.validator.addMethod("letrasusr", function(value, element) 
{
return this.optional(element) || /^[a-z,"_","@","-",".","+"]+$/i.test(value);
}, "Letters and spaces only please"); 
    var VALIDA = {};

    VALIDA.UTIL =
    {
        validacion: function()
        {

            $("#user_form").validate({
                rules: {
                    username: {
                        required: true,
                        minlength: 3,
			letrasusr: true
                    },

                    email: {
                        required: true,
                        email: true
                    },
                    password: {
                        required: true,
                        minlength: 5
                    },
                    password2: {
                        required: true,
                        minlength: 5
                    }
                },
                messages: {
                    username: {
                        required: "pon tu usuario",
                        minlength: "almenos de 3 caracteres",
			letrasusr: "caracteres normales y _@-.+"
                    },
                    password: {
                        required: "pon tu password",
                        minlength: "almenos de 5 caracteres"
                    },
                    password2: {
                        required: "repite tu password",
                        minlength: "almenos de 5 caracteres"
                    },
                    email: "pon un email valido"

                },
                submitHandler: function(form) {
                    form.submit();
                }
            });
        }
    }

    $(D).ready(function($) {
        VALIDA.UTIL.validacion();
    });

})(jQuery, window, document);
