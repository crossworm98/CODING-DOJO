function pizzaoven(crustType, sauceType, cheeses, toppings){
    var pizza = {};
    pizza.crustType = crustType;
    pizza.sauceType = sauceType;
    pizza.cheeses = cheeses;
    pizza.toppings = toppings;
    return pizza;
}

function possibletoppings(){
    pizza.toppings.value = "";
    var possibletoppings = [
        "Pepperoni",
        "sausage",
        "onions",
        "pineapple",
        "mushrooms",
        "olives",
        "peppers",
        "steak"
    ];
    var randomanswer = possibletoppings[Math.floor(Math.random() * possibletoppings.length)];
    pizza.toppings = randomanswer;
}


var s1 = pizzaoven("thin crust", "pizza sauce", ["mozzarella", "gouda", "parmasan"], ["peperoni", "sausage", "pineapple"])

console.log(s1)