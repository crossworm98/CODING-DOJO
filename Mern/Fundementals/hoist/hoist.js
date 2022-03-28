////1
console.log(hello);                                   
var hello = 'world';                                 

var hello;
console.log(hello);
'world'
////////////////////////////////

////2
var needle = 'haystack';
test();
function test(){
    var needle = 'magnet';
    console.log(needle);
}

var needle;
function test()
console.log(needle);
'magnet'
////////////////////////////////

////3
var brendan = 'super cool';
function print(){
    brendan = 'only okay';
    console.log(brendan);
}
console.log(brendan);

var brendan;
function print()
console.log(brendan)
'only okay'
//////////////////////////////// 

////4 
var food = 'chicken';
console.log(food);
eat();
function eat(){
    food = 'half-chicken';
    console.log(food);
    var food = 'gone';
}

var food

