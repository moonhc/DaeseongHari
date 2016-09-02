var pic_w = 2000;
var pic_h = 1150;
var bg_w, bg_h;
var rooms = [];

var floor = 2;

var floor2 = [
{x: 4700, y: 6300},
{x: 9000, y: 6300},
{x: 6400, y: 16900},
{x: 19200, y: 11600},
{x: 4450, y: 1800},
{x: 9500, y: 2900},
{x: 4700, y: 9900},
{x: 4700, y: 12900},
{x: 7400, y: 10500},
{x: 7400, y: 12300},
];

function draw_rooms()
{
    $(".room").remove();
    var p = $(".floor");
    for (var i=0; i<rooms.length; i++)
    {
        r = rooms[i];
        var e = $("<div></div>");
        if (floor === 2) {
            var px = (401.64 + 0.039 * r.x) * bg_w / 2000;
            var py = (1026.786 - 0.04 * r.y) * bg_h / 1150;
            var pr = 30 * bg_w / pic_w;
        }
        e.css('top', py + 'px');
        e.css('left', px + 'px');
        e.css('width', pr + 'px');
        e.css('height', pr + 'px');
        e.css('border-radius', pr + 'px');
        e.addClass("room");
        p.append(e);
    }
}

function scale()
{
    var scr_w = $(window).width();
    var scr_h = $(window).height();
    var e = $(".floor");

    var w, h;
    if (scr_h * pic_w < scr_w * pic_h) {
        bg_h = scr_h;
        bg_w = scr_h * pic_w / pic_h;
        e.css('left', ((scr_w - bg_w) / 2) + 'px');
        e.css('top', 0);
    }
    else {
        bg_w = scr_w;
        bg_h = scr_w * pic_h / pic_w;
        e.css('top', ((scr_h - bg_h) / 2) + 'px');
        e.css('left', 0);
    }
    e.css('width', bg_w + 'px');
    e.css('height', bg_h + 'px');
}

function resize_all()
{
    scale();
    draw_rooms();
}

$(window).resize(resize_all);
$(window).ready(function() {
    rooms = floor2;
    resize_all();
});
