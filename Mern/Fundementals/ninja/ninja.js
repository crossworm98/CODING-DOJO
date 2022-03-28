class Ninja {
    constructor(name, health){
        this.name = name;
        this.health = health;
        this.speed = 3;
        this.strength = 3;
    }

    sayName(){
        console.log(this.name)
    }
    showStats(){
        console.log('Name:' + this.name, 'Health:' + this.health, 'Speed:' + this.speed, 'Strength:' + this.strength)
    }
    drinkSake(){
        this.health = this.health + 10;
        console.log('You drank sake! Your health is now:' + this.health)
    }
}
class Sensai extends Ninja {
    constructor(name, health, speed=3, strength=3){
        super(name, health);
        this.wisdom = 10
        this.speed = speed
        this.strength = strength
    }
    speakWisdom(){
        const wisdom = super.drinkSake()
        wisdom
        console.log('Man go to sleep with itchy butt, wake up with stinky finger.')
    }
}

const john = new Ninja('John', 100);
const wiseone = new Sensai('John The sensai', 100)
wiseone.speakWisdom();