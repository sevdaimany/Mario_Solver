let lock_right = true;
let lock_up = true;
let lock_down = true;
let mario;
let marios;
let html;
let htmls;
let body;
let bodies;
let numberAction = -1;

// 4 = down ; 1 = up ; 5  = big ; 2  = small ;
let input = [0, 0, 0, 1, 0, 0, 4, 0, 2, 0, 5, 0, 1, 0, 0, 4, 0, 0];
let size = true;
// let input = [0,1,0,2,0,2,0,1,0];
// 
let mapString = ['_', '_', '_', '_', 'G', '_', 'M', 'L', '_', '_', 'G', '_'];
// let mapString = [ '_', 'M', 'G', '_', 'L', '_'];
// let mapString = [ 'L', 'L', 'L', 'L', 'L', 'L'];

let width = 1350;
let lengthMap = 1350 / mapString.length;
let mario_x = 50;
let mario_y = 440;
// const mushroomSound = new Audio("./audio/eatMushroom.wav");
let ids = [];
const map_main = {
  create: function () {
    html = document.querySelector ('html');
    htmls = html.style;
    body = document.querySelector ('div');
    bodies = body.style;
    for (let i = 0; i < mapString.length; i++) {
      if (mapString[i] === 'M') {
        mushroom = document.createElement ('div');
        mushroomStyle = mushroom.style;
        body.appendChild (mushroom);
        mushroomStyle.width = '64px';
        mushroomStyle.height = '64px';
        mushroomStyle.backgroundImage = "url('./icons/Mushroom.png')";
        mushroomStyle.position = 'absolute';
        mushroomStyle.top = mario_y + 'px';
        mushroomStyle.left = `${lengthMap * i + 50}px`;
        let id = `mushroom${i}`;
        mushroom.id = id;
        ids.push (id);
      } else if (mapString[i] === 'G') {
        goompa = document.createElement ('div');
        goompaStyle = goompa.style;
        body.appendChild (goompa);
        goompaStyle.width = '64px';
        goompaStyle.height = '64px';
        goompaStyle.backgroundImage = "url('./icons/Goomba.png')";
        goompaStyle.position = 'absolute';
        goompaStyle.top = mario_y + 'px';
        goompaStyle.left = `${lengthMap * i+50}px`;
        let id = `goompa${i}`;
        goompa.id = id;
        ids.push (id);
      } else if (mapString[i] === 'L') {
        lakipo = document.createElement ('div');
        lakipoStyle = lakipo.style;
        body.appendChild (lakipo);
        lakipoStyle.width = '64px';
        lakipoStyle.height = '64px';
        lakipoStyle.backgroundImage = "url('./icons/Boo.png')";
        lakipoStyle.position = 'absolute';
        lakipoStyle.top = mario_y - 80 + 'px';
        lakipoStyle.left = `${lengthMap * i+50}px`;
        let id = `lakipo${i}`;
        lakipo.id = id;
        ids.push (id);
      }
    }
  },

  update: function () {
    htmls.width = '100%';
    htmls.height = '100%';
    htmls.margin = '0';

    bodies.width = '1400px';
    bodies.height = '600px';
    bodies.margin = '0px 0px 0px 50px';
    bodies.backgroundImage = "url('./icons/game3.jpg')";
    bodies.backgroundSize = 'cover';
  },
};

const map_mario = {
  create: function () {
    mario = document.createElement ('div');
    mario.id = 'mario';
    marios = mario.style;
    body.appendChild (mario);
  },

  update: function () {
    if (size === false) {
      marios.width = '50px';
      marios.height = '50px';
      marios.backgroundImage = "url('./icons/Mario.png')";
      marios.backgroundSize = 'cover';
    } else {
      marios.width = '64px';
      marios.height = '64px';
      marios.backgroundImage = "url('./icons/Mario.png')";
    }

    marios.position = 'absolute';
    marios.top = mario_y + 'px';
    marios.left = mario_x + 'px';
  },
};

const master_create = function () {
  map_main.create ();
  map_mario.create ();
};

const master_update = function () {
  map_main.update ();
  map_mario.update ();
  movement ();
  for (let i = 0; i < ids.length; i++) {
    CheckDiv (ids[i], i);
  }
  myReq = window.requestAnimationFrame (master_update);
};

const action = function (actionMario) {
  if (actionMario === 0) lock_right = false;
  if (actionMario === 1) lock_up = false;
  if (actionMario === 4) lock_down = false;
};

const release = function (actionMario) {
  if (actionMario === 0) lock_right = true;
  if (actionMario === 1) lock_up = true;
  if (actionMario === 4) lock_down = true;
};

const movement = function () {
  if (lock_up === false) mario_y -= 4;
  if (lock_right === false) mario_x += lengthMap / 30;
  if (lock_down === false) mario_y += 4;
};

function CheckDiv (divId, index) {
  var ediv1 = document.getElementById ('mario');
  var ediv2 = document.getElementById (divId);

  ediv1.top = $ (ediv1).offset ().top;
  ediv1.left = $ (ediv1).offset ().left;
  ediv1.right = Number ($ (ediv1).offset ().left) + Number ($ (ediv1).width ());
  ediv1.bottom =
    Number ($ (ediv1).offset ().top) + Number ($ (ediv1).height ());

  ediv2.top = $ (ediv2).offset ().top;
  ediv2.left = $ (ediv2).offset ().left;
  ediv2.right = Number ($ (ediv2).offset ().left) + Number ($ (ediv2).width ());
  ediv2.bottom =
    Number ($ (ediv2).offset ().top) + Number ($ (ediv2).height ());

  if (
    ediv1.right > ediv2.left &&
    ediv1.left < ediv2.right &&
    ediv1.top < ediv2.bottom &&
    ediv1.bottom > ediv2.top
  ) {
    // let sound = mushroomSound.play();
    // if (sound != undefined){
    //   sound.then(_ =>{

    //   }).catch(error=>{

    //   });
    // console.log(mario_x);
    // }
    ids.splice (index, 1);
    ediv2.remove ();
  }
}

function run () {
  let check = true;
  let id = setInterval (function () {
    if (numberAction === input.length) {
      check = false;
      release (1);
      release (4);
      release (0);
      clearInterval (id);
    }
    if (check) {
      release (input[numberAction]);
      numberAction++;
      if (input[numberAction] === 2) {
        size = false;
        numberAction++;
      } else if (input[numberAction] === 5) {
        size = true;
        numberAction++;
      }
      action (input[numberAction]);
      
    }
  }, 500);
}

master_create ();
master_update ();
run ();
