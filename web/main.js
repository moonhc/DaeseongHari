var pic_w = 2000;
var pic_h = 1150;
var bg_w, bg_h;
var time = 0;

// t=0 if heat sensor / t=1 if smoke sensor
var coord = {
    f1: [
    {t: 0, x: 6400, y: 19200}
    ],

    f2: [
    {t: 0, x: 4700, y: 6300},
    {t: 1, x: 9000, y: 6300},
    {t: 0, x: 6400, y: 16900},
    {t: 0, x: 19200, y: 11600},
    {t: 1, x: 4450, y: 1800},
    {t: 0, x: 9500, y: 2900},
    {t: 0, x: 4700, y: 9900},
    {t: 0, x: 4700, y: 12900},
    {t: 0, x: 7400, y: 10500},
    {t: 0, x: 7400, y: 12300},
    ]
};

var frame = {
    f1: [
        [0],
        [1],
        [1],
        [1]
    ],
    f2: [
        [0,0,0,0,0,0,0,0,0,0],
        [0,1,0,0,0,0,0,0,0,0],
        [0,1,1,1,0,0,0,0,0,0],
        [0,1,1,1,1,1,0,0,0,0]
    ]
};

function draw_floor(name, frame)
{
    var p = $(".floor." + name);
    var c = coord[name];
    for (var i=0; i<c.length; i++)
    {
        var r = c[i];
        if (name == 'f1') {
            var px = (354 + 0.042 * r.x) * bg_w / 2000;
            var py = (1064 - 0.04 * r.y) * bg_h / 1150;
        }
        else if (name == 'f2') {
            var px = (401.64 + 0.039 * r.x) * bg_w / 2000;
            var py = (1026.786 - 0.04 * r.y) * bg_h / 1150;
        }
        if (frame[i] == 0)
            continue;
        if (r.t)
            var e = $('<img src="yellow.gif"/>');
        else
            var e = $('<img src="red.gif"/>');
        var pr = 200 * bg_w / pic_w;
        e.css('top', py + 'px');
        e.css('left', px + 'px');
        e.css('width', pr + 'px');
        e.addClass("sensor");
        if (r.x == 4700)
            e.css('opacity', '1');
        else if (r.x == 9500)
            e.css('opacity', '0.75');
        p.append(e);
    }
}

function draw_frame(time)
{
    $(".sensor").remove();
    draw_floor('f1', frame.f1[time]);
    draw_floor('f2', frame.f2[time]);
}

function scale()
{
    var scr_w = $(window).width();
    var scr_h = $(window).height();
    scr_w = $(".container").width();
    scr_h = $(".container").height();
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
    draw_frame(2);
}

$(window).resize(resize_all);
$(window).ready(function() {
    resize_all();
});

$(document).keydown(function(e) {
    if (e.keyCode == 37) {
        time -= 1;
    }
    else if (e.keyCode == 39) {
        time += 1;
    }
    else return;
    draw_frame(time);
    console.log(time);
});
