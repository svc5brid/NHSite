$(document).ready(function(){
    const bslider = $(".slider")
    bslider.on("beforeChange", (event, slick, currentSlide, nextSlide) => {
        bslider.find(".slick-slide").each((index, el) => {
            const tiles = $(el),
            slickindex = tiles.attr("data-slick-index");
            if (nextSlide == slick.slideCount - 1 && currentSlide == 0) {
            // 現在のスライドが最初のスライドでそこから最後のスライドに戻る場合
            if (slickindex == "-1") {
                // 最後のスライドに対してクラスを付与
                tiles.addClass("is-active-next");
            } else {
                // それ以外は削除
                tiles.removeClass("is-active-next");
            }
            } else if (nextSlide == 0) {
            // 次のスライドが最初のスライドの場合
            if (slickindex == slick.slideCount) {
                // 最初のスライドに対してクラスを付与
                tiles.addClass("is-active-next");
            } else {
                // それ以外は削除
                tiles.removeClass("is-active-next");
            }
            } else {
            // それ以外は削除
            tiles.removeClass("is-active-next");
            }
        });
        });
    slider = bslider.slick({
        autoplay: false,//自動的に動き出すか。初期値はfalse。
        infinite: true,//スライドをループさせるかどうか。初期値はtrue。
        speed: 500,//スライドのスピード。初期値は300。
        slidesToShow: 1,//スライドを画面に3枚見せる
        slidesToScroll: 1,//1回のスクロールで1枚の写真を移動して見せる
        prevArrow: '<div class="slick-prev"></div>',//矢印部分PreviewのHTMLを変更
        nextArrow: '<div class="slick-next"></div>',//矢印部分NextのHTMLを変更
        centerMode: true,//要素を中央ぞろえにする
        variableWidth: true,//幅の違う画像の高さを揃えて表示
        dots: true,//下部ドットナビゲーションの表示
        
    });

    
    $(".app_th").on("click", function(){
        var a = Array.from($(".app_th").not(this))
        a.forEach(function(i){
            i.classList.remove("app_th_selected")
        })
        this.classList.add("app_th_selected")
        
        if($(this).hasClass("app_th_home")){
            change("home")
        }else if($(this).hasClass("app_th_all")){
            change("all")
            slider.slick('setPosition')
        }else if($(this).hasClass("app_th_R")){
            change("app_td_R")
            slider.slick('setPosition')
        }else if($(this).hasClass("app_th_E")){
            change("app_td_E")
            slider.slick('setPosition')
        }else if($(this).hasClass("app_th_U")){
            change("app_td_U")
            slider.slick('setPosition')
        }else if($(this).hasClass("app_th_I")){
            change("app_td_I")
            slider.slick('setPosition')
        }else if($(this).hasClass("app_th_G")){
            change("app_td_G")
            slider.slick('setPosition')
        }else if($(this).hasClass("app_th_O")){
            change("app_td_O")
            slider.slick('setPosition')
        }
    })
    function change(mt){
        var home = document.getElementById("home")
        var content = document.getElementById("content")
        if(mt=="home"){
            home.classList.add("show")
            content.classList.remove("show")
        }else{
            home.classList.remove("show")
            content.classList.add("show")
            console.log(mt)
            
            bslider.slick('slickUnfilter');
            if(mt=="all"){
            }else{
                // slider.slick('slickFilter', ':even');
                bslider.slick('slickFilter', '.' + mt)
                // while($(".slick-track").children().length<4){

                // }
    
            }
        
            // $('.slider').slick('setPosition')
            
            // var apps = Array.from($(".tile"))
            // apps.forEach(function(i){
            //     i.classList.add("show_tile")
            //     if(!($(i).hasClass(mt))){
            //         i.classList.remove("show_tile")
            //     }
            // })
            // $('.slider').slick('setPosition');
            // $('.slider').slick({
            //     autoplay: true,//自動的に動き出すか。初期値はfalse。
            //     infinite: true,//スライドをループさせるかどうか。初期値はtrue。
            //     speed: 500,//スライドのスピード。初期値は300。
            //     slidesToShow: 3,//スライドを画面に3枚見せる
            //     slidesToScroll: 1,//1回のスクロールで1枚の写真を移動して見せる
            //     prevArrow: '<div class="slick-prev"></div>',//矢印部分PreviewのHTMLを変更
            //     nextArrow: '<div class="slick-next"></div>',//矢印部分NextのHTMLを変更
            //     centerMode: true,//要素を中央ぞろえにする
            //     variableWidth: true,//幅の違う画像の高さを揃えて表示
            //     dots: true,//下部ドットナビゲーションの表示
            // });
        }
        
    };
    
    
})

