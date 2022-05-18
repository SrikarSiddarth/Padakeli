// initialize variables

var onclick = [];
var onmouseover = [];
var btns = [];
var side = 75;
var inputWord = '';

// puzzle variable stores the letter that form the puzzle
var puzzle = [];

for(var i=0; i<26; i++){
	puzzle[i] = String.fromCharCode(65+Math.random()*26)
}


// wait for the page to load

window.onload = function(){

	for(var i=0; i<16; i++){
		// get all the buttons
		btns[i] = document.getElementById('b'+i);
		btns[i].style.left = (i%4) * 80 + "px";
		btns[i].style.top = Math.floor((i/4)) * 80 + 'px';
		btns[i].style.width = side + 'px';
		btns[i].style.height = side + 'px';
		btns[i].innerHTML = puzzle[i]
		// console.log('b'+i)
	}
	
	archive = document.getElementById('archive');
	displayField = document.getElementById('displayField');
}


// define callback functions

function buttonClick(pos){
    for(var i=0;i<16;i++){
        onclick[i] = 0;
        onmouseover[i] = 0;
    }
    onclick[pos] = 1;
    btns[pos].style.backgroundColor = 'orange';
    inputWord += puzzle[pos];
    displayField.innerHTML = inputWord;
    // btns[pos].style.color = 'white';

    // console.log('button: '+pos+' was pressed!')
}

function mouseover(pos){
	if (onclick.includes(1)){
		onmouseover[pos] = 1;
		btns[pos].style.backgroundColor = 'orange';
		inputWord += puzzle[pos];
		displayField.innerHTML = inputWord;
		// console.log(onclick)
  //   	console.log('button: '+pos+' was hovered upon!')	
	}

    
}


// document.body.addEventListener('mousedown', fucntion(){
// 	displayField.innerHTML = inputWord;
// });

document.body.addEventListener('mouseup', function(){
    for(var i=0;i<16;i++){
        onclick[i] = 0;
        onmouseover[i] = 0;
        btns[i].style.backgroundColor = 'skyblue';
    }
    if(inputWord){
    	archive.innerHTML += inputWord + '<br>';
    	inputWord = '';	
    	displayField.innerHTML = '';
    }    
    // console.log(onclick)
    // console.log('mouseup')
});

