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

    // Ch3-2_10  Components：List group-方法與事件,JavaScript 方法切換顯示標籤內容
    const list=$('#tab-demo .list-group a')
    list.click(function (event) {
        event.preventDefault()
        $(this).tab('show')
    })

    list.on('show.bs.tab', function (event) {
        console.log(`開始顯示:${ event.target.getAttribute('href')}`)
    })

    list.on('shown.bs.tab', function (event) {
        console.log(`完全顯示:${ event.target.getAttribute('href')}`)
    })

    list.on('hide.bs.tab', function (event) {
        console.log(`開始隱藏:${ event.target.getAttribute('href')}`)
    })

    list.on('hiden.bs.tab', function (event) {
        console.log(`完全影藏:${ event.target.getAttribute('href')}`)
    })


    // Ch3-2_12  Components：Modal:對話框的選項、方法與事件
    $('#modal-demo2').on('show.bs.modal', function() {
        console.log('show')
    })

    $('#modal-demo2').on('shown.bs.modal', function() {
        console.log('shown')
    })

    $('#modal-demo2').on('hide.bs.modal', function() {
        console.log('hide')
    })

    $('#modal-demo2').on('hidden.bs.modal', function() {
        console.log('hidden')
    })


    //Ch3-2_18  Components：Popovers：提示信息
    $('[data-toggle="popover"]').popover()

    //Ch3-2_21  Components：Tooltip 工具提示
    $('[data-toggle="tooltip"]').tooltip()
})