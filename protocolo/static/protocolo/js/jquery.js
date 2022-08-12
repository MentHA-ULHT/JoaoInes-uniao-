console.log("jquery.js loaded");
$(document).ready(function () {

    $(document).on("click", ".report-button", function () {
        document.getElementById("overlay").style.display = "flex";
        document.getElementById("overlay").style.zIndex = "100";
    })


    function off() {
        document.getElementById("overlay").style.display = "none";
        document.getElementById("overlay").style.zIndex = "2";
    }

    var seconds = 0;
    var ticking = false;

    function tick() {
        if (ticking) {
            var counter = document.getElementById("clock");
            seconds++;
            counter.innerHTML =
                "0:" + (seconds < 10 ? "0" : "") + String(seconds);
            if (seconds < 60) {
                setTimeout(tick, 1000);
            } else {
                document.getElementById("clock").innerHTML = "1:00";
            }
        }
    }

    $(document).on("click", ".btn-timer", function () {
        ticking = (ticking == true) ? false : true
        tick();
    })


    $(document).on("click", ".delete-same-id", function () {
        id = this.id;
        id = id.replace(/\s/g, '');
        console.log(id)
        var list = document.querySelectorAll('#collapse' + $.trim(id))

        for (i = 0; i < list.length; i++) {
            if (i >= 1) {
                list[i].remove();
            }
        }
    })

    $(document).on("click", ".toggle", function () {
        console.log("on toggle")
        console.log($(this).id)
        e = $(document).getElementsByClassName($(this).id)
        e.toggle();

    });

    $(document).on("click", ".jq-btn", function () {
        element = $(this)
        var href = element.attr("data-href");
        last_url = href;

        if (element.hasClass('nav-link')) {
            $(".nav-link").removeClass("active");
        }

        $(this).addClass('active')

        $.ajax({
            method: 'GET',
            url: href,
            success: function (data) {
                console.log(href);
                console.log("Success!");
                $('.page-content').html(data);
                seconds = 0;
                ticking = false;
                off()
            },
            error: function () {
                console.log("Error!");
                alert("Pagina não disponível.");
            }
        });
    });

    $(document).on("click", ".btn-submit", function () {
        event.preventDefault();
        var href = $(this).attr("data-href");
        const csrf_token = Cookies.get('csrftoken');
        var post_data = $("#question-form").serialize();

        $.ajax({
            method: 'POST',
            url: href,
            data: post_data,
            headers: {'X-CSRFToken': csrf_token},
            async: false,
            success: function (data) {
                console.log("Success!")
                $('.page-content').html(data);
                return false;
            },
            error: function () {
                console.log("Error!");
                alert("Pagina não disponível.");
            }
        })
    });

    $(document).on("click", ".btn-submit-upl", function () {
        event.preventDefault();
        var form = $("#upl-form");
        var form_data = new FormData(form[0]);
        var href = $(this).attr("data-href");
        const csrf_token = Cookies.get('csrftoken');

        console.log(form_data);
        $.ajax({
            method: 'POST',
            url: href,
            data: form_data,
            mimeType: "multipart/form-data",
            headers: {'X-CSRFToken': csrf_token},
            contentType: false,
            processData: false,
            async: false,
            success: function (data) {
                console.log("Success!")
                $('.page-content').html(data);
                return false;
            },
            error: function () {
                console.log("Error!");
                alert("Pagina não disponível.");
            }
        })
    });

    $(document).on("click", ".jq-report-btn", function () {
        console.log();
        $.ajax({
            method: 'POST',
            url: href,
            data: form_data,
            mimeType: "multipart/form-data",
            headers: {'X-CSRFToken': csrf_token},
            contentType: false,
            processData: false,
            async: false,
            success: function (data) {
                console.log("Success!")
                $('.container').html(data);
                return false;
            },
            error: function () {
                console.log("Error!");
                alert("Pagina não disponível.");
            }
        })
    });
});