var arry = [20,30,40,50,1]

var i = 0

while(i < (arry.length/2)) {
    var temp
    temp=arry[i];
    arry[i]= arry[arry.length-1-i];
    arry[arry.length-1-i]=temp;
    i++;
}

i=0;
while(i<arry.length){
    console.log(arry[i]);
    i++;
}