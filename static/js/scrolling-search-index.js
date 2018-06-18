			$(document).ready(function () {
                $(window).bind('scroll', function () {
                    var navHeight = $(window).height() + 1200;
                    console.log(navHeight);
                    if ($(window).scrollTop() > navHeight) {
                        $('#defaultmenu').removeClass('fixed');
                        $('#nav-header').removeClass('affixed-brand');
                        $('#search-box-content').removeClass('affix');
                        $('#search-box-content').addClass('affixed');
                    }
                    else {
                        $('#defaultmenu').addClass('fixed');
                        $('#nav-header').addClass('affixed-brand');
                        //$('#search-box-content').addClass('affix');
                        $('#search-box-content').removeClass('affixed');
                    }
                });
            });