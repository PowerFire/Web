$(document).ready(() => {
    /*Ch3-1  Components：Carousel-配置選項、方法與事件*/
    $('.components3_1_5').carousel({
        interval:1000
    })

    $('.components3_1_6').on('slide.bs.carousel', (event) => {
        console.log('slide: ', `
        方向: ${event.direction}
        從:${event.from}
        到:${event.to}
        `)
    })

    $('.components3_1_6').on('slid.bs.carousel', (event) => {
        console.log('slid: ', `
        方向: ${event.direction}
        從:${event.from}
        到:${event.to}
        `)
    })
})