$(document).ready(() => {
    $('#dropdown-demo3_2_6').on('show.bs.dropdown', ()=> {
        console.log('show')
    })

    $('#dropdown-demo3_2_6').on('shown.bs.dropdown', ()=> {
        console.log('shown')
    })

    $('#dropdown-demo3_2_6').on('hide.bs.dropdown', ()=> {
        console.log('hide')
    })

    $('#dropdown-demo3_2_6').on('hidden.bs.dropdown', ()=> {
        console.log('hidden')
    })
})