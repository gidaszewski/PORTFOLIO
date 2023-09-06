/*!
* Start Bootstrap - Personal v1.0.1 (https://startbootstrap.com/template-overviews/personal)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-personal/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project
$(document).ready(function () {
    $(".project-card").each(function (index) {
        var card = $(this);
        setTimeout(function () {
            card.css("opacity", "1");
            card.css("transform", "translateY(0)");
        }, 200 * index); // Ajusta la velocidad de la cascada aquí
    });
});