async function fetchPokemon(){
    var response = await fetch("https://pokeapi.co/api/v2/pokemon/pikachu/");
    var data = await response.json();
    console.log(data)
}
