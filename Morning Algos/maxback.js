moveMaxToBack(){

    if(!this.head){ 
        console.log("There's nothing in this list ")
    }

    var runner = this.head;
    var maxNode = this.head.next;
    var beforeNode = this.head;
    var afterNode = this.head;

    while(runner.next != null){
        if(runner.next.value > maxNode.value){
            maxNode = runner.next;
            //checks max number
            beforeNode = runner;
            //saves the before list item and after item 
            afterNode = runner.next.next;
        }
        runner = runner.next
    }
    console.log(`here it is current Maximum value ${maxNode.value}`)
        //moving tail point to our new tail
    maxNode.next = null
    //making the current tail point to our new node
    this.tail.next = maxNode
    this.tail = maxNode
    // this.tail.next = null
    //tail pointing out to the null again
    console.log(`here is our new tail ${maxNode.value}`)
    beforeNode.next = afterNode;

}