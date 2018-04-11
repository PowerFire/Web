$(document).ready(() => {

    $('#gorm-demo').submit(function (event) {
        const form=$(this)
        if(form[0].checkValidity()===fakse) {
            event.preventDefault()
            event.stopPropagation()
        }

        form.addClass('was-validated')
    })
    






})