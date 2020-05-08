let socket = io();
let canvas = document.getElementsByClassName('whiteboard')[0];
let colors = document.getElementsByClassName('color');
let context = canvas.getContext('2d');

let current = {
	color: 'black',
};
let drawing = false;

canvas.addEventListener('mousedown', on_mouse_down, false);
canvas.addEventListener('mouseup', on_mouse_up, false);
canvas.addEventListener('mouseout', on_mouse_up, false);
canvas.addEventListener('mousemove', throttle(on_mouse_move, 16), false);

canvas.addEventListener('touchstart', on_mouse_down, false);
canvas.addEventListener('touchend', on_mouse_up, false);
canvas.addEventListener('touchcancel', on_mouse_up, false);
canvas.addEventListener('touchmove', throttle(on_mouse_move, 16), false);

for (let i = 0; i < colors.length; ++i){
	colors[i].addEventListener('click', on_color_update, false);
}

socket.on('drawing', on_drawing_event);
socket.on('connect', function (data) { console.log(data); });
socket.on('message', function (data) { console.log(data); });

window.addEventListener('resize', on_resize, false);
on_resize();

function draw_line(x0, y0, x1, y1, color, emit){
	context.beginPath();
	context.moveTo(x0, y0);
	context.lineTo(x1, y1);
	context.strokeStyle = color;
	context.lineWidth = 4;
	context.stroke();
	context.closePath();

	if (!emit)
		return;
	let w = canvas.width;
	let h = canvas.height;

	socket.emit('drawing', {
		x0: x0 / w,
		y0: y0 / h,
		x1: x1 / w,
		y1: y1 / h,
		c: color
	});
}

function on_mouse_down(e){
	drawing = true;
	current.x = e.clientX || e.touches[0].clientX;
	current.y = e.clientY || e.touches[0].clientY;
}

function on_mouse_up(e){
	if (!drawing)
		return;
	drawing = false;
	draw_line(current.x, current.y, e.clientX || e.touches[0].clientX, e.clientY || e.touches[0].clientY, current.color, true);
}

function on_mouse_move(e){
	if (!drawing)
		return;
	draw_line(current.x, current.y, e.clientX || e.touches[0].clientX, e.clientY || e.touches[0].clientY, current.color, true);
	current.x = e.clientX || e.touches[0].clientX;
	current.y = e.clientY || e.touches[0].clientY;
}

function on_color_update(e){
	current.color = e.target.className.split(' ')[1];
}

function throttle(callback, delay) {
	let previous = new Date().getTime();
	return function() {
		let time = new Date().getTime();

		if ((time - previous) >= delay) {
			previous = time;
			callback.apply(null, arguments);
		}
	};
}

function on_drawing_event(data){
	let w = canvas.width;
	let h = canvas.height;
	draw_line(data.x0 * w, data.y0 * h, data.x1 * w, data.y1 * h, data.c);
}

function on_resize() {
	canvas.width = window.innerWidth;
	canvas.height = window.innerHeight;
}
